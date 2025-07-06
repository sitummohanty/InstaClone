"""
History:
--------
• **v1.0 – 2025-07-06**
Create and return a new "User" instance from validated serializer data.

Django’s "create_user()" helper:
- hashes the raw password
- enforces username constraints
- saves the object in one step

Parameters:
-----------
validated_data : dict
Cleaned data produced by "serializer.is_valid()".

Returns:
--------
django.contrib.auth.models.User
The newly created, fully saved user instance.
"""

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import UserProfile

class UserCreateSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = ('username', 'password', 'email', ) # <-- Postman JSON input fields

	def create(self, validated_data):

		user = User.objects.create_user(**validated_data)

		UserProfile.objects.create(user=user)

		return user


