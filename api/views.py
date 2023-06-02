from rest_framework.response import Response
from rest_framework.views import APIView, status
from api.serializer import TarefaSerializer ,UserSerializer
from api.models import Tarefa
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

    
class CriarTarefas(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tarefas = Tarefa.objects.filter(usuario=request.user) #filtragem pelo usuario
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['usuario'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 



from django.http import Http404



class TarefasDeletarAtualizar(APIView):

    permission_classes = [IsAuthenticated]

    def get_tarefa(self, pk, usuario):
        try:
            return Tarefa.objects.get(pk=pk, usuario=usuario)
        except Tarefa.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tarefa = self.get_tarefa(pk, request.user)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = self.get_tarefa(pk, request.user)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_tarefa(pk, request.user)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


class UserSignup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    