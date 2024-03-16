from datetime import datetime, timezone

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ..logic.checkpoint_logic import create_update_checkpoint, get_checkpoint


@csrf_exempt
def checkpoint(request):
    user_id = request.GET.get('user_id')

    if request.method == 'GET':
        return get_req_checkpoint(user_id)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        return post_req_create_update_checkpoint(user_id, data)


def get_req_checkpoint(user_id):
    if user_id:
        user_checkpoint, status = get_checkpoint(user_id)
        if user_checkpoint:
            return JsonResponse(user_checkpoint, safe=False, status=status)
        else:
            return JsonResponse({'error': '404 User not found', 'timestamp': datetime.now(timezone.utc)}, status=404)
    else:
        return JsonResponse({'error': '400 user_id is required', 'timestamp': datetime.now(timezone.utc)}, status=400)


def post_req_create_update_checkpoint(user_id, fields):
    fields['user_id'] = user_id
    user_checkpoint, status = create_update_checkpoint(fields)
    if user_checkpoint:
        return JsonResponse(user_checkpoint, safe=False, status=status)
    else:
        return JsonResponse({'error': '404 User not found', 'timestamp': datetime.now(timezone.utc)}, status=404)
