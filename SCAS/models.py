from django.db import models

# Create your models here.
class Supports(models.Model):
    support_sn = models.AutoField(primary_key=True)
    support_title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="SCAS/images",default="")
    
    def __str__(self):
        return self.support_title