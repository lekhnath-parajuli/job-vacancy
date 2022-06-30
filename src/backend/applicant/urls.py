from django.urls import path
from . import views

urlpatterns = [
    path('qualified/', views.qualified_applicants),

    path('vacancy/', views.vacancy_view),
    path('vacancy/add-position', views.vacancy_position),
    path('vacancy/add-skills', views.vacancy_skills),

    path('applicant/', views.applicants_view),
    path('applicant/add-info', views.applicant_info),
    path('applicant/add-skills', views.applicant_skills)
]
