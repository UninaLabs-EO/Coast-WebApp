# [Leanspace WebApp Flask](https://www.leanspace.io/hackathon/)

![alt text](https://www.leanspace.io/wp-content/uploads/logo-basique.svg)

## Debris Eaters Team 
### [ Roberto Del Prete, Carla Cicala, Stefano Cannavacciolo, Chiara Abbundo ]
Open-source dashboard for Leanspace hackathon to highlight Key Performance Indicator (KPI) of ClearSpace-1 space mission. 

## Core APIs provided from <a href="https://www.leanspace.io/">leanspace.io</a>. 
#### A heartfelt thanks to the technical support that followed us during the two-day hackathon.

Code base in **Flask** Framework  with Bootstrap 4 Lite for styling.
Feature-rich pages and components with fully developer-centric code. 
Deployment ready-to-use with Docker, Gunicorn / Nginx, Heroku.



> Features

- Up-to-date [dependencies](./requirements.txt): **Flask 2.0.1**
- DBMS: SQLite, PostgreSQL (production) 
- DB Tools: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- Modular design with **Blueprints**, simple codebase
- Session-Based authentication (via **flask_login**), Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx, Heroku
- Support via **Github** and [Discord](https://discord.gg/fZC6hup).

<br />



## How to use it

```bash
$ # Get the code
$ git clone https://github.com/UninaLabs-EO/LEANSPACE.git
$ cd Leanspace_app
$ 
$ # Conda Env installation (Requires Anaconda installed - for all systems):
$ conda create -n leanspace_app python=3.8
$ conda activate leanspace_app
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.


> Credits for style and layout:

- [Code base](https://docs.appseed.us/products/flask-dashboards/datta-able) - product documentation
