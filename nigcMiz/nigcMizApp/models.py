from django.db import models


class MizReqS(models.Model):
     ReqDate = models.DateTimeField(auto_now_add=True)
     Reqslug= models.SlugField(max_length=20,allow_unicode=True)
     ReqTitle= models.TextField()
     ReqDesc=models.TextField()
     ReqAdd = models.TextField()
     def __str__(self):
         return self.ReqTitle


     def snippet(self):
         return self.ReqDesc[0:3]+'...'
