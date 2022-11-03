# hikvision-isapi-web-client

Web client to remote control compatible HIKVISION devices via ISAPI

## Features

Only supports controlling Access Control device right now. Feel free to contribute.

Can schedule with [APScheduler](https://apscheduler.readthedocs.io/). By default it will
lock the door 1 at 18:00 everyday.

## Usage

* Clone repo
* [Activate virtual env](https://docs.python.org/3/library/venv.html) and install
dependencies: `pip install -r requirements.txt`
* Copy `.env.example` to `.env` file, fill in credentials
* Run server: `flask --app src/app.py run`
* Access server at <http://localhost:5000/>

### Use with WSGI

**WSGI servers like Gunicorn is NOT FULLY supported** since there might be unforeseen
issues related to multiple workers.

* Run server: `gunicorn --preload --chdir ./src 'app:app'`
* Access server at <http://localhost:8000/>

Without `--preload`, multiple workers will cause the cronjob to be executed on each worker.

## Development

Same as [Usage](#usage) but use `flask --app src/app.py --debug run` instead to
watch for changes & auto reload.

Access the dev server at <http://localhost:5000>
