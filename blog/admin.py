from django.contrib import admin
from .models import Post
from .models import Comments

admin.site.register(Post)
admin.site.register(Comments)

# Register your models here.
