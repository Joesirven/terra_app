from django.urls import path

from .views import (
    api_courses,
    api_course,
    api_room,
    api_rooms,
    api_departments,
    api_department,
    api_prereqs,
    api_prereq,
    api_sections,
    api_section,
)

urlpatterns = [
    path("course/", api_courses, name="api_courses",),
    path("courses/<str:course_code>/", api_course, name="api_course",),
    path("rooms/", api_rooms, name="api_rooms",),
    path("rooms/<str:room_num>/", api_room, name="api_room",),
    path("departments/", api_departments, name="api_departments",),
    path("departments/<str:name>/", api_department, name="api_department",),
    path("prereqs/", api_prereqs, name="api_prereqs",),
    path("prereqs/<str:course>/", api_prereq, name="api_prereq",),
    path("sections/", api_sections, name="api_sections",),
    path("sections/<str:section_num>/", api_section, name="api_section",),
]
