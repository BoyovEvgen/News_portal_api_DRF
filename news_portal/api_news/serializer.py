from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'date_joined', 'is_active', 'last_login']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'parent')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'post', 'image', 'is_main')

    # def validate(self, data):
    #     if data['is_main']:
    #         post = data['post']
    #         if PostImage.objects.filter(post=post, is_main=True).exists():
    #             raise serializers.ValidationError("Only one main image allowed per post.")
    #     return data


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    images = ImageSerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'categories', 'images', 'author', 'created_at', 'updated_at']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'categories']
