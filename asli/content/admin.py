from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Courses)
admin.site.register(UploadVideoCourses)
admin.site.register(Comment)
admin.site.register(SingleVideo)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(ArticleTag)