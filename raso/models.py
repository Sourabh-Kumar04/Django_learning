from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class RasoVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='rasos/')
    date_addes = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# One to Many
class RasoReview(models.Model) :
    raso = models.ForeignKey(RasoVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str_(self):
        return f'{self.user.username} review for {self.raso.name}'

# Many to many

class Store(models.Model) :
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    raso_varity = models.ManyToManyField(RasoVarity, related_name='stores')

    def __str__(self):
        return self.name


# One to One

class RasoCertificate(models.Model):
    raso = models.OneToOneField(RasoVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate  for {self.raso.name}'






