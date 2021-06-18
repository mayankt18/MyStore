FROM python:3

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .



RUN python manage.py collectstatic --no-input

RUN python manage.py migrate --no-input


# ENTRYPOINT ["sh","-c", "entrypoint.sh"]
