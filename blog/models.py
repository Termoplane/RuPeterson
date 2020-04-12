from django.db import models

class Entry(models.Model):
    entry_header = models.CharField(max_length=200)
    entry_text = models.TextField(blank=True, default=None)
    entry_rating = models.IntegerField(default=0)
    entry_image = models.ImageField(upload_to="gallery", blank=True, default=None)
    entry_video = models.URLField(blank=True, default=None)
    pub_date = models.DateTimeField('date published')
    #video_link = models.
    
    def __str__(self):
        return self.entry_header

class Comment(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Entry, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField()

    def __str__(self):
        return self.comment_date

#class User(models.Model):
#    username = models.CharField(max_length=30)
#    user_email = models.EmailField()
#
#    def __str__(self):
#        return self.username