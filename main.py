import bottle
import jinja2
from google.appengine.api import users

ENV = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
APP = bottle.Bottle()

@APP.route('/')
def home():
  return ENV.get_template('index.html').render()

