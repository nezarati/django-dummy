- https://github.com/nezarati/django-dummy/tree/main/business_profile
- https://testdriven.io/blog/customize-django-admin
- https://djangocentral.com/django-orm-cheatsheet
- https://cheatography.com/lewiseason/cheat-sheets/django-models
- https://revsys.com/static/images/django-1.5-cheatsheet.pdf

```py
created_at = models.DateTimeField(auto_now_add=True)
changed_at = models.DateTimeField(auto_now=True)
from urllib import request
from django.contrib.auth.models import User
created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

chained_filters = MyModel.objects.filter(field_name='value', another_field=42)
excluded_objects = MyModel.objects.exclude(field_name='value')
single_object = MyModel.objects.get(pk=1)

from django.db.models import Q, F
q = Q(field_name='value') | (Q(another_field=42) & Q(field_name=F('first_field__nested_field__year')))
query = MyModel.objects.filter(q)[:10]

ordered_objects = MyModel.objects.order_by('field_name', '-field_name')
count_objects = MyModel.objects.count()

obj = MyModel(field_name='value', another_field=42)
obj.save()
obj.delete()

ModelAdmin.has_view_permission(self, request: HttpRequest, obj=None)
ModelAdmin.has_add_permission(self, request: HttpRequest)
ModelAdmin.has_change_permission(self, request: HttpRequest, obj=None)
ModelAdmin.has_delete_permission(self, request: HttpRequest, obj=None)
    if obj is not None and obj.created_by != request.user:
        return False
    return True


def get_queryset(self, request):
    qs = super().get_queryset(request)
    if request.user.is_superuser:
        return qs
    return qs.filter(created_by=request.user)

def save_model(self, request, obj, form, change):
    if not change
        obj.created_by = request.user
    super().save_model(self, request, obj, form, change)

def delete_model(self, request, obj):
    """
    Given a model instance delete it from the database.
    """
    obj.delete()
```