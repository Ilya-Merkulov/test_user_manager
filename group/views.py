from .models import Groups
from .serializers import GroupsSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



# Create your views here.

@csrf_exempt
def group(request, id = 0):
    if request.method == 'GET':
        groups = Groups.objects.all()
        groups_serializer = GroupsSerializer(groups, many=True)
        return JsonResponse(groups_serializer.data, safe=False)

    elif request.method == 'POST':
        group_data = JSONParser().parse(request)
        group_serializer = GroupsSerializer(data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse("Group added", safe=False)
        return JsonResponse("Failed to add Group", safe=False)

    elif request.method == 'PUT':
        groups_data = JSONParser().parse(request)
        group = Groups.objects.get(id=groups_data['id'])
        group_serializer = GroupsSerializer(group, data=groups_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse('Group updating!!', safe=False)
        return JsonResponse('Failed to update Group!!!', safe=False)

    elif request.method == "DELETE":
        group = Groups.objects.get(id=id)
        group.delete()
        return JsonResponse('Delete!!', safe=False)