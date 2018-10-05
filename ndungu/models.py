from django.db import models
from django.urls import reverse

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('province-detail', kwargs={'pk': self.id})

class Municipality(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta(object):
        verbose_name_plural = 'municipalities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('municipality-detail', kwargs={'pk': self.id})

class Authority(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta(object):
        verbose_name_plural = 'authorities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('authority-detail', kwargs={'pk':self.id})

class Entity(models.Model):
    ENTITY_CHOICES = (
        ('individual', 'Individual'),
        ('corporation', 'Corporation'),
        ('government', 'Government'),
        ('other', 'Other'),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    address = models.TextField(blank=True)
    entity_type = models.CharField(max_length=50, choices=ENTITY_CHOICES, blank=True)

    class Meta(object):
        verbose_name_plural = 'entities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('entity-detail', kwargs={'pk':self.id})

class UseCase(models.Model):
    USE_CHOICES = (
        ('intended', 'Intended'),
        ('current', 'Current'),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    use_choices = models.CharField(max_length=50, choices=USE_CHOICES)

    def __str__(self):
        return self.name

class Allocation(models.Model):
    serial_number = models.IntegerField(blank=True, null=True)
    reference_number = models.CharField(max_length=255, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, blank=True, null=True)
    intended_use = models.ForeignKey(UseCase, on_delete=models.SET_NULL, blank=True, null=True)
    current_use = models.ForeignKey(UseCase, on_delete=models.SET_NULL, blank=True, null=True, related_name='current_allocations')
    hectares = models.DecimalField(max_digits=11, decimal_places=6, blank=True, null=True)
    period = models.CharField(max_length=255, blank=True)
    original_allottee = models.ForeignKey(Entity, on_delete=models.SET_NULL, blank=True, null=True)
    original_allottee_date = models.DateField(blank=True, null=True)
    current_owner = models.ForeignKey(Entity, on_delete=models.SET_NULL, blank=True, null=True, related_name='current_allocations')
    current_owner_date = models.DateField(blank=True, null=True)
    allocating_authority = models.ForeignKey(Authority, on_delete=models.SET_NULL, blank=True, null=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return 'Allocation number %s' % self.serial_number

    def get_absolute_url(self):
        return reverse('allocation-detail', kwargs={'pk':self.id})



