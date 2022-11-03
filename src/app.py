import logging
import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_apscheduler import APScheduler

from hikvision_isapi_client.client import HikvisionClient

load_dotenv()

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger("gunicorn.error")
app.logger.setLevel(os.getenv("LOG_LEVEL", logging.INFO))
app.logger.handlers.extend(gunicorn_error_logger.handlers)
scheduler = APScheduler()
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

hikvision_client = HikvisionClient(
    base_url=os.getenv("HIK_URL", ""),
    username=os.getenv("HIK_USERNAME", ""),
    password=os.getenv("HIK_PASSWORD", ""),
)
app.logger.info(f"App is setup with base URL {hikvision_client.base_url}")


@app.route("/")
def main():
    # TODO: fetch door list from server, hardcoding door #1 for now
    return render_template("door.html", door_list=range(1, 2))


@app.route("/door/<string:door_id>", methods=["POST"])
def door_control(door_id):
    json_data = request.json
    if json_data is None:
        return {
            "message": "error controling door",
            "error": "bad request data",
        }, 400

    res = hikvision_client.remote_control_door(
        door_id=door_id, command=json_data["command"]
    )
    app.logger.debug(
        f"Remote control response from server: {res.status_code} | {res.text}"
    )
    if res.status_code == 200:
        return {
            "message": f"Door {door_id} status: {json_data['command']}"
        }, res.status_code
    return {
        "message": "error controling door",
        "error": res.text,
    }, res.status_code


# Close the door at 18:00 everyday
# Lesser fields default to their minimum values (0)
# https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html#module-apscheduler.triggers.cron
@scheduler.task("cron", id="close_door", hour=18)
def job_close_door():
    res = hikvision_client.remote_control_door(door_id="1", command="close")
    app.logger.info(
        f"[Cronjob] DOOR CLOSE - status: {res.status_code}",
    )


if __name__ == "__main__":
    app.run()
