from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(
        null=True, blank=True, verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="article_scopes",  # ← важно: не "scopes"
        verbose_name="Статья"
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tag_scopes",  # ← уникальное имя
        verbose_name="Тег"
    )
    is_main = models.BooleanField(default=False, verbose_name="Основной")

    class Meta:
        verbose_name = "Тематика статьи"
        verbose_name_plural = "Тематики статьи"
        ordering = ["-is_main", "tag__name"]  # сначала основной, потом по алфавиту

    def __str__(self):
        main = " [основной]" if self.is_main else ""
        return f"{self.article.title} — {self.tag.name}{main}"