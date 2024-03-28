from django.db import models

class TeamMember(models.Model): 
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, unique = True)
    Phone = models.CharField(max_length=50, unique = True)
    Admin = models.BooleanField()
    def getAdmin(self):
        return "(admin)" if self.Admin else ""
        

