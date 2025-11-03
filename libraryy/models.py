from django.db import models

# Create your models here.



class LibraryModel(models.Model):

    category_choices = [('horror', 'horror'),
                        ('action','action'),
                        ('romance', 'romance')
                        ]
    
    category = models.CharField(max_length=30,choices= category_choices)

    
    title = models.CharField(max_length=30)

    author = models.CharField(max_length=40)

    

    
