from google.appengine.ext import ndb

class DatabaseNeeds(ndb.Model):
	value = ndb.StringProperty()

class DatabaseWants(ndb.Model):
	value = ndb.StringProperty()

class DatabaseBought(ndb.Model):
	value = ndb.StringProperty()

# use value and catagory after giving add buttons different key values
