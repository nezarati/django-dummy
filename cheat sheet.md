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

## Install

```shell
# Install python version
pyenv install 3.8.10

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source ./.venv/bin/activate

# Your python version stays `3.8.10`, but you need to update `pip` to help install `black` package.
./.venv/bin/python -m pip install --upgrade pip

# Do `git clone --branch develop` for its dependencies at the same level as `REPO` project and install them.
cd ..

git clone --branch develop ...
pip install -e ./DEPENDENCY

cd REPO

# Install projects development requirements
pip install -r REPO/requirements/dev.txt
```

### Importing database
To access the container shell, run the following command:
```shell
docker exec -it NAME sh
```

To restore PostgreSql database:
```shell
gunzip -c < dummy.dump.gz | psql -U postgres -h localhost dummy
```

### On Windows

#### Execution Policy Settings for PowerShell Script
First of all, you need to change execution policy.
```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

#### `pyenv-win`
This is `pyenv` for Windows. [Here](https://github.com/pyenv-win/pyenv-win) is its repository:

Use the following command to activate virtual environment:
```shell
.\.venv\Scripts\activate
```

#### Updating `pip`
```shell
.\.venv\scripts\python.exe -m pip install --upgrade pip
```

#### `pysha3` problem
For building `pysha3` on Windows, you need to install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools).
