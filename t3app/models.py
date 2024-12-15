from django.db import models

class course(models.Model):
    CAT=((1,'spritual'),(2,'Historical'),(3,'adventure'))
    loc=((1,'Rajasthan'),(2,'Delhi'),(3,'Gujrat'),(4,'Maharastra'))
    name=models.CharField(max_length=100 ,verbose_name='place Name')
    cat=models.IntegerField(verbose_name='Category' ,choices=CAT)
    lc=models.IntegerField(verbose_name='locations' ,choices=loc)
    cdetail=models.CharField(max_length=300, verbose_name='place Detail')
    cimage=models.ImageField(upload_to='image')
    is_active=models.BooleanField(default=True)
