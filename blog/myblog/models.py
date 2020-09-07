from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateField(default=timezone.now)
    def __str__(self):
        return("the name of the post is{} and the author is {} then the content is{} on the time{}".format(self.name,self.author,self.content,self.date_time))

