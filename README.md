# Fibonacci api

API signature was written in raml and the html conversion with current signatures is maintained on the [project page]

### Prerequisites
The api requires python 3.4,  pip and [virtualenvwrapper] installed as parts of its site packages. 

### Installation and virtualenv
To clone the application and create the virtualenv. 
```sh
cd /path/to/workspace
git clone https://github.com/draganaperez/fibonacci.git
mkvirtualenv -p `which python3.4` -a ~/dev-flask/fibonacci fib-dev
cdproject  

# Install in editable mode
pip install -e . # note the dot
```
To activate your virtual env and start the service in debug mode (on port 3300 with logs in debug mode):
```sh
workon fib-dev 
cdproject
fibonacci_api
```
To deactivate, while in current virtualenv
```sh
deactivate
```
# Running unittests
```sh
python setup.py test
```

# Using the api
Api allows integers between 0 and 1000
```sh 
curl http://localhost:5000/fibonacci/5
"[0, 1, 1, 2, 3]"
```
[virtualenvwrapper]:http://virtualenvwrapper.readthedocs.org/en/latest/install.html
