from django.db import models

from django.shortcuts import reverse

# Create your models here.
class Blog(models.Model):
    Name = models.CharField(max_length=100)
    Background_Image = models.ImageField()

    Subheading1 = models.CharField(max_length=100,blank=True,null=True)
    Image1 = models.ImageField(blank=True,null=True)
    Paragraph1 = models.TextField(blank=True,null=True)

    Subheading2 = models.CharField(max_length=100, blank=True, null=True)
    Image2 = models.ImageField(blank=True, null=True)
    Paragraph2 = models.TextField(blank=True,null=True)

    Subheading3 = models.CharField(max_length=100, blank=True, null=True)
    Image3 = models.ImageField(blank=True, null=True)
    Paragraph3 = models.TextField(blank=True,null=True)

    Date = models.DateField(auto_now_add=True,blank=True,null=True)

    Video = models.FileField(blank=True,null=True,upload_to="Videos")

    slug = models.SlugField(blank=True,null=True,unique=True)

    coments = models.ManyToManyField("Comments",blank=True)
    def get_abs_url(self):
        return reverse(viewname="Blogs:BlogView",
                       kwargs={'slug':self.slug}

                       )

class Comments(models.Model):
    Name = models.CharField(blank=True,null=True,max_length=50)
    Comment = models.TextField()
    Date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

class Contacts(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    subject = models.TextField(max_length=50)