from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.getRoutes, name='courses_get_routes'),
    path('course-list/', views.list_courses, name='list_courses'),
    path('course-videos/<uuid:course_id>/', views.get_course_videos, name='get_course_videos'),
    path('course-details/<uuid:course_id>/', views.get_course_details, name='get_course_details'),
    path('course/<uuid:course_id>/last-watched/', views.get_last_watched, name='get_last_watched'),
    path('course/<uuid:course_id>/last-watched/update/', views.update_last_watched,name='update_last_watched'),
    path('course-content/<uuid:course_id>/watch-history/', views.get_course_watch_history, name='get_course_watch_history'),
    path('videos/<uuid:video_id>/', views.get_video, name='get_video'),
    path('videos/<uuid:video_id>/watch-history/', views.get_video_watch_history, name='get_video_watch_history'),
    path('videos/<uuid:video_id>/watch-history/update/', views.update_watch_history, name='update_watch_history'),
    path('videos/upload/', views.upload_video, name='upload_video'),
    path('enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('enrollment/update/', views.update_enrollment_status, name='update_enrollment_status'),
]
