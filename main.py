import webapp2
import jinja2
from google.appengine.api import users
import os
import webbrowser

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import api
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
        user = users.get_current_user()
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/index.html')
        self.response.write(response_html.render())

# class LoginPageHandler(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         self.response.headers['Content-Type'] = 'text/html'
#         response_html = jinja_env.get_template('templates/login.html')
#         self.response.write(response_html.render())
#     #def post(self):

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        itemID = self.request.get("item_id")
        self.response.headers['Content-Type'] = 'text/html'
        response_html = jinja_env.get_template('templates/search.html')
        values = {
        "item_id": itemID,
        "googleApi" : api.googleApi,
        }
        self.response.write(response_html.render(values))
    def post(self):
        item = self.request.get('newItem')
        typeSelector = self.request.get('choiceSearch')
        self.response.headers['Content-Type'] = 'text/html'
        print("hello")
        storedStuff(typeSelector, item)
        time.sleep(0.5)
        response_html = jinja_env.get_template('templates/checklist.html')
        values= {
        "wantsList": database.DatabaseEntry.query(database.DatabaseEntry.type == "want").fetch(),
        "needList": database.DatabaseEntry.query(database.DatabaseEntry.type == "need").fetch(),
        "boughtList": database.DatabaseEntry.query(database.DatabaseEntry.type == "bought").fetch(),
        }
        self.response.write(response_html.render(values))
        self.response.write(readfromDatabase())

class ChecklistHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
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
        user = users.get_current_user()
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
        self.redirect("/checklist")
        item = self.request.get('item')
        typeSelector = self.request.get('choice')

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



app = webapp2.WSGIApplication([
    ('/', WelcomeHandler),
    ('/search', SearchHandler),
    ('/checklist', ChecklistHandler),
    ('/delete', DeleteItemHandler),
], debug= True)
