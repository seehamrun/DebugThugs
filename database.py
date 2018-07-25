from google.appengine.ext import ndb

class DatabaseEntry(ndb.Model):
	value = ndb.StringProperty()
	type = ndb.StringProperty()
	username = ndb.StringProperty()
