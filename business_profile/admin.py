from django.contrib import admin
from django.http import HttpRequest
from django.forms import ModelForm
from .models import (
    BusinessProfile,
    City,
    FullName,
    Insurance,
    Locality,
    NamedTelephone,
    PostalAddress,
    Skill,
    WebLink,
    WorkDay,
)


# Register your models here.
class BusinessProfileForm(ModelForm):
    class Meta:
        model = BusinessProfile
        fields = "__all__"  # ["gender", "person_name", ...]
        # exclude = ["expires_at"]


class NamedTelephoneInline(admin.TabularInline):
    model = NamedTelephone
    extra = 1


class WebLinkInline(admin.TabularInline):
    model = WebLink
    extra = 1


class WorkWeekInline(admin.TabularInline):
    model = WorkDay
    extra = 1


class BusinessProfileAdmin(admin.ModelAdmin):
    form = BusinessProfileForm
    # def get_exclude(self, request, obj=None):  # it works for flat fields
        # return ["expires_at"]
    # fields = ["display_name", "get_types"]

    fieldsets = [
        (
            "Person",
            {
                "fields": [
                    ("person_name", "gender"),
                    ("specialty", "fellowship", "subspecialty"),
                ]
            },
        ),
        ("Place", {"fields": ["place_name", "tagline"]}),
        (
            None,
            {
                "fields": [
                    "types",
                    ("city", "localities", "geoAddress"),
                    "services",
                    "insurances",
                    "description",
                    "note",
                    "image",
                    "expires_at",
                ],
                # "classes": ["collapse"],
            },
        ),
    ]
    inlines = [NamedTelephoneInline, WebLinkInline, WorkWeekInline]
    def get_fieldsets(self, request: HttpRequest, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        def remove_from_fieldsets(fieldsets, field):
            for fieldset in fieldsets:
                if field in fieldset[1]['fields']:
                    fieldset[1]['fields'].remove(field)
                    break
        
        if not request.user.is_superuser:
            remove_from_fieldsets(fieldsets, 'expires_at')
        if not request.user.is_staff:
            remove_from_fieldsets(fieldsets, 'note')
        return fieldsets


    list_display = ["display_name", "get_types", "expires_at", "image"]

    list_filter = [
        "types",
        "city",
        "localities",
        "services",
        "insurances",
        "expires_at",
    ]
    search_fields = [
        "person_name__given_name",
        "person_name__family_name",
        "place_name",
    ]

    def get_types(self, obj):
        return " و ".join([item.name for item in obj.types.all()])

    get_types.short_description = "types"

    def has_view_permission(self, request: HttpRequest, obj=None):
        return request.user.is_authenticated

    def has_add_permission(self, request: HttpRequest):
        return request.user.is_superuser

    def has_change_permission(self, request: HttpRequest, obj=None):
        if obj is not None and obj.created_by != request.user:
            return False
        return True

    def has_delete_permission(self, request: HttpRequest, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.changed_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(BusinessProfile, BusinessProfileAdmin)
admin.site.register(Skill)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Insurance)
admin.site.register(PostalAddress)
admin.site.register(FullName)
# admin.site.register(WebLink)
# admin.site.register(NamedTelephone)
# admin.site.register(WorkDay)