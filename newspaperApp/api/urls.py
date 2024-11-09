from django.urls import path
from .import views

urlpatterns = [
    # Urls to interact with users model
    path('users/',views.users_list,name='user_list'),
    path('users/create',views.add_user,name='add_user'),
    path('users/<int:pk>',views.users_record,name='user_record'),

    # Urls to interact with authors model
    path('authors/',views.author_list,name='author_list'),
    path('authors/create',views.create_author,name='add_author'),
    path('authors/<int:pk>',views.authors_record,name='author_record')
]