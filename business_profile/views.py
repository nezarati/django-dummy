import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.db.models import Q
from .models import BusinessProfile

whitelist_fields = (
    "id",
    "gender",
    "person_name",
    "place_name",
    "tagline",
    "city",
    "geoAddress",
    "description",
    # "note",
    "image",
    # "expires_at",
    "types",
    "specialty",
    "fellowship",
    "subspecialty",
    "localities",
    "services",
    "insurances",
)


# Create your views here.
def index(request: HttpRequest):
    items = BusinessProfile.objects.all()

    name = request.GET.get("name", None)
    if name:
        items = items.filter(
            Q(place_name__icontains=name)
            | Q(person_name__given_name__icontains=name)
            | Q(person_name__family_name__icontains=name)
        )

    service = request.GET.get("service", None)
    if service:
        items = items.filter(services__name=service)

    items = items.order_by("-expires_at")[:25]

    # return JsonResponse(list(items.values(*whitelist_fields)), safe=False)
    dump = serializers.serialize("json", items)
    # dump = json.dumps(items)
    return HttpResponse(dump, content_type="application/json")


def detail(request, pk):
    object = get_object_or_404(BusinessProfile, pk=pk)

    # return JsonResponse(object)
    dump = serializers.serialize("json", [object])[1:-1]
    return HttpResponse(dump, content_type="application/json")
