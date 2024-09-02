from . import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    # path('detail/',views.detail,name='detail'),
    path('delete/<int:todotaskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TodoListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TodoDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TodoUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TodoDeleteView.as_view(),name='cbvdelete'),
]