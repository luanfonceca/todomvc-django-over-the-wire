
from rest_framework.generics import UpdateAPIView

from todos.models import ToDo
from api.serializers import ToggleToDoSerializer


class ToggleToDo(UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToggleToDoSerializer
