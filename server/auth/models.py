from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    avatar = models.ImageField(blank=True, null=True, verbose_name=_('Imágen de perfil'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, verbose_name=_('Biografía'))
    location = models.CharField(max_length=30, blank=True, verbose_name=_('Dirección'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Fecha de nacimiento'))

    def __str__(self):
        return self.get_fullname()

    def get_fullname(self):
        """
        Method to get the fullname of user
        """
        if self.user.last_name and self.user.first_name:
            fullname = '%s %s' % (self.user.first_name, self.user.last_name)
        else:
            fullname = self.user.username
        return fullname
    

    class Meta:
        ordering = ['-id']
        verbose_name = _('Perfil de Usuario')
        verbose_name_plural = _('Perfiles de Usuarios')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()