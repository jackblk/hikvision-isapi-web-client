FROM python:3.10-alpine

ENV TZ=Asia/Ho_Chi_Minh
ENV LOG_LEVEL=INFO

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

EXPOSE 5000
CMD ["flask", "--app", "src/app.py", "run", "--host", "0.0.0.0"]
