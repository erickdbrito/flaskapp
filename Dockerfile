# ------------------ Prepare Python environment ------------------ #

FROM python:3.9.5-slim-buster

# ---------------  CONFIGURING  ------------------ #

WORKDIR /app

RUN apt-get -y update

COPY ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r /var/www/requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python3", "main.py" ]
