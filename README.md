# Cat Vs Dog

Fork from https://github.com/Missyanc/CatVsDog

Online demo: https://catvsdog.cloudevops.cn

## Environment

* python3.6+

## Quick Start

### Docker

```shell script
docker-compose up -d

```

### Manual

```shell script
# Install requirements
pip install -r requirements.txt

# Init db
python manage.py makemigrations && python manage.py migrate

# Runserver
python manage.py runserver

```

## Known issues

* cv2 errors during manual start

Solved: https://blog.csdn.net/yuanlulu/article/details/79017116

## Contact

hsowan.me@gmail.com

