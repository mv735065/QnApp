from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView

urlpatterns = [
    path('', views.root_view, name='root'),
    path('question/list/', views.question_list, name='question_list'),
    path('home/', views.home, name='home'),

    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('tag/<str:tag_name>/', views.filter_by_tag, name='filter_by_tag'),
    
    path('question/create/', views.manage_question, name='create_question'),
    path('question/<int:pk>/edit/', views.manage_question, name='edit_question'),
    path('question/<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('question/<int:question_pk>/like/', views.like_question, name='like_question'),
    path('question/<int:question_pk>/unlike/', views.unlike_question, name='unlike_question'),

    path('question/<int:question_pk>/answer/', views.manage_answer, name='create_answer'),
    path('question/<int:question_pk>/answer/<int:answer_pk>/edit/', views.manage_answer, name='edit_answer'),
    path('question/<int:question_pk>/answer/<int:answer_pk>/delete/', views.delete_answer, name='delete_answer'),
    path('question/<int:question_pk>/answer/<int:answer_pk>/like/', views.like_answer, name='like_answer'),
    path('question/<int:question_pk>/answer/<int:answer_pk>/unlike/', views.unlike_answer, name='unlike_answer'),

    path('question/<int:question_pk>/comment/', views.create_comment, name='create_comment'),
    path('question/<int:question_pk>/answer/<int:answer_pk>/comment/', views.create_comment_answer, name='create_comment_answer'),

    path('like_comment/<int:question_pk>/<int:comment_pk>/', views.like_comment, name='like_comment'),
    path('unlike_comment/<int:question_pk>/<int:comment_pk>/', views.unlike_comment, name='unlike_comment'),

    path('like_comment/<int:question_pk>/<int:answer_pk>/<int:comment_pk>/',views.like_comment, name='like_comment_answer'),
    path('unlike_comment/<int:question_pk>/<int:answer_pk>/<int:comment_pk>/',views.unlike_comment, name='unlike_comment_answer'),

    path('question/<int:question_pk>/answer/<int:answer_pk>/allcomments',views.question_answer_comment,name='question_answer_comment'),
      
    path('delete_comment/<int:question_pk>/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:question_pk>/<int:comment_pk>/', views.edit_comment, name='edit_comment'),

    path('delete_comment/<int:question_pk>/<int:answer_pk>/<int:comment_pk>/',views.delete_comment, name='delete_comment_answer'),
    path('edit_comment/<int:question_pk>/<int:answer_pk>/<int:comment_pk>/',views.edit_comment, name='edit_comment_answer'),

    path('login/', views.custom_login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    
]
