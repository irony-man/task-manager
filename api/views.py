from distutils import ccompiler
from symbol import return_stmt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

'''
# created without decorators
@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# created with decorators
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    try:
        article = Articles.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class based
class ArticleAPIView(APIView):
    authentication_classes = (TokenAuthentication) 
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

# class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Articles.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, req):
#         return self.list(req)

#     def post(self, req):
#         return self.create(req)

# class ArticleDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Articles.objects.all()
#     serializer_class = ArticleSerializer

#     lookup_field = 'id'

#     def get(self, req, id):
#         return self.retrieve(req, id = id)

#     def put(self, req, id):
#         return self.update(req, id = id)

#     def delete(self, req, id):
#         return self.destroy(req, id = id)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# generic viewset class
# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

# model viewset class

class ArticleViewSet(viewsets.ModelViewSet):
    # generic ans Model viewset
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication, )

    # normal view set

    # def list(self, req):
    #     return self.list(req)

    # def create(self, req):
    #     return self.create(req)

    # def retrieve(self, req, id):
    #     return self.retrieve(req, id = id)

    # def update(self, req, id):
    #     return self.update(req, id = id)

    # def destroy(self, req, id):
    #     return self.destroy(req, id = id)




    # def list(self, req):
    #     articles = Articles.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # def create(self, request):
    #     data = JSONParser().parse(request)
    #     serializer = ArticleSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, id=None):
    #     try:
    #         article = Articles.objects.get(id=id)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)

    # def update(self, request, id=None):
    #     try:
    #         article = Articles.objects.get(id=id)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = ArticleSerializer(article, request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    # def destroy(self, request, id=None):
    #     try:
    #         article = Articles.objects.get(id=id)
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)