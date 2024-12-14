from django.urls import path
from .views import  UserKeyList, UserKeyDetail, RegistryHelperList, RegistryHelperDetail

urlpatterns = [
    path('userkey/', UserKeyList.as_view(), name='userkey-list'),
    path('userkey/<int:pk>/', UserKeyDetail.as_view(), name='userkey-detail'),
    path('registryhelper/', RegistryHelperList.as_view(), name='registryhelper-list'),
    path('registryhelper/<int:pk>/', RegistryHelperDetail.as_view(), name='registryhelper-detail'),
]
