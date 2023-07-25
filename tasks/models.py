from django.db import models


# Create your models here.


class Task(models.Model):
    STATUS= (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    title= models.CharField(max_length=255)
    description= models.TextField()
    done= models.CharField(max_length=5,choices=STATUS) # se tá pronta ou não
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to= "static/img", null=True, blank=True)
    
    def __str__(self):
        return self.title


