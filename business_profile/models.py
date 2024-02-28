from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="created_by_user"
    )
    changed_at = models.DateTimeField(auto_now=True)
    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="changed_by_user",
    )


class GenderState(models.IntegerChoices):
    NONE = 1, "ندارد"
    MALE = 2, "مرد"
    FEMALE = 3, "زن"


class WeekDay(models.IntegerChoices):
    SATURDAY = 6, "شنبه"
    SUNDAY = 0, "یک‌شنبه"
    MONDAY = 1, "دوشنبه"
    TUESDAY = 2, "سه‌شنبه"
    WEDNESDAY = 3, "چهارشنبه"
    THURSDAY = 4, "پنج‌شنبه"
    FRIDAY = 5, "جمعه"


class FullName(models.Model):
    prefix = models.CharField(max_length=50, blank=True)
    given_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    family_name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.prefix} {self.given_name} {self.middle_name} {self.family_name} {self.suffix}".strip()


class Skill(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostalAddress(models.Model):
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address_line = models.CharField(max_length=250)
    postalCode = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.region}، {self.city}، {self.address_line}"


class NamedTelephone(models.Model):
    profile = models.ForeignKey("BusinessProfile", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class WebLink(models.Model):
    profile = models.ForeignKey("BusinessProfile", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.URLField()

    def __str__(self):
        return self.name


class WorkDay(models.Model):
    profile = models.ForeignKey("BusinessProfile", on_delete=models.CASCADE)
    day = models.IntegerField(choices=WeekDay)
    start = models.TimeField()
    end = models.TimeField()
    limit = models.PositiveSmallIntegerField()

    def __str__(self):
        for item in WeekDay.choices:
            if item[0] == self.day:
                return item[1] + " " + str(self.start)


class BusinessProfile(BaseModel):
    gender = models.IntegerField(choices=GenderState)
    types = models.ManyToManyField(Skill, related_name="type_skills")
    person_name = models.ForeignKey(
        FullName, on_delete=models.SET_NULL, null=True, blank=True
    )
    place_name = models.CharField(max_length=100, null=True, blank=True)
    tagline = models.CharField(max_length=200, blank=True)
    specialty = models.ManyToManyField(
        Skill, related_name="specialty_skills", blank=True
    )
    fellowship = models.ManyToManyField(
        Skill, related_name="fellowship_skills", blank=True
    )
    subspecialty = models.ManyToManyField(
        Skill, related_name="subspecialty_skills", blank=True
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    localities = models.ManyToManyField(Locality, blank=True)
    geoAddress = models.ForeignKey(
        PostalAddress, on_delete=models.SET_NULL, null=True, blank=True
    )
    # geoPosition = models.PointField(null=True)
    services = models.ManyToManyField(Skill, related_name="service_skills", blank=True)
    insurances = models.ManyToManyField(Insurance, blank=True)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)
    # web_links = models.ManyToManyField(WebLink)
    # telephones = models.ManyToManyField(NamedTelephone)
    # work_week = models.ManyToManyField(WorkDay)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.display_name()

    @admin.display(
        description="Name",
    )
    def display_name(self):
        if self.place_name:
            return self.place_name
        return str(self.person_name)
