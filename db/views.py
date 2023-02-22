from rest_framework import status, generics, permissions, authentication, views
from rest_framework.response import Response
from .serializers import CreateTodoSerializer

# Create your views here.
class CreateTodo(generics.GenericAPIView):
    serializer_class = CreateTodoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
            "Value" : "Created"
            })
        return Response({"Error": "Invalid Values"}, status=400)
