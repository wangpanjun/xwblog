from rest_framework import status
from labels.models import LabelModel
from labels.permissions import LabelPermission
from labels.serializers import LabelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class LabelsViewSet(GenericViewSet):

    queryset = LabelModel.objects.filter(flag=True).order_by('created_time')
    serializer_class = LabelSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LabelViewSet(GenericViewSet):
    permission_classes = [LabelPermission]

    def destroy(self, request, pk):
        label = get_object_or_404(LabelModel, id=pk)
        self.check_object_permissions(request, label)
        label.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
