import uuid
from django.db import models, transaction
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # poster = models.ImageField(upload_to='Elearning/course-posters/', null=True, blank=True)  # Poster for the course
    poster = CloudinaryField('image', null=True, blank=True, folder='Elearning/course-posters/')
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed'), ('inactive', 'Inactive')], default='active')  # Track enrollment status
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Track course completion as a percentage
    completion_date = models.DateTimeField(null=True, blank=True)  # When the course was completed (if applicable)
    last_watched_video = models.UUIDField(null=True, blank=True)  # Track the last watched video for this enrollment

    class Meta:
        unique_together = ('user', 'course')  # Ensure each user is enrolled only once per course

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)  # URL to access the video
    video_file = CloudinaryField('video', resource_type='video', null=True, blank=True, folder='Elearning/videos/')
    poster = CloudinaryField('image', null=True, blank=True, folder='Elearning/video-posters/')
    duration = models.DurationField(null=True, blank=True)  # Duration in seconds
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_order = models.PositiveIntegerField()  # New field for video order in the course

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # New field to link to Course
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    last_watched_time = models.FloatField()
    watched_status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'video')  # Ensures each user has one record per video

    def __str__(self):
        return f"{self.user.username} - {self.video.title} - {self.course.title}"
