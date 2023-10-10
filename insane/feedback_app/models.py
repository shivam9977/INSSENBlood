from django.db import models

class Feedback(models.Model):
    fullname = models.CharField(max_length=50,default="Please Enter Your Full Name")
    subject = models.CharField(max_length=255,default="Please Enter The Subject")
    message = models.TextField(default="Please Enter Your Feedback")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
