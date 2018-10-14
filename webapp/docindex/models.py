from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    is_admin = models.BooleanField()

class Project(models.Model):
    name = models.CharField(max_length=128)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=8)

class Location(models.Model):
    name = models.CharField(max_length=16)
    room_no = models.CharField(max_length=16)

class DocumentType(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=8)

class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    doc_type = models.OneToOneField(DocumentType, on_delete=models.CASCADE)
    pdf_path = models.CharField(max_length=512)
    is_pdf = models.BooleanField()
    
    class Meta:
        abstract = True

class StudyPlan(Document):
    title = models.TextField()
    STUDY_PLAN_STATUS = (
        ('PEN', 'Pending'),
        ('IND', 'In draft'),
        ('COM', 'Complete'),
    )
    status = models.CharField(max_length=3, choices=STUDY_PLAN_STATUS, default='')
    sign_date = models.DateField()
    is_filed = models.BooleanField()

class Report(Document):
    study_plan = models.ManyToManyField(StudyPlan)
    title = models.TextField()
    STUDY_PLAN_STATUS = (
        ('PEN', 'Pending'),
        ('IND', 'In draft'),
        ('COM', 'Complete'),
    )
    status = models.CharField(max_length=3, choices=STUDY_PLAN_STATUS, default='')
    sign_date = models.DateField()
    is_filed = models.BooleanField()
    
class RelatedFile(Document):
    alias = models.CharField(max_length=512)
    content_descr = models.TextField()
    vol_no = models.IntegerField()
    date_started = models.DateField()
    date_finished = models.DateField()
    date_archived = models.DateField()
    
class LabBook(Document):
    content_descr = models.TextField()
    date_issued = models.DateField()
    date_started = models.DateField()
    date_finished = models.DateField()
    index_added_pr_file = models.BooleanField()
    index_no_pages = models.IntegerField()
