from django.urls import path
from .views import (
    PostListView,
    CalendarView,
    StudentsView,
    LessonView,
    ProfileView,
    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('calendar', CalendarView.as_view(), name='calendar'),
    path('students', StudentsView.as_view(), name='students'),
    path('lesson', LessonView.as_view(), name='lesson'),
    path('profile', ProfileView.as_view(), name='profile'),
]