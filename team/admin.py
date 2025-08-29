from .models import TeamMember
from django.contrib import admin


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "designation")


admin.site.register(TeamMember, TeamMemberAdmin)
