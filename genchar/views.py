from django.http import JsonResponse
from .models import GenshinChar
from .serializers import GenshinCharSerializer

def genshin_list(request):
    genshin = GenshinChar.objects.all()
    serializer = GenshinCharSerializer(genshin, many=True)
    return JsonResponse(serializer.data, safe=False)