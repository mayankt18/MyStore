FROM python:3

RUN pip install --upgrade pip


WORKDIR /app


COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh ./


# RUN python manage.py collectstatic --no-input

# RUN chmod 777 /app


ENTRYPOINT ["bash", "/app/entrypoint.sh"]
