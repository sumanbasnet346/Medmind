from django.db import models

# Create your models here.
class training(models.Model):
    training_sno = models.AutoField(primary_key=True)
    training_title = models.CharField(max_length=50)
    training_description = models.TextField()
    date = models.DateField
    image = models.ImageField(upload_to ="trainings/images",default="")

    def __str__(self):
        return self.training_title