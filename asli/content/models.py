from django.db import models
from accounts.models import User
# Create your models here.

class Courses(models.Model):
    STATUS_COURSE=(
        ('تکمیل','تکمیل'),
        ('imperfect','درحال ظبط'),
    
    )

    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='images/')
    teacher=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=STATUS_COURSE,default='تکمیل',verbose_name="وضعیت دوره")
    price=models.IntegerField()
    caption=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    
class UploadVideoCourses(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='Qu')
    number=models.CharField(max_length=100,null=True,blank=True)
    video=models.FileField(upload_to='videos/')

    def __str__(self) -> str:
        return self.course.teacher

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ucoment')
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='ccoment')
    sub=models.ForeignKey('self',on_delete=models.CASCADE,related_name='scoment',null=True,blank=True)
    is_sub=models.BooleanField(default=False)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} Commented... {self.course}'
    
class Tag(models.Model):
    title=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
class SingleVideo(models.Model):
    tag=models.ManyToManyField(Tag,related_name='tags',null=True,blank=True)
    title=models.CharField(max_length=255)
    auther=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    video=models.FileField(upload_to='singlevideos/')
    img=models.ImageField(upload_to='images/',null=True,blank=True)
    body=models.TextField()

    def __str__(self) -> str:
        return self.title

class ArticleTag(models.Model):
    title=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Article(models.Model):
    tag=models.ManyToManyField(ArticleTag,related_name='aticletag',null=True,blank=True)
    title=models.CharField(max_length=255)
    img=models.ImageField(upload_to='images/')
    auther=models.CharField(max_length=255)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title