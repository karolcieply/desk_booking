from datetime import datetime

from django.urls import path, register_converter

from labs_booking.scheduler import views
from labs_booking.scheduler.views import (
    SessionCancelView,
    SessionCreateView,
    SessionDetailView,
    SessionEditView,
    SessionListView,
)


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value


register_converter(DateConverter, "yyyy")

urlpatterns = [
    path("", SessionCreateView.as_view(), name="session-create"),
    path("about/", views.about, name="scheduler-about"),
    path("sessions/", SessionListView.as_view(), name="scheduler-sessions"),
    path("sessions/<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
    path(
        "sessions/new/<yyyy:date>/",
        SessionCreateView.as_view(),
        name="session-create-date",
    ),
    path(
        "sessions/new/<yyyy:date>/<str:timeblock>",
        SessionCreateView.as_view(),
        name="session-create-spec",
    ),
    path("sessions/<int:pk>/edit", SessionEditView.as_view(), name="session-edit"),
    path(
        "sessions/<int:pk>/cancel", SessionCancelView.as_view(), name="session-cancel"
    ),
    path("issues/", views.report_issues, name="scheduler-issues"),
]
