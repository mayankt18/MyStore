FROM python

ADD . /app

COPY ./requirements.txt ./app/requirements.txt

WORKDIR /app

RUN pip install wheel

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT python manage.py runserver

