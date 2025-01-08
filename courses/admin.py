from django.contrib import admin
from .models import Course, Video, WatchHistory, Enrollment

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration', 'created_at', 'video_order')
    list_filter = ('course', 'created_at', 'duration')
    search_fields = ('title', 'course__title')

class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'video', 'last_watched_time', 'watched_status', 'updated_at')
    list_filter = ('user', 'course', 'watched_status', 'updated_at')
    search_fields = ('user__username', 'course__title', 'video__title')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'status', 'completion_percentage', 'completion_date', 'enrollment_date')
    list_filter = ('user', 'course', 'status', 'enrollment_date')
    search_fields = ('user__username', 'course__title')

# Register the models with their respective custom admin configurations
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(WatchHistory, WatchHistoryAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
