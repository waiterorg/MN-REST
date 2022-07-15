from django.db import models


class CategoryManager(models.Manager):
    def filter_active_category(self):
        active = self.filter(status=True)
        return active


class Category(models.Model):
    """
    Category table for product table
    """

    title = models.CharField(max_length=150, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(
        max_length=150, unique=True, verbose_name="ادرس دسته بندی"
    )
    status = models.BooleanField(
        default=True, verbose_name="آیا نمایش داده شود؟"
    )
    position = models.IntegerField(default=0, verbose_name="پوزیشن")
    objects = CategoryManager()

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["position"]

    def __str__(self):
        return self.title
