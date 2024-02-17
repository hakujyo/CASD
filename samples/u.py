from samples import views
from mysite.school import StudentViews
from django.urls import path

urlpatterns = [
    path('student/', views.StudentView.as_view(), name="student"),
    path('student/<int:pk>/', views.StudentView.as_view(), name="student"),
    path('student/', StudentViews.StudentView.as_view(), name="student"),
    path('student/<int:pk>/', StudentViews.StudentView.as_view(), name="student")
]