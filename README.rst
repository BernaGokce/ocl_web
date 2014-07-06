ocl_web
=======

Web client interface for Open Concept Lab terminology services API.

LICENSE: BSD

Developer Installation
-----------------------

1. Clone this repository::

    git clone https://github.com/OpenConceptLab/ocl_web/

2. Set up a virtualenv and virtualenvwrapper::
    If you aren't familiar with virtualenvs, go here:  TODO:
    Link to virtualenv setup from Hitchiker's Guide to Python.
    You don't *have* to use virtualenvwrapper, but this document
    assumes that you do.

    mkproject ocl_web

3. Install all the supporting libraries into your virtualenv::

    pip install -r requirements/local.txt

4. Install Grunt Dependencies::

    npm install

If you don't have node.js and grunt-cli installed, go here:  TODO

6. Create a database::

    OS X
    If you don't already have Postgres.app, you should use that:  TODO:  What's that URL?

    createdb ocl_web

7. Create database tables::

    python ocl_web/manage.py syncdb --migrate

7. Run development server. (For browser auto-reload, use Livereload_ plugins.)

    grunt serve

.. _livereload: https://github.com/gruntjs/grunt-contrib-watch#using-live-reload-with-the-browser-extension


Settings
------------
For configuration purposes, the following table maps the cookiecutter-django environment variables to their Django setting:

======================================= =========================== ============================================== ===========================================
Environment Variable                    Django Setting              Development Default                            Production Default
======================================= =========================== ============================================== ===========================================
DJANGO_AWS_ACCESS_KEY_ID                AWS_ACCESS_KEY_ID           n/a                                            raises error
DJANGO_AWS_SECRET_ACCESS_KEY            AWS_SECRET_ACCESS_KEY       n/a                                            raises error
DJANGO_AWS_STORAGE_BUCKET_NAME          AWS_STORAGE_BUCKET_NAME     n/a                                            raises error
DJANGO_CACHES                           CACHES                      locmem                                         memcached
DJANGO_DATABASES                        DATABASES                   See code                                       See code
DJANGO_DEBUG                            DEBUG                       True                                           False
DJANGO_EMAIL_BACKEND                    EMAIL_BACKEND               django.core.mail.backends.console.EmailBackend django.core.mail.backends.smtp.EmailBackend
DJANGO_SECRET_KEY                       SECRET_KEY                  CHANGEME!!!                                    raises error
DJANGO_SECURE_BROWSER_XSS_FILTER        SECURE_BROWSER_XSS_FILTER   n/a                                            True
DJANGO_SECURE_SSL_REDIRECT              SECURE_SSL_REDIRECT         n/a                                            True
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF      SECURE_CONTENT_TYPE_NOSNIFF n/a                                            True
DJANGO_SECURE_FRAME_DENY                SECURE_FRAME_DENY           n/a                                            True
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS   HSTS_INCLUDE_SUBDOMAINS     n/a                                            True
DJANGO_SESSION_COOKIE_HTTPONLY          SESSION_COOKIE_HTTPONLY     n/a                                            True
DJANGO_SESSION_COOKIE_SECURE            SESSION_COOKIE_SECURE       n/a                                            False
======================================= =========================== ============================================== ===========================================

* TODO: Add vendor-added settings in another table


Deployment
------------

Run these commands to deploy the project to Heroku:

.. code-block:: bash

    heroku create --buildpack https://github.com/heroku/heroku-buildpack-python
    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups
    heroku addons:add sendgrid:starter
    heroku addons:add memcachier:dev
    heroku pg:promote HEROKU_POSTGRESQL_COLOR
    heroku config:set DJANGO_CONFIGURATION=Production
    heroku config:set DJANGO_SECRET_KEY=RANDOM_SECRET_KEY
    heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_ID
    heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_KEY
    heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=BUCKET
    git push heroku master
    heroku run python ocl_web/manage.py syncdb --noinput --settings=config.settings
    heroku run python ocl_web/manage.py migrate --settings=config.settings
    heroku run python ocl_web/manage.py collectstatic --settings=config.settings
