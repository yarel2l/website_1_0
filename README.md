# Locomotion USA website Ver-1.0
An fantastic project starter template for Django 1.9.

##INFO:
    THIS PROJECT HELP ME TO LEARN ABOUT DJANGO.
    PLEASE COMMENT YOUR CODE AND THANKS!!

## IMPORTANT TO ME!!
All changes in apps, please write inside readme file in their respective section.

## App list:

### Blog
Include simple models as Page and Category

- Changes:
        Put it here. Use format: [# info about it]

### Configuration
Set initial settings for homepage:
    - Header Video
    - Sections (Header menu navigation, Services, Portfolio, Promotional, Team, Contacts, Map, Footer)

####  Models:
        1. Website
        2. SocialNetworks

- Changes:
        Put it here. Use format: [# info about it]

### Portfolio
Include a list of projects.

####  Models:
        1. Project
        2. Promo

- Changes:
        Put it here. Use format: [# info about it]

### Services
Include a  basic info about company services

####  Models:
        1. Service

- Changes:
        Put it here. Use format: [# info about it]

### Team
Show simple stuff list in homepage. Team member could be join to one Team

####  Models:
        1. Team
        2. Profile

- Note:
    Profile had a relation 121 with Django User only

- Changes:
        Put it here. Use format: [# info about it]

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Python 2.7 runtime environment.

## How to collaborate

1. Be worker!!
2. Be honest!!
3. Mail me!!!!!

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "My Company website. Version 1.0"

    $ heroku create my-company-website
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
- [Pillow] (https://warehouse.python.org/project/pillow/)
