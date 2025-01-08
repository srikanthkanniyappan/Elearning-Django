from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Course, Video, WatchHistory, Enrollment
from .serializers import CourseSerializer, WatchHistorySerializer, VideoSerializer
from django.utils import timezone
from uuid import UUID

def validate_uuid(uuid_str):
    try:
        # Convert input to UUID object to validate, then back to string to maintain consistency
        return str(UUID(str(uuid_str)))
    except (ValueError, TypeError):
        return None

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_video(request):
    """Handles uploading a video."""
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_courses(request):
    """Lists all available courses."""
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enrolled_list_courses(request):
    """Lists courses the user is enrolled in."""
    user = request.user
    # Filter courses by user enrollment
    enrolled_courses = Enrollment.objects.filter(user=user).values_list('course', flat=True)
    courses = Course.objects.filter(id__in=enrolled_courses)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_courses_with_enrollment_status(request):
    """Lists all courses with enrollment status for the logged-in user."""
    user = request.user
    # Get all courses
    courses = Course.objects.all()
    # Get courses the user is enrolled in
    enrolled_course_ids = Enrollment.objects.filter(user=user).values_list('course_id', flat=True)
    # Serialize courses and add enrollment status
    serialized_courses = []
    for course in courses:
        serialized_course = CourseSerializer(course).data
        serialized_course['is_enrolled'] = course.id in enrolled_course_ids  # Add enrollment status
        serialized_courses.append(serialized_course)

    return Response(serialized_courses, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course_details(request, course_id):
    """Retrieve details for a specific course."""
    course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch the course using the validated UUID
        course = Course.objects.get(id=course_uuid)

        # Check if the user is enrolled in this course
        user = request.user
        if not Enrollment.objects.filter(user=user, course=course).exists():
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Serialize the course details
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_last_watched(request, course_id):
    """Retrieve the last-watched video for a specific course."""
    course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch the course using the validated UUID
        course = Course.objects.get(id=course_uuid)

        # Check if the user is enrolled in this course
        user = request.user
        enrollment = Enrollment.objects.filter(user=user, course=course).first()
        if not enrollment:
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Get the last_watched_video from the enrollment
        last_watched_video = enrollment.last_watched_video

        if not last_watched_video:
            # If no video has been watched, fetch the video with video_order = 1
            first_video = course.videos.filter(video_order=1).first()
            if first_video:
                # Return the video with video_order = 1
                return Response({"last_watched_video": first_video.id}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "No videos available in this course."}, status=status.HTTP_404_NOT_FOUND)

        # Return the last watched video ID
        return Response({"last_watched_video": last_watched_video}, status=status.HTTP_200_OK)

    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_last_watched(request, course_id):
    """Update the last-watched video ID for an enrollment."""
    course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch the course using the validated UUID
        course = Course.objects.get(id=course_uuid)

        # Check if the user is enrolled in this course
        user = request.user
        enrollment = Enrollment.objects.filter(user=user, course=course).first()
        if not enrollment:
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Get the last_watched video ID from request data
        last_watched = request.data.get('last_watched')
        if not validate_uuid(last_watched):  # Validate the video ID
            return Response({"error": "Invalid video ID format."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the enrollment's last_watched_video field
        enrollment.last_watched_video = last_watched
        enrollment.save()

        return Response({"message": "Last watched video updated successfully."}, status=status.HTTP_200_OK)

    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course_videos(request, course_id):
    """Retrieve videos for a specific course."""
    # Validate the course UUID
    course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course = Course.objects.get(id=course_uuid)
        # Check if the user is enrolled in this course
        user = request.user
        if not Enrollment.objects.filter(user=user, course=course).exists():
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        videos = Video.objects.filter(course=course).order_by('video_order')  # Order by video order
        video_serializer = VideoSerializer(videos, many=True)
        return Response(video_serializer.data)

    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_video(request, video_id):
    """Retrieve details for a specific video."""
    # Validate the video UUID
    video_uuid = validate_uuid(video_id)
    if not video_uuid:
        return Response({"error": "Invalid video ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Retrieve the video by ID
        video = Video.objects.get(id=video_uuid)
        user = request.user

        # Check if the user is enrolled in the course related to the video
        if not Enrollment.objects.filter(user=user, course=video.course).exists():
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Serialize the video details
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Video.DoesNotExist:
        return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course_watch_history(request, course_id):
    """Handles retrieving watch history for all videos in a particular course."""
    # Validate the course UUID
    course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course = Course.objects.get(id=course_uuid)
        user = request.user

        # Check if the user is enrolled in this course
        if not Enrollment.objects.filter(user=user, course=course).exists():
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Retrieve all videos for the course
        videos = Video.objects.filter(course=course)

        # Fetch the watch history for each video for the current user
        watch_histories = WatchHistory.objects.filter(user=user, video__in=videos)

        # If no watch history exists, create default data for each video
        if not watch_histories.exists():
            default_data = [
                {
                    "id": None,
                    "user": user.id,
                    "video": video.id,
                    "course": course.id,
                    "last_watched_time": 0,  # Default time for new entries
                    "watched_status": False,     # Default status for unwatched videos
                    "video_title": video.title,
                    "course_title": course.title,
                }
                for video in videos
            ]
            return Response(default_data, status=status.HTTP_200_OK)

        # Serialize the existing watch histories
        watch_history_serializer = WatchHistorySerializer(watch_histories, many=True)
        return Response(watch_history_serializer.data, status=status.HTTP_200_OK)

    except Course.DoesNotExist:
        return Response({"error": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_video_watch_history(request, video_id):
    """Retrieve watch history for a specific video."""
    # Validate the video UUID
    video_uuid = validate_uuid(video_id)
    if not video_uuid:
        return Response({"error": "Invalid video ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Retrieve the video by ID
        video = Video.objects.get(id=video_uuid)
        user = request.user

        # Check if the user is enrolled in the course related to the video
        if not Enrollment.objects.filter(user=user, course=video.course).exists():
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Retrieve the watch history for the video and user
        try:
            watch_history = WatchHistory.objects.get(user=user, video=video)
            serializer = WatchHistorySerializer(watch_history)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except WatchHistory.DoesNotExist:
            return Response(
                {
                    "id": None,
                    "user": user.id,
                    "video": video.id,
                    "course": video.course.id,
                    "last_watched_time": 0,  # Default to 0 if no history exists
                    "watched_status": False  # Default to unwatched
                },
                status=status.HTTP_200_OK
            )
    except Video.DoesNotExist:
        return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_watch_history(request, video_id):
    """Handles updating the watch history for a specific video."""
    # Validate the video UUID
    video_uuid = validate_uuid(video_id)
    if not video_uuid:
        return Response({"error": "Invalid video ID format."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Retrieve the video by ID
        video = Video.objects.get(id=video_uuid)
        user = request.user

        # Check if the user is enrolled in the course related to the video
        if not Enrollment.objects.filter(user=user, course=video.course).exists():
            return Response({"error": "User not enrolled in this course."}, status=status.HTTP_403_FORBIDDEN)

        # Get last watched time and watched_status from request data
        last_watched_time = request.data.get('last_watched_time')
        watched_status = request.data.get('watched_status', False)  # Default to False if not provided

        # Validate last_watched_time
        if last_watched_time is None:
            return Response({"error": "Last watched time is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve or create the watch history record for the user and video
        watch_history, created = WatchHistory.objects.get_or_create(
            user=user,
            video=video,
            defaults={
                'course': video.course,
                'last_watched_time': last_watched_time,  # Initialize with provided last_watched_time
                'watched_status': watched_status        # Initialize with provided or default watched_status
            }
        )

        # Update the watch history record
        watch_history.last_watched_time = last_watched_time
        watch_history.watched_status = watched_status
        watch_history.course = video.course  # Ensure the course is always correctly set
        watch_history.save()

        # Serialize the updated watch history data
        serializer = WatchHistorySerializer(watch_history)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Video.DoesNotExist:
        return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_in_course(request):
    """Enroll a user in a course."""
    user = request.user
    course_id = request.data.get('course_id')

    # Validate the course UUID
    course_uuid = validate_uuid(course_id["course_id"])
    # course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    if not course_id:
        return Response({"error": "Course ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course = Course.objects.get(id=course_uuid)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    # Enroll user in the course
    enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)
    if created:
        return Response({"message": f"Successfully enrolled in {course.title}"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": f"Already enrolled in {course.title}"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_enrollment_status(request):
    """Update the enrollment status and completion percentage."""
    user = request.user
    course_id = request.data.get('course_id')
    status_value = request.data.get('status')  # 'active', 'completed', etc.
    completion_percentage = request.data.get('completion_percentage')  # 0-100 range

    # Validate the course UUID
    course_uuid = validate_uuid(course_id)
    if not course_uuid:
        return Response({"error": "Invalid course ID format."}, status=status.HTTP_400_BAD_REQUEST)

    if not course_id:
        return Response({"error": "Course ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        enrollment = Enrollment.objects.get(user=user, course_id=course_uuid)
    except Enrollment.DoesNotExist:
        return Response({"error": "Enrollment not found"}, status=status.HTTP_404_NOT_FOUND)

    # Validate completion_percentage (0-100 range)
    if completion_percentage is not None:
        if not (0 <= completion_percentage <= 100):
            return Response({"error": "Completion percentage must be between 0 and 100"},
                            status=status.HTTP_400_BAD_REQUEST)

    # Update status and completion percentage
    if status_value:
        enrollment.status = status_value
    if completion_percentage is not None:
        enrollment.completion_percentage = completion_percentage
        if completion_percentage == 100:
            enrollment.completion_date = timezone.now()  # Set completion date if fully completed

    enrollment.save()
    return Response({
        "message": "Enrollment status and completion updated",
        "status": enrollment.status,
        "completion_percentage": enrollment.completion_percentage
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def getRoutes(request):
    """Get available API routes.""" 
    routes = [
        {'GET': '/all-courses/'},
        {'GET': '/course-list/'},
        {'GET': '/course-details/<uuid:course_id>/'},
        {'GET': '/course-videos/<uuid:course_id>/'},
        {'GET': '/course-content/<uuid:course_id>/watch-history/'},
        {'GET': '/course/<uuid:course_id>/last-watched/'},
        {'POST': '/course/<uuid:course_id>/last-watched/update/'},
        {'GET': '/videos/<uuid:video_id>/'},
        {'GET': '/videos/<uuid:video_id>/watch-history/'},
        {'POST': '/videos/<uuid:video_id>/watch-history/update/'},
        {'POST': '/videos/upload/'},
        {'POST': '/enroll/'},
        {'POST': '/enrollment/update/'},
    ]
    return Response(routes)
