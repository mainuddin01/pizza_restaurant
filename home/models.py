from django.db import models

# Create your models here.
class MainSlider(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main_slider')
    button_text = models.CharField(max_length=50)
    button_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Greeting(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class GreetingItem(models.Model):
    parent_section = models.ForeignKey(Greeting, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CallToAction(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='call_to_action')
    button_text = models.CharField(max_length=50)
    button_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    reviewer = models.CharField(max_length=250)
    review = models.TextField()
    image = models.ImageField(upload_to='greeting')

    def __str__(self):
        return self.title