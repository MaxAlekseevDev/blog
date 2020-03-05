from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_ROLES = [
    ('a', 'Author'),
    ('r', 'Reader'),
    ('g', 'Anonymous')
]

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email  = models.EmailField()
    is_auth = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.CharField(max_length=1, choices=STATUS_ROLES, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    @property
    def get_posts(self):
        Post.objects.filter(category__title=self.title).count()


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="Other")
    image = models.ImageField(upload_to='media/')
    pub_date = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')