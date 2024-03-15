from datetime import datetime, timezone

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ..logic.checkpoint_logic import get_checkpoint


@csrf_exempt
def checkpoint(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            user_checkpoint = get_checkpoint(user_id)
            if user_checkpoint:
                return JsonResponse(user_checkpoint, safe=False)
            else:
                return JsonResponse({'error': '404 User not found', 'timestamp': datetime.now(timezone.utc)}, status=404)
        else:
            return JsonResponse({'error': '400 user_id is required', 'timestamp': datetime.now(timezone.utc)}, status=400)
