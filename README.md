# hikvision-isapi-web-client

Web client to remote control compatible HIKVISION devices via ISAPI

## Features

Only supports controling Access Control device right now. Feel free to contribute.

## Usage

* Clone repo
* [Activate virtual env](https://docs.python.org/3/library/venv.html) and install
dependencies: `pip install -r requirements.txt`
* Copy `.env.example` to `.env` file, fill in credentials
* Run server: `flask --app src/app.py run`
* Access server at <http://localhost:8000/>

**WSGI servers like Gunicorn is NOT supported**, can only run via single thread Flask.

## Development

Same as [Usage](#usage) but use `flask --app src/app.py --debug run` instead to
watch for changes & auto reload.
