FROM python:3.9
MAINTAINER maximnudler@gmail.com

COPY . /automationbro

WORKDIR /automationbro

RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "--junitxml=reports/result.xml"]

CMD tail -f /dev/null