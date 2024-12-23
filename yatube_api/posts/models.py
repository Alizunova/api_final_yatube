from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(max_length=30)
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="posts/", null=True, blank=True)

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = "posts"

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=30)
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        default_related_name = "comments"

    def __str__(self):
        return f"Комментарий от {self.author} к посту {self.post}"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name="follower",
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_followers"
            ),
        ]

    def __str__(self):
        return f"На пользователя {self.user} подписаны {self.following}"
