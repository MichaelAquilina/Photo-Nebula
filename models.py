from google.appengine.ext import ndb


class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    nickname = ndb.StringProperty()
    email = ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)


class Photo(ndb.Model):
    name = ndb.StringProperty()
    blob_info_key = ndb.BlobKeyProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)


class Album(ndb.Model):
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)


class Comment(ndb.Model):
    author = ndb.StringProperty()
    text = ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)
