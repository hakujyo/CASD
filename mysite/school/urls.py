
from . import StudentViews
from django.urls import path, re_path, include
urlpatterns = [
path('student/', StudentViews.StudentViews.as_view(), name='student/'), 
path('student/<int:pk>/', StudentViews.StudentViews.as_view(), name='student/')]
