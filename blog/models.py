from django.db import models
from django.utils.text import slugify

from uuid import uuid4

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)

    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return self.full_name()
    

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"
    
def image_upload_path(instance, filename):
        ext = filename.split('.')[-1]
        # app_label = instance._meta.app_label
        return f"blog/post/{uuid4().hex}.{ext}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    excerpt = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=image_upload_path)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    def save(self, *args, **kwargs):
    # Check if the object is new or title changed
        if not self.slug or self._title_changed():
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def _title_changed(self):
        if not self.pk:
            return True  # New object, title "changed" by default
        old_title = Post.objects.get(pk=self.pk).title
        return old_title != self.title

    class Meta:
        ordering = ['-created_at'] # latest posts first

