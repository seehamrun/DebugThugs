from google.appengine.ext import ndb

class DatabaseNeeds(ndb.Model):
	value = ndb.StringProperty()

class DatabaseWants(ndb.Model):
	value = ndb.StringProperty()

class DatabaseBought(ndb.Model):
	value = ndb.StringProperty()
