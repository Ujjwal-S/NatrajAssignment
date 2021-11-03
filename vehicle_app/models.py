from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Vehicle(models.Model):
    """ Model representing a vehicle """
    ENGINE_STATUS = (
        ('On', "On"),
        ('Off', "Off")
    )
    name = models.CharField(max_length=50, help_text="Enter the name of a vehicle")
    speed = models.FloatField(help_text="Enter the speed of the vehicle (in kmph)")
    average_speed = models.FloatField(help_text="Enter the average speed of the vehicle (in kmph)")
    temperature = models.FloatField(help_text="Enter the temperature of the vehicle (in celcius)")
    fuel_level = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], help_text="Enter the fuel level of the vehicle (in percentage)")
    engine_status = models.CharField(max_length=3, choices=ENGINE_STATUS, help_text="Choose the engine status")
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["date_added"]
    
    def get_absolute_url(self):
        """ Returns the url to access a detail record for this instace of Vehicle. """
        return reverse('vehicle-detail', args=[str(self.id)])

    def get_delete_url(self):
        """ Returns the url to delete the record for this instace of Vehicle. """
        return reverse('vehicle-delete', args=[str(self.id)])
    
    def get_update_url(self):
        """ Returns the url to update the record for this instace of Vehicle. """
        return reverse('vehicle-update', args=[str(self.id)])

    def __str__(self):
        return self.name
