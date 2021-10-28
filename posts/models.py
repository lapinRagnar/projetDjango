from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_on = models.DateField(blank=True, null=True, auto_now_add=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"

    # On ajoute la méthode get_absolute_url
    def get_absolute_url(self):
        return reverse("posts:home")

    # On rajoute une classe Meta pour préciser notre modèle
    class Meta:
        # ordering = ['-created_on']
        # get_latest_by = ['created_on']
        verbose_name = "Article"



