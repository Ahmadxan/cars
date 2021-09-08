from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


class BrandViewSet(ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandView(APIView):
    def get_object(self, pk):
        try:
            brand = models.Brand.objects.get(pk=pk)
            return brand
        except Exception:
            raise NotFound("Brand not found!")

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            brand = self.get_object(kwargs.get('pk'))
            serializer = serializers.BrandSerializer(brand, many=False)
        else:
            brands = models.Brand.objects.all()
            serializer = serializers.BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        brand = self.get_object(kwargs.get('pk'))
        serializer = serializers.BrandSerializer(data=request.data, instance=brand)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        brand = self.get_object(kwargs.get('pk'))
        brand.delete()
        return Response({"data": "deleted"})


class MadelViewSet(ModelViewSet):
    queryset = models.Madel.objects.all()
    serializer_class = serializers.MadelSerializer


class MadelView(APIView):
    def get_object(self, pk):
        try:
            brand = models.Madel.objects.get(pk=pk)
            return brand
        except Exception:
            raise NotFound("Madel not found!")

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            madel = self.get_object(kwargs.get('pk'))
            serializer = serializers.MadelSerializer(madel, many=False)
        else:
            madels = models.Madel.objects.all()
            serializer = serializers.MadelSerializer(madels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MadelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        madel = self.get_object(kwargs.get('pk'))
        serializer = serializers.MadelSerializer(data=request.data, instance=madel)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        madel = self.get_object(kwargs.get('pk'))
        madel.delete()
        return Response({"madel": "deleted"})