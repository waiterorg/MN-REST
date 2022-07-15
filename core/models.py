from django.db import models


class TimeStamp(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CategoryManager(models.Manager):
    def filter_active_category(self):
        active = self.filter(status=True)
        return active


class Category(TimeStamp):
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


class ItemManager(models.Manager):
    def filter_active_status(self):
        return self.filter(status=True)


class Product(TimeStamp):
    """
    Product table stored items for sale
    """

    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ManyToManyField(
        Category, max_length=100, related_name="items"
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name="کد محصول",
        help_text="این فیلد باید پر شود, حداکثر 12 کلمه",
    )
    description = models.TextField()
    image = models.ImageField(upload_to="items_image")
    production_date = models.DateTimeField(verbose_name="تاریخ تولید")
    status = models.BooleanField(default=False)
    objects = ItemManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title
