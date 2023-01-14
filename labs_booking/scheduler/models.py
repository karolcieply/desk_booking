from datetime import date

# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Session(models.Model):

    TIMEBLOCK_CHOICES = (
        ("A", "8:00-9:00"),
        ("B", "9:00-10:00"),
        ("C", "10:00-11:00"),
        ("D", "11:00-12:00"),
        ("E", "12:00-13:00"),
        ("F", "13:00-14:00"),
        ("G", "14:00-15:00"),
        ("H", "15:00-16:00"),
        ("I", "16:00-17:00"),
        ("J", "17:00-18:00"),
        ("K", "18:00-19:00"),
        ("L", "19:00-20:00"),
    )

    LABS = (
        ("Quantum Computing Workstation","Quantum Computing Workstation"),
        ("X-ray Diffraction Workstation","X-ray Diffraction Workstation"),
        ("Nuclear Magnetic Resonance Workstation","Nuclear Magnetic Resonance Workstation"),
        ("Particle Accelerator Workstation","Particle Accelerator Workstation")
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    timeblock = models.CharField(max_length=10, choices=TIMEBLOCK_CHOICES, default="A")

    lab_workstation = models.CharField(max_length=40, choices=LABS, default="A")
    operator_licence = models.CharField(max_length=30, default="")
    additional_info = models.CharField(max_length=50, default="")

    # @property
    def is_upcoming(self):
        return date.today() <= self.date

    is_upcoming.admin_order_field = "date"
    is_upcoming.boolean = True
    is_upcoming.short_description = "Session in the future?"

    @property
    def get_weekday(self):
        return self.date.strftime("%A")

    def __str__(self) -> str:
        return f"{self.student.username}: {self.date} ({self.timeblock})"

    def get_absolute_url(self):
        # returns a complete url string and let view handle the redirect
        return reverse("session-detail", kwargs={"pk": self.pk})


# REF: READ https://docs.djangoproject.com/en/4.0/topics/db/models/
class DayBlock(models.Model):
    date = models.DateField(default=timezone.now)
    # onduty = models.OneToOneField(Lab, on_delete=models.CASCADE, default="")
    # allBlocks = Session.objects.filter(date=date)
    # blockA = allBlocks.filter(timeblo)
    # blockB = models.OneToOneField(Lab, on_delete=models.CASCADE, default='')
    # blockC = models.OneToOneField(Lab, on_delete=models.CASCADE, default='')
    # blockD = models.OneToOneField(Lab, on_delete=models.CASCADE, default='')
    # blockE = models.OneToOneField(Lab, on_delete=models.CASCADE, default='')
    # blockF = models.OneToOneField(Lab, on_delete=models.CASCADE, default='')


class Issue(models.Model):
    email = models.EmailField()
    issue = models.TextField()
    user_agent = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    # dunder STR
    def __str__(self):
        return self.email
