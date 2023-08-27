from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, default="slug")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)

    @property
    def subcategories(self):
        return self.category_set.all()

    @property
    def posts(self):
        return Post.objects.filter(category=self, is_active=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    text = models.TextField()
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    @property
    def main_image(self):
        return PostImage.objects.filter(Q(post_id=self.id) & Q(is_main=True)).first().image

    @property
    def all_images(self):
        return PostImage.objects.filter(post_id=self.id).values_list('image', flat=True).order_by('-is_main')

    def __str__(self):
        return f"Post {self.title}, id: {self.id}"


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="uploads/img/posts/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image id: {self.id} for post id: {self.post}"
