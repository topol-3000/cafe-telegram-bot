# Cafe Telegram Bot

## Requirements
1. docker version __20.10.x__
2. docker-compose version __2.13.x__

## Getting Started
1. Clone the repository from GitHub and switch to the new directory:
```shell
$ git clone https://github.com/topol-3000/cafe-telegram-bot.git
$ cd cafe-telegram-bot
```
2. Build the project
```shell
$ docker-compose build
```
3. Run the project
```shell
$ docker-compose up
```
4. Run project tests
```shell
$ docker-compose run --rm app sh -c "python manage.py test"
```
5. Run code style checking
```shell
$ docker-compose run --rm app sh -c "flake8"
