from django.core.checks import messages
from django.db import models
from django.db.models.fields import related
from login_registration_app.models import User

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name= "user_messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #message_comments
    def __repr__(self):
        comments = ""
        if len(self.message_comments.all()) > 0:    
            for i in self.message_comments.all():
                comments += i.comment + ","
        return f"Messages: Id = {self.id}, Message = {self.message}, User = {self.user_id}, Comments = {comments}"

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name= "user_comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name = "message_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"Comments: Id = {self.id}, comment = {self.comment}, User Id = {self.user_id}, Message Id = {self.message_id}"