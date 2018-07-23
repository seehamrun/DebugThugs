import webapp2
import jinja2
import os
from google.appengine.ext import ndb

import database


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/index.html')
        self.response.write(response_html.render())

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/login.html')
        self.response.write(response_html.render())
    #def post(self):

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/search.html')
        self.response.write(response_html.render())
    #def post(self):

class ChecklistHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/checklist.html')
        values= {
        "wants": database.DatabaseWants.query().fetch(),
        "needs": database.DatabaseNeeds.query().fetch(),
        "bought": database.DatabaseBought.query().fetch()
        }
        self.response.write(response_html.render(values))


app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/login', LoginPageHandler),
    ('/search', SearchHandler),
    ('/checklist', ChecklistHandler)
], debug=True)
