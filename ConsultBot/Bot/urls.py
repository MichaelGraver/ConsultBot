from django.conf.urls import url
from Bot import views

urlpatterns = [
    url(r'Consent/', views.Consent.as_view(), name='Consent'),
    url(r'^$', views.Intro.as_view(), name='Intro'),
    url(r'index/', views.index.as_view(), name='index'),
    url(r'survey/', views.QuestionnaireView.as_view(), name='Questionnaire'),
]