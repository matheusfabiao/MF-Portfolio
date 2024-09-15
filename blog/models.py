from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True, editable=False)
    content = models.TextField(null=False, blank=False, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = create_slug(self.title)
        super(self, Post).save(*args, **kwargs)

    def __str__(self):
        if len(str(self.title)) > 50:
            return self.title[:50] + ' ...'
        else:
            return self.title
        
        
def create_slug(title):
    slug = slugify(title)
    
    return f'{slug}'