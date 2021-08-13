from django.db import models
import string
import random

class Todo(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

class FloatArrayField(models.TextField):
    separator = ","

    def from_db_value(self, value, expression, connection):
        if not value:
            return value
        return [float(v) for v in value.split(self.separator)]

    def to_python(self, value):
        if isinstance(value, list):
            return value

        return self.from_db_value(value, None, None)

    def get_prep_value(self, value):
        return self.separator.join(map(str, value))

class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code ,unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    path = models.CharField(max_length=1024, default='')
    frame = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

class Shape(models.Model):
    type = models.CharField(max_length=16)
    occluded = models.BooleanField(default=False)
    z_order = models.IntegerField(default=0)
    points = FloatArrayField()