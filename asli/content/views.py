from typing import Any
from django import http
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from .forms import *
from .serializers import *
# DRF imports...
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser
# Create your views here.

class HomeView(View):
    form_class=SearchHomeForm
    template_name='content/home.html'

    def get(self,request):
        courses=Courses.objects.all()
        parts=SingleVideo.objects.all()
        articles=Article.objects.all()
        if request.GET.get('search'):
            courses=courses.filter(title__contains=request.GET['search'])
        return render(
            request,self.template_name,
            {
                'courses':courses,
                'parts':parts,
                'articles':articles,
                'form':self.form_class
            }
        )
    
class DetailCourseView(View):
    form_class=CommentForm
    template_name='content/detail_course.html'

    def get(self,request,pk):
        course=Courses.objects.get(id=pk)
        videos=UploadVideoCourses.objects.filter(course=pk)
        comments=Comment.objects.filter(is_sub=False,course=pk)
        return render(request,self.template_name,{'course':course,'videos':videos,'form':self.form_class,'comments':comments})
    
    def post(self,request,pk):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            now=form.save(commit=False)
            now.user=request.user
            now.course=Courses.objects.get(id=pk)
            now.save()
            return redirect('home')
        return render(request,self.template_name,{'form':form})

class UploadCourseView(View):
    template_name='content/upload_course.html'

    def get(self,request,pk):
        cours=UploadVideoCourses.objects.get(id=pk)
        return render(request,self.template_name,{'cours':cours})
    
class UpdateCommentView(View):
    from_class=UpdateCommentForm
    template_name='content/update_comment.html'
    
    def setup(self, request, *args, **kwargs):
        self.coment_ins=Comment.objects.get(id=kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        com=self.coment_ins
        if not com.user == request.user:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,pk):
        comment_user=self.coment_ins
        form=self.from_class(instance=comment_user)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,pk):
        comment_user=self.coment_ins
        form=self.from_class(request.POST,instance=comment_user)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            form.save()
            return redirect('home')
        return render(request,self.template_name,{'form':form})
    
class DeleteCommentView(View):

    def setup(self, request, *args, **kwargs):
        self.comment_ins=Comment.objects.get(id=kwargs['pk'])
        return super().setup(request, *args, **kwargs)
    
    def get(self,request,pk):
        comment_user=self.comment_ins
        if comment_user.user == request.user:
            comment_user.delete()
            return redirect('home')
        else:
            return redirect('home')
        
class ListCourseView(View):
    form_class=SearchListCoursesForm
    template_name='content/list_course.html'

    def get(self,request):
        courses=Courses.objects.all()
        if request.GET.get('search'):
            courses=courses.filter(title__contains=request.GET['search'])
        return render(request,self.template_name,{'courses':courses,'form':self.form_class})
    
class ListSingleVideoView(View):
    form_class=SearchListSingleVideoForm
    template_name='content/list_single.html'

    def get(self,request,pk=None):
        parts=SingleVideo.objects.all()
        if pk:
            tag=Tag.objects.get(id=pk)
            parts=parts.filter(tag=tag)
        return render(request,self.template_name,{'parts':parts,'form':self.form_class})
    
class DetailSingleVideoView(View):
    template_name='content/detail_single.html'

    def get(self,request,pk):
        video=SingleVideo.objects.get(id=pk)
        return render(request,self.template_name,{'video':video})


class ListArticleView(View):
    form_class=SearchListArticleForm
    template_name='content/list_article.html'

    def get(self,request,pk=None):
        articles=Article.objects.all()
        if request.GET.get('search'):
            articles=articles.filter(title__contains=request.GET['search'])
        if pk:
            tag=ArticleTag.objects.get(id=pk)
            articles=articles.filter(tag=tag)
        return render(request,self.template_name,{'articles':articles,'form':self.form_class})

