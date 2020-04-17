from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Artefact(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100, verbose_name="Title of artefact")  
    description = models.TextField()
    artist = models.CharField(max_length=100, db_index=True)
    publish_date = models.DateTimeField(auto_now_add=True, )
    favourite = models.ManyToManyField(User, related_name='favourites', blank=True )
    dimensions = models.CharField(max_length=100, null=True, default=None, blank=True)
    accession_number = models.CharField(max_length=100, null=True, default=None, blank=True)
    credit_line = models.CharField(max_length=100, default=None, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('artefact_detail', args=[self.id])

    class Meta:
        ordering = ('-publish_date',)


    def __str__(self):
        return f"Artefact :{self.title}"


class Comment(models.Model):
    artefact  = models.ForeignKey(Artefact, related_name='comments', on_delete=models.CASCADE)
    name  = models.CharField(max_length=80)
    email = models.EmailField()
    body  = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)        
     