from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginReg),
    path('process_reg', views.process_reg),
    path('process_login', views.process_login),
    path('index', views.index),
    path('new_message', views.new_message),
    path('wall', views.display_new_message),
    path('new_comment', views.new_comment),
    path('<int:message_id>/delete_message', views.delete_message),
    # path('<int:comment_id>/delete_comment', views.delete_comment),
    path('log_out', views.log_out)
]
