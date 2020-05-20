from django.db import models

# Create your models here.
class classfications(models.Model):
    classfication = models.CharField(max_length=1000,null=True)
    class Meta:
        verbose_name_plural = '单词分类'

class words(models.Model):
    word = models.CharField(max_length=30)
    sound = models.CharField(max_length=100)
    plain = models.CharField(max_length=100)
    # construct = models.CharField(max_length=200)
    example = models.CharField(max_length=1000,null=True)
    
    classfication = models.ForeignKey(classfications,on_delete=models.CASCADE,null=True)

    class Meta:
        verbose_name_plural = '所有单词'
