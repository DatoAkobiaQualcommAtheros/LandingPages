from rest_framework import viewsets

from users.models import User
from users.serializer import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        print("qs")
        print(User.objects.all())
        return User.objects.all()
