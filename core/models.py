from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamp(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ModelManager(models.Manager):
    def filter_active_status(self):
        active = self.filter(status=True)
        return active


class Category(TimeStamp):
    """
    Category table
    """

    title = models.CharField(max_length=150, verbose_name=_("عنوان دسته بندی"))
    slug = models.SlugField(
        max_length=150, unique=True, verbose_name=_("ادرس دسته بندی")
    )
    status = models.BooleanField(
        default=True, verbose_name=_("آیا نمایش داده شود؟")
    )
    position = models.IntegerField(default=0, verbose_name=_("پوزیشن"))
    objects = ModelManager()

    class Meta:
        verbose_name = _("دسته بندی")
        verbose_name_plural = _("دسته بندی ها")
        ordering = ["position"]

    def __str__(self):
        return self.title


class Mobile(TimeStamp):
    """
    Mobile product table stored mobile items for sale
    """

    title = models.CharField(max_length=100, verbose_name=_("عنوان محصول"))
    price = models.FloatField(verbose_name=_("قیمت"))
    category = models.ManyToManyField(
        Category,
        max_length=100,
        related_name="items",
        verbose_name=_("دسته بندی"),
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("کد محصول"),
        help_text="این فیلد باید پر شود, حداکثر 12 کلمه",
    )
    description = models.TextField(verbose_name=_("توضیحات"))
    image = models.ImageField(
        upload_to="items_image", verbose_name=_("تصویر محصول")
    )
    production_date = models.DateField(verbose_name=_("تاریخ تولید"))
    status = models.BooleanField(default=False, verbose_name=_("فعال باشد؟"))
    objects = ModelManager()

    class Meta:
        verbose_name = _("محصول موبایل")
        verbose_name_plural = _("محصولات موبایل")

    def __str__(self):
        return self.title
