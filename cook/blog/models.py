import django
from django.utils import timezone

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='categories/', default='categories/cat-1.jpg')
    parent = TreeForeignKey(
        'self',
        related_name='childrens',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    slug = models.SlugField(max_length=200, default='')

    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )

    tags = models.ManyToManyField(
        Tag,
        related_name='post'
    )
    time_prepare = models.PositiveIntegerField()
    time_cook = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_next_post(self):
        all_posts = Post.objects.all()
        current_slug_num = int(self.slug.split('_')[-1])
        for post in all_posts:
            if int(post.slug.split('_')[-1]) > current_slug_num:
                return post
        return self

    def get_prev_post(self):
        all_posts = Post.objects.all()
        current_slug_num = int(self.slug.split('_')[-1])
        for post in all_posts[::-1]:
            if int(post.slug.split('_')[-1]) < current_slug_num:
                return post
        return self

    def get_comments(self):
        return self.comments.all()

    def get_comments_number(self):
        count = self.comments.count()
        if count > 0:
            return f'{count} comment'
        return "No comments"


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    serves = models.CharField(max_length=50)
    cook_time = models.PositiveIntegerField(default=0)
    prep_time = models.PositiveIntegerField(default=0)
    ingredient_list = RichTextField()
    direction_list = RichTextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.SET_NULL,
        related_name='recipes',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    # number_of_likes = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )