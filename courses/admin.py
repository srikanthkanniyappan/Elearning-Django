from django.contrib import admin
from .models import Course, Video, WatchHistory, Enrollment

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'poster')  # Display course title, created/updated time, and poster
    list_filter = ('created_at', 'updated_at')  # Add filter options for course creation and update time
    search_fields = ('title', 'description')  # Allow searching by course title and description

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration', 'created_at', 'video_order')  # Display video title, course, duration, and order
    list_filter = ('course', 'created_at', 'duration')  # Filter by course, creation date, and video duration
    search_fields = ('title', 'course__title')  # Allow searching by video title and course title

class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'video', 'last_watched_time', 'watched_status', 'updated_at')  # Display relevant fields
    list_filter = ('user', 'course', 'watched_status', 'updated_at')  # Filter by user, course, watched status, and update time
    search_fields = ('user__username', 'course__title', 'video__title')  # Search by username, course title, and video title

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'status', 'completion_percentage', 'completion_date', 'enrollment_date')  # Display relevant fields
    list_filter = ('user', 'course', 'status', 'enrollment_date')  # Filter by user, course, status, and enrollment date
    search_fields = ('user__username', 'course__title')  # Search by username and course title

# Register the models with their respective custom admin configurations
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(WatchHistory, WatchHistoryAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
