from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Colors available for guest. I picked THESE, because Materialize can add them as a nice background color.
COLORS = (
    ('red', 'Red'),
    ('pink', 'Pink'),
    ('purple', 'Purple'),
    ('deep-purple', 'Deep-Purple'),
    ('indigo', 'Indigo'),
    ('blue', 'Blue'),
    ('light-blue', 'Light Blue'),
    ('cyan', 'Cyan'),
    ('teal', 'Teal'),
    ('green', 'Green'),
    ('light-green', 'Light-Green'),
    ('lime', 'Lime'),
    ('yellow', 'Yellow'),
    ('amber', 'Amber'),
    ('orange', 'Orange'),
    ('deep-orange', 'Deep Orange'),
    ('brown', 'Brown'),
    ('grey', 'Grey'),
    ('blue-grey', 'Blue Grey'),
    ('black', 'Black'),
    ('white', 'White')
)

# Picture (Art) model
class Picture(models.Model):
    name = models.CharField('Title', max_length=200)
    link = models.CharField('Link', max_length=500)
    description = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse('picture_detail', kwargs={'pk': self.id})


# Note model
class Note(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    number = models.IntegerField()
    pictures = models.ManyToManyField(Picture)

# This method allowes us to see a readable format of Objects instead of 'Object<>'
    def __str__(self):
        return self.name

# Person (Guest) model
class Person(models.Model):
    name = models.CharField('Name', max_length=200)
    color = models.CharField(
        'Color',
        max_length=11,
        choices=COLORS,
        default=COLORS[0][0]
    )
    # create a note foreign key
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_color_display()} for {self.name}'