"""
History
-------
• **v1.2 – 2025-06-20**
  – Introduced "TimeStamp" abstract base class to add "created_on" and
    "updated_on" to multiple models in one shot.
  – Replaced the earlier "ForeignKey" link with a stricter
    "OneToOneField" in "UserProfile" so each Django `"User" now has
    exactly one profile.
  – Added "is_verified" flag (default **True**) to track e-mail or
    verification status.
  – Set "profile_pic_url" default to an empty string instead of NULL
    for cleaner validation.
  _ Keep authentication concerns in Django’s proven "auth.User" model
    while extending per-user metadata—bio, profile photo, verification
    status—via "UserProfile".  The "TimeStamp" mixin enforces a uniform
    created/updated audit trail across the code-base.

• **v1.1 – 2025-06-18**
  – Switched from a hand-rolled "User" model to Django’s built-in
    "auth.User" for authentication.
  – Introduced "UserProfile" to store extra fields (bio, profile
    picture) without touching the core auth table.

• **v1.0 – 2025-06-16**
  – Initial commit with a completely custom "User" model
    (commented-out in this version).

"""

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
   <-- Manual Way
    Manual may, but Django provides a User class that is built in
    class User(models.Model):  #<-- Manual Way

	name = models.CharField(max_length=200, null=False)
	email = models.EmailField(max_length=500, unique=True, null=False)
	phone_number = models.CharField(max_length=10, unique=True)
	is_active = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
"""

class TimeStamp(models.Model): # <---django user model doesnot have any timestamp field
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class UserProfile(TimeStamp):

	default_profile_pic_url = ""

	"""user = models.ForeignKey(User, null=False, on_delete=models.CASCADE) # <-- Manual Way"""

	user = models.OneToOneField(User,on_delete=models.CASCADE, null=False)

	profile_pic_url = models.CharField(max_length=500, default=default_profile_pic_url)

	bio = models.CharField(max_length=10000, blank=True)

	is_verified = models.BooleanField(default=True)





