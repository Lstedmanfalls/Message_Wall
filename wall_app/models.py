from django.db import models

class Wall(models.Model):
    label = models.CharField(max_length=255)
    label = models.TextField()
    label = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #wall_messages
    def __repr__(self):
        return f"Object_Name: {self.id}, {self.label}"

class Message(models.Model):
    label = models.CharField(max_length=255)
    label = models.TextField()
    label = models.IntegerField()
    many_to_many_label = models.ManyToManyField(Wall, related_name = "wall_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #message_comments
    def __repr__(self):
        variable_name = ""
        if len(self.many_to_many_label.all()) == 0:
            variable_name = "This objects has no many_to_many_labels"
        else:
            for i in self.many_to_many_label.all():
                variable_name += i.object_label + ","
        return f"Object_Name: id = {self.id}, Label = {self.label}, Label = {variable_name}"

class Comment(models.Model):
    label = models.CharField(max_length=255)
    label = models.TextField()
    label = models.IntegerField()
    one_to_many_label = models.ForeignKey(Message, related_name= "message_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        variable_name = ""
        if len(self.one_to_many_label.all()) == 0:
            variable_name = "This objects has no one_to_many_labels"
        else:
            for i in self.one_to_many_label.all():
                variable_name += i.object_label + ","
        return f"Object_Name: id = {self.id}, Label = {self.label}, Label = {variable_name}"