FROM python:3.7

WORKDIR /catvsdog

COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple && \
python manage.py makemigrations && \
python manage.py migrate