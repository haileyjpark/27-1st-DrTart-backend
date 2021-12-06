import jwt

from django.http import JsonResponse

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM

def authorization(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            token = request.headers.get('Authorization')

            if not token:
                return JsonResponse({'MESSAGE': 'TOKEN_REQUIRED'}, status=401)

            payload      = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            user         = User.objects.get(id=payload['user_id'])
            request.user = user

            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'MESSAGE': 'INVALID_TOKEN'}, status=401)

        except KeyError:
            return JsonResponse({'MESSAGE': 'KER_ERROR'}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE': 'INVALID_USER'}, status=401)

    return wrapper