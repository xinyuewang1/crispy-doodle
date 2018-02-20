# flask_platform

Shining new flask_platform, can check platform and print on a webpage.

install
	
	pip install git+https://github.com/xinyuewang1/crispy-doodle

## Quick Start

Run the application:

    python path/to/flask_platform/run.py

or type in terminal

	flask_platform


## Prerequisites

It's using sysinfo, make sure install systeminfo_cookiecutter first.

	pip install git+https://github.com/xinyuewang1/super-duper-potato

This is built to be used with Python 3. Update `Makefile` to switch to Python 2 if needed.

Some Flask dependencies are compiled during installation, so `gcc` and Python header files need to be present.
For example, on Ubuntu:

    apt install build-essential python3-dev


## Development environment and release process

 - create virtualenv with Flask and flask_platform installed into it (latter is installed in
   [develop mode](http://setuptools.readthedocs.io/en/latest/setuptools.html#development-mode) which allows
   modifying source code directly without a need to re-install the app): `make venv`

 - run development server in debug mode: `make run`; Flask will restart if source code is modified

 - run tests: `make test` (see also: [Testing Flask Applications](http://flask.pocoo.org/docs/0.12/testing/))

 - create source distribution: `make sdist` (will run tests first)

 - to remove virtualenv and built distributions: `make clean`

 - to add more python dependencies: add to `install_requires` in `setup.py`

 - to modify configuration in development environment: edit file `settings.cfg`; this is a local configuration file
   and it is *ignored* by Git - make sure to put a proper configuration file to a production environment when
   deploying


## Deployment

If you are interested in an out-of-the-box deployment automation, check out accompanying
[`cookiecutter-flask-ansible`](https://github.com/candidtim/cookiecutter-flask-ansible).

Or, check out [Deploying with Fabric](http://flask.pocoo.org/docs/0.12/patterns/fabric/#fabric-deployment) on one of the
possible ways to automate the deployment.

In either case, generally the idea is to build a package (`make sdist`), deliver it to a server (`scp ...`),
install it (`pip install flask_platform.tar.gz`), ensure that configuration file exists and
`FLASK_PLATFORM_SETTINGS` environment variable points to it, ensure that user has access to the
working directory to create and write log files in it, and finally run a
[WSGI container](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/) with the application.
And, most likely, it will also run behind a
[reverse proxy](http://flask.pocoo.org/docs/0.12/deploying/wsgi-standalone/#proxy-setups).
