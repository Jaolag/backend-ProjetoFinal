from django.urls import path
from . import views

from api.views import TarefasDeletarAtualizar, CriarTarefas, UserSignup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatters = [
    
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_login_refresh'),
    path('signup/', UserSignup.as_view(), name='Create_new_User'),
    path('tarefas', CriarTarefas.as_view(), name='CriarTarefas'),
    path('tarefas/<int:pk>', TarefasDeletarAtualizar.as_view(),
         name='TarefasDeletarAtualizar')
]