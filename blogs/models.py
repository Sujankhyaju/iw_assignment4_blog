from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    content = models.TextField()
    
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):

        return self.title
        # f"{self.title[:10]}... -{self.author}"

 
