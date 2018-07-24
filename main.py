import webapp2
import jinja2
import os
from google.appengine.ext import ndb

import database
import time

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# @ndb.transactional
def readfromDatabase():
    response_html = jinja_env.get_template('templates/checklist.html')
    values= {
    "wantsList": database.DatabaseEntry.query(database.DatabaseEntry.type == "want").fetch(),
    "needsList": database.DatabaseEntry.query(database.DatabaseEntry.type == "need").fetch(),
    "boughtList": database.DatabaseEntry.query(database.DatabaseEntry.type == "bought").fetch(),
    }
    return response_html.render(values)

# @ndb.transactional
def storedStuff(typeSelector, item):
    stored_items = database.DatabaseEntry(type= typeSelector, value= item)
    stored_items.put()

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
<<<<<<< HEAD
=======
    #def post(self):

# nkdvkjs
>>>>>>> 68b9331fe063859094a17495e01c9c47c9133512
class ChecklistHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(readfromDatabase())

    def post(self):
        item = self.request.get('item')
        typeSelector = self.request.get('choice')
        self.response.headers['Content-Type'] = 'text/html'
        storedStuff(typeSelector, item)
        time.sleep(0.5)
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/checklist.html')
        values= {
        "wantsList": database.DatabaseEntry.query(database.DatabaseEntry.type == "want").fetch(),
        "needsList": database.DatabaseEntry.query(database.DatabaseEntry.type == "need").fetch(),
        "boughtList": database.DatabaseEntry.query(database.DatabaseEntry.type == "bought").fetch(),
        }
        self.response.write(response_html.render(values))

class DeleteItemHandler(webapp2.RequestHandler):
    def get(self):
        item_to_delete = self.request.get('item_id')
        response_html = jinja_env.get_template("templates/remove.html")
        key = ndb.Key(urlsafe=item_to_delete)
        the_item = key.get()
        data= {
            "item_id": the_item.key.urlsafe()
        }
        self.response.write(response_html.render(data))
    def post(self):
        key = ndb.Key(urlsafe=self.request.get('item_id'))
        key.delete()

app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/login', LoginPageHandler),
    ('/search', SearchHandler),
    ('/checklist', ChecklistHandler),
    ('/delete', DeleteItemHandler),
], debug= True)
