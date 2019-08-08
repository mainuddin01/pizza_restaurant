from django.db import models
from django.utils.text import slugify

# Create your models here.
SIZE_CHOICES = (
    ('sm', 'Small'),
    ('md', 'Medium'),
    ('lg', 'Large'),
    ('ps', 'Party Size')
)

def upload_path(instance, filename):
    name = slugify(instance.name)
    basename, extension = filename.split('.')
    new_filename = "{}-{}.{}".format(name, instance.id, extension)
    return new_filename

class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='md')
    image = models.ImageField(upload_to=upload_path)
    categories = models.ForeignKey('Category', related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Dishes'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Dish, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name