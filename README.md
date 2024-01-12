# hikvision-isapi-web-client

Web client to remote control compatible HIKVISION devices via ISAPI

## Features

Only supports controlling Access Control device right now. Feel free to contribute.

Can schedule with [APScheduler](https://apscheduler.readthedocs.io/). Check [app.py](src/app.py) for example.

## Docker usage

Setup `.env` file from template `.env.example` and run:

```shell
docker run --rm \
    --env-file ./.env \
    -p 5000:5000 \
    -e VERIFY_SSL=true \
    -it ghcr.io/jackblk/hikvision-isapi-web-client:latest
```

Access server at <http://localhost:5000/>

## Usage

* Clone repo
* [Activate virtual env](https://docs.python.org/3/library/venv.html) and install
dependencies: `pip install -r requirements.txt`
* Copy `.env.example` to `.env` file, fill in credentials
* Run server: `flask --app src/app.py run`
* Access server at <http://localhost:5000/>

### Environment variables

* `VERIFY_SSL`: Any value that's not `true` will ignore the SSL validation. Default: `true`.

### Use with WSGI

**WSGI servers like Gunicorn is NOT FULLY supported** since there might be unforeseen
issues related to multiple workers.

* Run server: `gunicorn --preload --chdir ./src 'app:app'`
* Access server at <http://localhost:8000/>

Without `--preload`, multiple workers will cause the cronjob to be executed on each worker.

On Mac, use `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` to [avoid fork issue](https://stackoverflow.com/questions/50168647/multiprocessing-causes-python-to-crash-and-gives-an-error-may-have-been-in-progr).

## Development

Same as [Usage](#usage) but use `flask --app src/app.py --debug run` instead to
watch for changes & auto reload.

Access the dev server at <http://localhost:5000>

Docker build:

```shell
docker build --rm \
    -t ghcr.io/jackblk/hikvision-isapi-web-client:latest \
    .
```
