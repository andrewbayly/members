from django.db import models

class TeamMember(models.Model): 
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, unique = True)
    Phone = models.CharField(max_length=50, unique = True)
    Role = models.IntegerField(default=1)
    def getAdmin(self):
        return "(admin)" if self.Role == 2 else ""
        

