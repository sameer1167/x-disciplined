from rest_framework import viewsets
from .models import Users

from .permissions import CustomPermissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [CustomPermissions]

    def get_queryset(self):
        # If the user is staff, they can see all records.
        if self.request.user.is_staff:
            return Users.objects.all()
        # Regular users only see their own record.
        return Users.objects.filter(id=self.request.user.id)
