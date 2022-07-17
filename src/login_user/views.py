from rest_framework import viewsets, status, mixins
from .serializers import LoginUserSerializer
from rest_framework.response import Response
from django.conf import settings

from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from rest_framework_simplejwt.tokens import RefreshToken

from register_user.models import Usuario
from .models import LoginUserModel


# tempo de vida do cache 
# https://realpython.com/caching-in-django-with-redis/

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# função para buscar o valor do cache
def get_cache(key):
    return cache.get(key)
  
# função para salvar o valor do cache
def set_cache(key, value):
    cache.set(key, value, CACHE_TTL)



class LoginUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = LoginUserSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        try:
            user = Usuario.objects.get(email=email)
      
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'email não cadastrado'})
        # check_password compara a senha do hash com a senha de texto simples e verificamos se elas são equivalentes
        # a senha de hash ou não.
        # https://pythonguides.com/encrypt-and-decrypt-password-in-django/
        if not user.check_password(password):
            return Response(
                data={
                    'detail': 'password inválido'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
     
        token_cache = get_cache(user.id)
        if token_cache:
            return Response(
                data={
                    'refresh': token_cache['refresh'],
                    'access': token_cache['access'],
                    'user_id': user.id,
                    'message': "redis"
                },
                status=status.HTTP_200_OK
            )
        # cria um token de acesso e um token de refresh manualmente
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id
        }

        LoginUserModel.objects.create(
            user_id=user.id,
            refresh=str(refresh),
            access=str(refresh.access_token)
        )

        set_cache(user.id, data)
        return Response(
            data={
                'refresh': data['refresh'],
                'access': data['access'],
                'user_id': user.id,
                'message': 'banco'
            },
            status=status.HTTP_200_OK
        )
