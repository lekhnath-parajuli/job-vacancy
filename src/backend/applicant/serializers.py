from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . import models


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ['job_id', 'skill_name']


class JobSerializer(serializers.ModelSerializer):
    req_skills = SkillSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Job
        fields = ['job_title', 'req_skills']


class ApplicantSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApplicantSkill
        fields = ['candidate_id', 'skill_name']


class ApplicantSerializer(serializers.ModelSerializer):
    applicant_skills = ApplicantSkillSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Applicant
        fields = ['first_name', 'last_name', 'applicant_skills']
