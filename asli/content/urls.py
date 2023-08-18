from django.urls import path
from rest_framework import routers
from .import views

urlpatterns = [
    path('home/',views.HomeView.as_view(),name='home'),
    path('detail_course/<int:pk>/',views.DetailCourseView.as_view(),name='detail_course'),
    path('upload_course/<int:pk>/',views.UploadCourseView.as_view(),name='upload_course'),
    path('update_comment/<int:pk>/',views.UpdateCommentView.as_view(),name='update_comment'),
    path('delete_comment/<int:pk>/',views.DeleteCommentView.as_view(),name='delete_comment'),
    path('list_course/',views.ListCourseView.as_view(),name='list_course'),
    path('list_single_course/',views.ListSingleVideoView.as_view(),name='list_single_course'),
    path('detail_single_course/<int:pk>/',views.DetailSingleVideoView.as_view(),name='detail_single_course'),
    path('filter_tag/<int:pk>/',views.ListSingleVideoView.as_view(),name='filter_tag'),
    path('list_article/',views.ListArticleView.as_view(),name='list_article'),
    path('detail_article/<int:pk>/',views.DetailArticleView.as_view(),name='detail_article'),
    path('filter_tag_article/<int:pk>/',views.ListArticleView.as_view(),name='filter_tag_article'),
    # Api Urls..
    path('list_course_api/',views.ListCoursesAPIView.as_view(),name='list_course_api'),
    path('retrieve_course_api/<int:pk>/',views.RetrieveCoursesAPIView.as_view(),name='retrieve_course_api'),
    path('update_course_api/<int:pk>/',views.UpdateCoursesAPIView.as_view(),name='update_course_api'),
    path('delete_course_api/<int:pk>/',views.DeleteCoursesAPIView.as_view(),name='delete_course_api'),
    path('list_upload_course_api/',views.ListUploadCoursesAPIView.as_view(),name='list_upload_course_api'),
    path('retrieve_upload_course_api/<int:pk>/',views.RetrieveUploadCoursesAPIView.as_view(),name='retrieve_upload_course_api'),
    path('update_upload_course_api/<int:pk>/',views.UpdateUploadCoursesAPIView.as_view(),name='update_upload_course_api'),
    path('delete_upload_course_api/<int:pk>/',views.DeleteUploadCoursesAPIView.as_view(),name='delete_upload_course_api'),
    path('list_create_singlevideo_api/',views.List_Create_SingleVideoAPIView.as_view(),name='list_create_singlevideo_api'),
    path('rud_singlevideo_api/<int:pk>/',views.RUD_SingleVideoAPIView.as_view(),name='rud_singlevideo_api'),
]
router=routers.SimpleRouter()
router.register('vset',views.ViewSet_CRUD_Article)
urlpatterns += router.urls
