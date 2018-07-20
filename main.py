import webapp2
import jinja2
import os
from google.appengine.ext import ndb


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):

class ViewItemHandler(webapp2.RequestHandler):
    def get(self):

class ChecklistHandler(webapp2.RequestHandler):
    def get(self):



app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/login', LoginPageHandler),
    ('/view_item', ViewItemHandler),
    ('/checklist', ChecklistHandler)
], debug=True)
