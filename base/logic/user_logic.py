from base.models import User


def get_user(user_id) -> User:
    user = None
    
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        return user, 200

    return user, 404