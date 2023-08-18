from rest_framework import serializers
from .models import *

class CoursesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Courses
        fields=('__all__')

class UploadCoursesSerializer(serializers.ModelSerializer):
    # Teacher=serializers.SerializerMethodField()
    course=serializers.StringRelatedField(read_only=True)

    class Meta:
        model=UploadVideoCourses
        fields=('__all__')

    # def get_Teacher(self,obj):
    #     result=obj.Qu.all()
    #     return CoursesSerializer(instance=result,many=True).data

class SingleVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model=SingleVideo
        fields=('__all__')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=('__all__')



    



