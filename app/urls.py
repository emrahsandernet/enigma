from django.urls import path
from .views import  UserKeyList, registry_helper_list, UserKeyDetail, RegistryHelperDetail

urlpatterns = [
    path('userkey/', UserKeyList.as_view(), name='userkey-list'),
    path('userkey/<str:pk>/', UserKeyDetail.as_view(), name='userkey-detail'),
    
    path('registryhelper/', registry_helper_list, name='registryhelper-list-1'),
    path('registryhelper/<int:pk>/', RegistryHelperDetail.as_view(), name='registryhelper-detail'),

]
