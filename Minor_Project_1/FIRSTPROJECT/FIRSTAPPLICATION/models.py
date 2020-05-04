from django.db import models

# Create your models here.
class Candidate(models.Model):
    CandidateFullName = models.CharField(max_length=20)
    CandidateID = models.CharField(max_length=20)
    CandidateContact = models.CharField(max_length=20)
    CandidateAddress = models.CharField(max_length=20)