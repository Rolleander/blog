from django.db import models

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

CODE_TYPE=(
    (0,"Language"),
    (1,"Technology"),    
    (2,"Web"),    
    (3,"DB"),    
    (4,"IDE"),    
    (5,"Concept"),    
    (6,"Testing"),
    (7,"Gamedev"),    
    (8,"Other"),        
)

class CodeExp(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code_type =  models.IntegerField(choices=CODE_TYPE, default=0)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name