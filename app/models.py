from django.db import models
import uuid
# Create your models here.
class UserKey(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    oem_1 = models.CharField(max_length=255)
    oem_2 = models.CharField(max_length=255)
    oem_3 = models.CharField(max_length=255)
    timestamp1 = models.CharField(max_length=255)
    timestamp2 = models.CharField(max_length=255)
    timestamp3 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.user.username


class RegistryHelper(models.Model):
    key_hive = models.CharField(max_length=255)
    key_version = models.CharField(max_length=255)
    value_name = models.CharField(max_length=255)
    value_type = models.CharField(max_length=255)
    access_type = models.CharField(max_length=255)


    def __str__(self):
        return self.key_hive
    

    



   