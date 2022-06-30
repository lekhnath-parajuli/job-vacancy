from django.db import models


class Job(models.Model):
    job_title = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.pk


class Skill(models.Model):
    job_id = models.ForeignKey(
        Job, related_name='req_skills', on_delete=models.CASCADE)
    skill_name = models.TextField(max_length=30)

    def __str__(self) -> str:
        return self.pk


class Applicant(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)

    def __str__(self) -> str:
        return self.pk


class ApplicantSkill(models.Model):
    candidate_id = models.ForeignKey(
        Applicant, related_name='applicant_skills', on_delete=models.CASCADE)
    skill_name = models.TextField(max_length=30)

    def __str__(self) -> str:
        return self.pk
