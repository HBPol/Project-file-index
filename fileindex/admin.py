from django.contrib import admin

# Register your models here.
from fileindex.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook

# admin.site.register(Project)
admin.site.register(Location)
# admin.site.register(StudyPlan)
# admin.site.register(Report)
admin.site.register(RelatedFile)
admin.site.register(LabBook)

# Define the admin class
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'sign_date', 'e_copy', 'owner', 'project', 'location')
    # 'fields' attribute list those fields that are to be displayed in the details forms, in order
    fields = ['owner', 'title', 'status', ('e_copy', 'sign_date', 'project'), 'location']

# Register the admin class with the associated model
admin.site.register(StudyPlan, StudyPlanAdmin)

# Same for Report class
class ReportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Report, ReportAdmin)

# Same for Project, this time using the @ decorator
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass