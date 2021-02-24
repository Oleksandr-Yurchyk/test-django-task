from django.db import models


class Menu(models.Model):
    site_name = models.CharField(max_length=20)
    home_page = models.CharField(max_length=20)
    news = models.CharField(max_length=20)
    about_us = models.CharField(max_length=20)
    contact_us = models.CharField(max_length=20)
    lang_switch = models.CharField(max_length=20)

    def __str__(self):
        return self.lang_switch
