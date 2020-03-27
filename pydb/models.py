from django.db import models

# Create your models here.

class Meta:
    db_table = 'pydb'

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=120, verbose_name='Название стиля')

    def __unicode__(self):
        return self.style_name

    def __str__(self):
        return self.style_name


class Crew(models.Model):
    id = models.AutoField(primary_key=True)
    crew_name = models.CharField(max_length=120, verbose_name='Название команды')

    def __unicode__(self):
        return self.crew_name

    def __str__(self):
        return self.crew_name


class Dancer(models.Model):
    id = models.AutoField(primary_key=True)
    crew_id = models.ForeignKey('Crew', null=True, blank=True)
    style_id = models.ForeignKey('Style', null=True, blank=True)
    dancer_name = models.CharField(max_length=120, verbose_name='Имя танцора')

    def __unicode__(self):
        return self.dancer_name

    def __str__(self):
        return self.dancer_name
