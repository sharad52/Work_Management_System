from django.db import models
from Surface.handleslug import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class WorkDetail(models.Model):
    TYPES = (
            ('frontend', 'Frontend'),
            ('backend', 'Backend'),
            ('Database', 'Database'),
            ('FullStack', 'FullStack'),
            ('Test', 'Test'),
        ('hello', 'hello')
    )
    project = models.CharField(max_length=120)
    project_type = models.CharField(max_length=40, choices=TYPES)
    duration = models.IntegerField()
    is_complete = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.project


@receiver(pre_save, sender=WorkDetail)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
