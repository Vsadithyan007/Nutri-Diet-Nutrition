from django.db import models
# Create your models here.

GEN_CATEGORY=(
    ('Male','Male'),
    ('Female','Female')
)

CATEGORY=(
    ('Extremely Inactive','Extremely Inactive'),
    ('Inactive','Inactive'),
    ('Moderately Active','Moderately Active'),
    ('Active','Active'),
    ('Extremely Active','Extremely Active')
)

class Nutri(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=100,choices=GEN_CATEGORY)
    Height = models.FloatField()
    Weight = models.FloatField()
    LifeStyle = models.CharField(max_length=200,choices=CATEGORY)

    class Meta:
        verbose_name_plural='Nutri'

    def __str__(self):
        return f'{self.Name}-{self.Age}'