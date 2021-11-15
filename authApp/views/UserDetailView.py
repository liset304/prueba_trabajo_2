from django.conf                        import settings
from rest_framework                     import generics, status
from rest_framework.response            import Response
from rest_framework_simplejwt.backends  import TokenBackend
from rest_framework.permissions         import IsAuthenticated
from rest_framework_simplejwt.backends  import TokenBackend

from authApp.models.user                import User
from authApp.serializer.user_serializer import Userserializer

class UserDetailView(generics.RetrieveAPIView):
    queryset            = User.objects.all()
    serializer_class    = Userserializer
    permission_classes  = (IsAuthenticated, )

    def get(selt, request, *args, **Kwargs):
        token           = request.META.get('HTTP_AUTHORIZATION')[7: ]
        token_backend   = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != Kwargs['pk']:
            string_response = { 'detail':'Acceso No Autorizado.'}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **Kwargs)


