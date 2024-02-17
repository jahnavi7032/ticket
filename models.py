from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[('Technical', 'Technical'), ('Billing', 'Billing'), ('Service', 'Service')])
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='Open')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.name} - {self.description}"
