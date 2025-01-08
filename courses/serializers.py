from rest_framework import serializers
from .models import Course, Video, WatchHistory, Enrollment

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_url', 'poster_url', 'duration', 'created_at', 'updated_at', 'video_order']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'poster_url']

class WatchHistorySerializer(serializers.ModelSerializer):
    video_title = serializers.CharField(source='video.title', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = WatchHistory
        fields = ['id', 'user', 'course', 'video', 'last_watched_time', 'watched_status', 'video_title', 'course_title']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'status', 'completion_percentage', 'completion_date', 'enrollment_date', 'last_watched_video']