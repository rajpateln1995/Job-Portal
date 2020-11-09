from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team', TemplateView.as_view(template_name="inner-team-2.html")),
    path('contact', TemplateView.as_view(template_name="inner-contact-2.html")),
    
    path('search', SearchView.as_view(), name='searh'),
    path('employer/dashboard/', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
        path('mark-delete/<int:job_id>', delete, name='job-mark-delete'),
    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('applications', ApplicationsView.as_view(), name='applications'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
]
