from django.db import models

# Create your models here.


class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact_num = models.CharField(max_length=50)

    # category = forms.ChoiceField(choices=[('question', 'Questions'), ('other', 'Other')])
    # subject = forms.CharField(required=False)

    # Vehicle details
    vehicle_year_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_num = models.CharField(max_length=50, primary_key=True)

    # Loss details
    # YEARS = models.IntegerField(choices=yearChoices(), default=2021)
    # YEARS = [x for x in range(2010, 2022)]
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=50)

    description = models.CharField(max_length=500)
    report = models.CharField(choices=(('no', 'No'), ('yes', 'Yes')), max_length=10)
    injury = models.CharField(choices=(('no', 'No'), ('yes', 'Yes')), max_length=10)
    # Document required
    photo = models.ImageField(upload_to='UserPics/')
    document = models.FileField(upload_to='UserDocs/')

    def __str__(self):
        return self.name




