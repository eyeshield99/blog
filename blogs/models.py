from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to="blog_images/",
        null=True,
        blank=True,
    )
    pub_date = models.DateField(
        "Publication Date",
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", args=[str(self.slug)])

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ("-pub_date",)


@receiver(pre_save, sender=Blog)
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