class DetailArticleView(View):
    template_name='content/detail_article.html'

    def get(self,request,pk):
        article=Article.objects.get(id=pk)
        return render(request,self.template_name,{'article':article})
# Start Apis....
    
class ListCoursesAPIView(APIView):
    """
        Hello World...
    """
    serializer_class=CoursesSerializer
    permission_classes=(IsAdminUser,)
    throttle_scope=('scop')

    def get(self,request):
       queryset=Courses.objects.all()
       srz_data=self.serializer_class(instance=queryset,many=True)
       return Response(data=srz_data.data) 

class RetrieveCoursesAPIView(APIView):
    serializer_class=CoursesSerializer

    def get(self,request,pk):
       queryset=Courses.objects.get(id=pk)
       srz_data=self.serializer_class(instance=queryset)
       return Response(data=srz_data.data) 
    
class UpdateCoursesAPIView(APIView):
    serializer_class=CoursesSerializer

    def put(self,request,pk):
       queryset=Courses.objects.get(id=pk)
       srz_data=self.serializer_class(instance=queryset,data=request.POST,partial=True)
       if srz_data.is_valid():
           vd=srz_data.validated_data
           srz_data.save()
           return Response(data=srz_data.data)
       return Response(srz_data.errors)
    
class DeleteCoursesAPIView(APIView):

    def get(self,request,pk):
        queryset=Courses.objects.get(id=pk)
        queryset.delete()
        return Response({'massage':'Course Deleted...'})
    
class ListUploadCoursesAPIView(APIView):
    serializer_class=UploadCoursesSerializer

    def get(self,request):
        queryset=UploadVideoCourses.objects.all()
        srz_data=self.serializer_class(instance=queryset,many=True)
        return Response(data=srz_data.data)
    
class RetrieveUploadCoursesAPIView(APIView):
    serializer_class=UploadCoursesSerializer

    def get(self,request,pk):
        queryset=UploadVideoCourses.objects.get(id=pk)
        srz_data=self.serializer_class(instance=queryset)
        return Response(data=srz_data.data)
    
class UpdateUploadCoursesAPIView(APIView):
    serializer_class=UploadCoursesSerializer

    def put(self,request,pk):
        queryset=UploadVideoCourses.objects.get(id=pk)
        srz_data=self.serializer_class(instance=queryset,data=request.POST,partial=True)
        if srz_data.is_valid():
            vd=srz_data.validated_data
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)
    
class DeleteUploadCoursesAPIView(APIView):

    def get(self,request,pk):
        queryset=UploadVideoCourses.objects.get(id=pk)
        queryset.delete()
        return Response({'massage':'video Deleted'})
    
class List_Create_SingleVideoAPIView(ListCreateAPIView):
    queryset=SingleVideo.objects.all()
    serializer_class=SingleVideoSerializer

class RUD_SingleVideoAPIView(RetrieveUpdateDestroyAPIView):
    queryset=SingleVideo.objects.all()
    serializer_class=SingleVideoSerializer

class ViewSet_CRUD_Article(viewsets.ViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

    def list(self, request):
        srz_data=self.serializer_class(instance=self.queryset,many=True)
        return Response(srz_data.data)

    def create(self, request):
        srz_data=self.serializer_class(data=request.POST)
        if srz_data.is_valid():
            vd=srz_data.validated_data
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)

    def retrieve(self, request, pk=None):
        queryset=self.queryset.get(id=pk)
        srz_data=self.serializer_class(instance=queryset)
        return Response(data=srz_data.data)
    
    def partial_update(self, request, pk=None):
        queryset=self.queryset.get(id=pk)
        srz_data=self.serializer_class(instance=queryset,data=request.POST,partial=True)
        if srz_data.is_valid():
            vd=srz_data.validated_data
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(srz_data.errors)

    def destroy(self, request, pk=None):
        queryset=self.queryset.get(id=pk)
        queryset.delete()
        return Response({'massage':'Article Deleted...'})
    

    


    

