FROM python:3.10.13-alpine3.19

RUN apk update && apk add git

ARG WORK_DIR=/backend

WORKDIR ${WORK_DIR}

COPY requirements.txt ${WORK_DIR}

RUN pip install --no-cache-dir -r requirements.txt

COPY . ${WORK_DIR}

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000