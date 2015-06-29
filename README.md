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
python run_service.py
```
To deactivate, while in current virtualenv
```sh
deactivate
```
[github project pages setup]:https://help.github.com/articles/creating-project-pages-manually/
[raml2html]:https://www.npmjs.com/package/raml2html
[virtualenvwrapper]:http://virtualenvwrapper.readthedocs.org/en/latest/install.html
