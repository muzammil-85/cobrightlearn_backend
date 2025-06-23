from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from common.mixin import CustomResponseMixin
from .models import RecordedClass
from .serializers import RecordedClassSerializer

class RecordedClassViewSet(CustomResponseMixin, viewsets.ModelViewSet):
    queryset = RecordedClass.objects.all()
    serializer_class = RecordedClassSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return self.custom_response(data=serializer.data)
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=500)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return self.custom_response(data=serializer.data)
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=404)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.custom_response(data=serializer.data, status_code=status.HTTP_201_CREATED)
        err_msg = next(iter(serializer.errors.values()))[0]
        return self.custom_response(success=False, err_msg=err_msg, status_code=400)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return self.custom_response(data=serializer.data)
        err_msg = next(iter(serializer.errors.values()))[0]
        return self.custom_response(success=False, err_msg=err_msg, status_code=400)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return self.custom_response(data="Deleted successfully")
        except Exception as e:
            return self.custom_response(success=False, err_msg=str(e), status_code=400)
