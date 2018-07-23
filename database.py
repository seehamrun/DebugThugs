from google.appengine.ext import ndb

class DatabaseNeeds(ndb.Model):
	value = ndb.StringProperty()

class DatabaseWants(ndb.Model):
	value = ndb.StringProperty()

class DatabaseBought(ndb.Model):
	value = ndb.StringProperty()

# use value and catagory after giving add buttons different key values
# >>>>>>> a49925f9b6e3d54b05b46ba375e8b5d336c2acf9
