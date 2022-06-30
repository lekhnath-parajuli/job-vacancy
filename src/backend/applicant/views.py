from . import models
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    JobSerializer, SkillSerializer,
    ApplicantSerializer, ApplicantSkillSerializer
)


@api_view(['GET'])
def qualified_applicants(request) -> Response:

    def get_req_skills(job): return list(
        skill['skill_name'] for skill in job['req_skills'])

    def get_applicant_skills(applicant): return list(
        skill['skill_name'] for skill in applicant['applicant_skills'])

    def get_common_skills(req_skills, applicant_skills): return list(
        set(req_skills).intersection(applicant_skills))

    vacancy = models.Job.objects.all()
    applicants = models.Applicant.objects.all()

    vacancy_data = JobSerializer(vacancy, many=True).data
    applicant_data = ApplicantSerializer(applicants, many=True).data

    qualified = []
    for job in vacancy_data:
        req_skills = get_req_skills(job)
        for applicant in applicant_data:
            applicant_skills = get_applicant_skills(applicant)
            common_skills = get_common_skills(req_skills, applicant_skills)
            if common_skills:
                qualified.append(applicant)

    return Response(qualified)


@ api_view(['GET'])
def applicants_view(request) -> Response:
    applicant_instance = models.Applicant.objects.all()
    data = ApplicantSerializer(applicant_instance, many=True).data

    return Response(data)


@ api_view(['GET'])
def vacancy_view(request) -> Response:
    job_instance = models.Job.objects.all()
    data = JobSerializer(job_instance, many=True).data

    return Response(data)


@ api_view(['POST'])
def vacancy_position(request) -> Response:
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = JobSerializer(instance).data
        return Response(data)


@ api_view(['POST'])
def vacancy_skills(request) -> Response:
    serializer = SkillSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = SkillSerializer(instance).data
        return Response(data)


@ api_view(['POST'])
def applicant_info(request) -> Response:
    serializer = ApplicantSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = ApplicantSerializer(instance).data
        return Response(data)


@ api_view(['POST'])
def applicant_skills(request) -> Response:
    serializer = ApplicantSkillSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = ApplicantSkillSerializer(instance).data
        return Response(data)
