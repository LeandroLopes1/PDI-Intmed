from rest_framework import viewsets, status, mixins
from .serializers import LoginUserSerializer
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from register_user.models import Usuario
from .models import LoginUserModel

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
      
        if not user.check_password(password):
            return Response(
                data={
                    'detail': 'password inválido'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            } 
            LoginUserModel.objects.create(**data)
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
