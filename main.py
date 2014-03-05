import bottle
import jinja2

ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
APP = bottle.Bottle()

@APP.route('/')
def home():
  return ENV.get_template('index.html').render()

@APP.route('/about')
def home():
  return ENV.get_template('about.html').render()

@APP.error(404)
def error404():
  return ENV.get_template('error404.html').render()

