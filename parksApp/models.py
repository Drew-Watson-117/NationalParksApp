from django.db import models

class Park(models.Model):
    name=models.CharField(max_length=300)
    description = models.TextField()
    directionsInfo = models.TextField()
    directionsURL = models.URLField()
    image = models.URLField()
    link_to_website = models.URLField()
    marked = models.BooleanField()
    visited = models.BooleanField()
    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    park=models.ForeignKey(Park, on_delete=models.CASCADE)
    visitation_date=models.DateField('date visited')
    content = models.TextField()