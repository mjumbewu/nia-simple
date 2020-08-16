from django.contrib import admin
from nia.models import Value, Goal, Project

class ValueAdmin(admin.ModelAdmin):
    pass


class GoalAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Value, ValueAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Project, ProjectAdmin)