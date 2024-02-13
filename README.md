# QuickFlask
This is my Flask quick start template.
Its based on https://github.com/bittobennichan/flask-quickstart/ but updated to Flask version 2.3.3.

It is a minimal boilerplate/template for starting your new Flask project.

## How to install

NOTE: This repo is not yet ready for Flask v 3.0 . Working on it, will update when ready!

First clone the repository

```
$ git clone https://github.com/DamianK/quickflask.git
```
Change directory to quickflask

```
$ cd quickflask
```
Create a virtual environment and install dependencies
```
$ mkvirtualenv quickflask
$ workon quickflask
$ pip install -r requirements.txt
```

Start the development server
```
$ flask run
```
That's it! 

Navigate to `http://127.0.0.1:5000/` and start your new project!

## Project layout
```
quickflask/
├── app/
│   ├── __init__.py
│   ├── main/
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   └── views.py
│   ├── models/
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   └── templates/
│       ├── common/
│       ├── error/
│       │   ├── 404.html
│       │   └── 500.html
│       └── main/
│           └── index.html
├── CHANGES
├── config.py
├── instance/
│   └── config.py
├── LICENSE
├── manage.py
├── README.md
├── requirements.txt
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── wsgi.py
```

When you clone the repo, you'll notice that you will be missing the *config.py* file in instance folder. You will find an *example_config.py* file instead.

```
├── instance/
    └── example_config.py
```

This is b'coz it should be set to be ignored in the *.gitignore* file. Infact everything except *example_config.py* is set to be ignored. This is where you will store the deployment/production configuration values. You don't want to accidently push this to Github. Rename the file to *config.py* after you clone the repo.


If available, the values in `quickflask/instance/config.py` will override any config values set in tthe environment form `quickflask/config.py` when environment is set to `production` (it is set to `development` by default).

The **wsgi.py** file uses `production` as the environment. This file is to be used by WSGI servers such as Gunicorn.

You can also test production environment using `manage.py`

```
$ python manage.py runserver --env production
```

You'll find that there are `.gitkeep` files in some folders. Git does not track empty folders. This is a convention used to preserve the folder structure. These files are not necessary and you can delete them if you want.

## manage.py

As mentioned earlier, **manage.py** has just one command **runserver** which is used to run the Flask development server.

It takes two optional parameters

- `env` - Environment to use while running server. Supports  `production`, `development` and `testing` out of the box. Default is `development`. 

- `port` - Port to use while running server. Default is 5000.

Eg.

```
$ python manage.py runserver --env production --port 5566
``` 

Runs the  server in `production` environment on port 5566.

You can  extend `manage.py` to support additional commands, parameters etc.

## Developing your application

*quickflask* is built in such a way that you can easily integrate extensions, blueprints, tests etc. The files are commented to help you out with this.

## Contact me

If you have any comments, suggestions or ideas to improve this, please contact me!
