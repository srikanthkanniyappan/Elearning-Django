# courses/serializers.py

from rest_framework import serializers
from .models import Course, Video, WatchHistory, Enrollment

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'url', 'video_file', 'poster', 'duration', 'created_at', 'updated_at', 'video_order']

    video_file = serializers.FileField(required=False)  # Optional video file field for uploads
    poster = serializers.ImageField(required=False)  # Optional poster field for the video thumbnail

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'poster']
    poster = serializers.ImageField(required=False)

class WatchHistorySerializer(serializers.ModelSerializer):
    video_title = serializers.CharField(source='video.title', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)  # Add course title

    class Meta:
        model = WatchHistory
        fields = ['id', 'user', 'course', 'video', 'last_watched_time', 'watched_status', 'video_title', 'course_title']  # Include course field

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'status', 'completion_percentage', 'completion_date', 'enrollment_date', 'last_watched_video']