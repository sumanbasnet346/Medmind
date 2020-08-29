from django.db import models

# Create your models here.
class guidelist(models.Model):
    guide_sn= models.AutoField(primary_key=True)
    guide_title = models.CharField(max_length=100)
    guide_description = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to ="guidelines/images",default="")

    def __str__(self):
        return self.guide_title