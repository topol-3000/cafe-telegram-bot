# Cafe Telegram Bot

## Getting Started

First clone the repository from GitHub and switch to the new directory:

    $ git clone https://github.com/topol-3000/cafe-telegram-bot.git
    $ cd cafe-telegram-bot
    
Activate the virtualenv for the project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
