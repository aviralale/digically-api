from django.db import models


class TeamMember(models.Model):
    full_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="team_members/")

    def __str__(self):
        return self.full_name
