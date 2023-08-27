
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializer import *
from .models import User, Post, PostImage
from .pagination import CustomSetPagination


class UserApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomSetPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegisterSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class UserApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserApiDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


class PostsByCategoryApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    pagination_class = CustomSetPagination

    def get_queryset(self):
        slug_category = self.kwargs['slug_category']
        return Post.objects.filter(categories__slug=slug_category, is_active=True)


class PostApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomSetPagination
    permission_classes = (IsAdminOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class PostUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.get_serializer_class()(*args, **kwargs)


class PostDeleteApiView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ImageApiView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = PostImage.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ImageDeleteApiView(generics.DestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = PostImage.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAdminOrReadOnly,)
