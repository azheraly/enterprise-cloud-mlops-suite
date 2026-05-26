FROM python:3.12-slim

WORKDIR /code 
COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install  --no-cache-dir --upgrade  -r /code/requirements.txt

COPY . /code

EXPOSE 5001

CMD ["python", "app.py"]
