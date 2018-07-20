from google.appengine.ext import ndb

class DatabaseNeeds(ndb.Model):
	value = nab.StringProperty()

class DatabaseWants(ndb.Model):
	value = nab.StringProperty()

class DatabaseBought(ndb.Model):
	value = nab.StringProperty()
