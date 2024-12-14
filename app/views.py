
from rest_framework import generics

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import UserKey, RegistryHelper
from .serializers import UserKeySerializer, RegistryHelperSerializer


# Sadece listeleme (GET) için ViewSet'ler
class UserKeyList(generics.ListAPIView):
    queryset = UserKey.objects.all()
    serializer_class = UserKeySerializer



@api_view(['GET'])
def registry_helper_list(request):
    user_key = request.GET.get('user_id')
    user_key_list = UserKey.objects.filter(key=user_key)


    if user_key_list:
        registry_helper = RegistryHelper.objects.all()
        serializer = RegistryHelperSerializer(registry_helper, many=True)
        return Response(serializer.data)
    else:
        msg = "User key not found,fuck off"
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    
# Sadece detay (GET) için ViewSet'ler
class UserKeyDetail(generics.RetrieveAPIView):
    queryset = UserKey.objects.all()
    serializer_class = UserKeySerializer

    def get_object(self):
        queryset = self.get_queryset()


        return queryset.get(id=self.kwargs['pk'])
        

class RegistryHelperDetail(generics.RetrieveAPIView):
    queryset = RegistryHelper.objects.all()
    serializer_class = RegistryHelperSerializer