from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=128)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=8)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('project-detail', args=[str(self.id)])

class Location(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    room_no = models.CharField(max_length=16, null=True, blank=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('location-detail', args=[str(self.id)])


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    
    DOCUMENT_CODE = (
        ('SP', 'Study plan'),
        ('R', 'Report'),
        ('RDF', 'Related file'),
        ('LBN', 'Lab book'),
    )
    document_code = models.CharField(max_length=3, choices=DOCUMENT_CODE, default='')
    e_copy = models.FileField(upload_to='uploads/', null=True, blank=True)
    class Meta:
        abstract = True

class StudyPlan(Document):
    title = models.TextField()
    STUDY_PLAN_STATUS = (
        ('PEN', 'Pending'),
        ('IND', 'In draft'),
        ('COM', 'Complete'),
    )
    status = models.CharField(max_length=3, choices=STUDY_PLAN_STATUS, default='PEN')
    sign_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('studyplan-detail', args=[str(self.id)])

class Report(Document):
    study_plan = models.ManyToManyField(StudyPlan)
    title = models.TextField()
    STUDY_PLAN_STATUS = (
        ('PEN', 'Pending'),
        ('IND', 'In draft'),
        ('COM', 'Complete'),
    )
    status = models.CharField(max_length=3, choices=STUDY_PLAN_STATUS, default='')
    sign_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('report-detail', args=[str(self.id)])
    
class RelatedFile(Document):
    alias = models.CharField(max_length=512)
    content_descr = models.TextField(null=True, blank=True)
    vol_no = models.IntegerField(null=True, blank=True)
    date_started = models.DateField(null=True, blank=True)
    date_finished = models.DateField(null=True, blank=True)
    date_archived = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.content_descr
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('relatedfile-detail', args=[str(self.id)])
    
class LabBook(Document):
    content_descr = models.TextField(null=True, blank=True)
    date_issued = models.DateField()
    date_started = models.DateField(null=True, blank=True)
    date_finished = models.DateField(null=True, blank=True)
    index_added_pr_file = models.BooleanField()
    index_no_pages = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.content_descr
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('labbook-detail', args=[str(self.id)])
 
