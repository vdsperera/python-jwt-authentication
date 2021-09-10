from django.urls import path
from .views import UsersView

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('users/register/', UsersView.as_view()),
#     path('users/login/', UsersView.as_view()),
#     path('users/logout/', UsersView.as_view()),
# ]


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users/register/', UsersView.as_view({'post': 'register'}), name = 'UsersView'),
    path('users/login/', UsersView.as_view({'post': 'login'}), name = 'UsersView'),
    path('users/', UsersView.as_view({'get': 'get_user'}), name = 'UsersView'),
    path('users/logout/', UsersView.as_view({'get': 'logout'}), name = 'UsersView'),
]


# print('vvvvvvvvvvvvvvvv')

# print(str(path('users/logout', UsersView.as_view())))

# print('aaaaaaaaaaaaaaaaa')

