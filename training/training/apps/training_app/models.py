from __future__ import unicode_literals

from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
import ipcalc


# Create your models here.


class City(models.Model):
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = USZipCodeField(blank=True, db_index=True)

    @property
    def city_state_zip(self):
        return self.city + " " + self.state + ", " + self.zip_code

    class Meta:
        verbose_name_plural = "Cities"

    def __unicode__(self):
        return self.city_state_zip


network_help_txt = 'Insert one ip address or a network mask (i.e. 10.1.1.0/24) to include a whole network.'


class TrustedIP(models.Model):
    title = models.CharField('Title', max_length=100)
    network = models.CharField('IP network', max_length=18, help_text=network_help_txt)

    def __unicode__(self):
        return self.title

    def get_network(self):
        return ipcalc.Network(self.network)

    class Meta:
        verbose_name = 'IP mask to include'
        verbose_name_plural = 'IP masks to include'


