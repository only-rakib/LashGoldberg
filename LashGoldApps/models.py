from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Office_Address(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150, )
    address2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50,)
    zip_code = models.CharField(max_length=50,)
    phone = models.CharField(max_length=50, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    cover_pic = models.ImageField(
        upload_to='images/', help_text='Enter Company Office Pic')

    def get_absolute_url(self):
        return reverse("offices_inside", kwargs={'pk': str(self.id), 'office_title': self.title})

    def __str__(self):
        return self.title

class PracticeArea(models.Model):
    title=models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True ,blank=True)

    def get_absolute_url(self):
        return reverse("practices_inside", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(PracticeArea, self.title)
        else:  # create
            self.slug = generate_unique_slug(PracticeArea, self.title)
        super(PracticeArea, self).save(*args, **kwargs)


def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug

