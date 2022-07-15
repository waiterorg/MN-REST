# Generated by Django 4.0.6 on 2022-07-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=150, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='ادرس دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(default=0, verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, verbose_name='عنوان محصول')),
                ('price', models.FloatField(verbose_name='قیمت')),
                ('upc', models.CharField(help_text='این فیلد باید پر شود, حداکثر 12 کلمه', max_length=12, unique=True, verbose_name='کد محصول')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='items_image', verbose_name='تصویر محصول')),
                ('production_date', models.DateTimeField(verbose_name='تاریخ تولید')),
                ('status', models.BooleanField(default=False, verbose_name='فعال باشد؟')),
                ('category', models.ManyToManyField(max_length=100, related_name='items', to='core.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'محصول موبایل',
                'verbose_name_plural': 'محصولات موبایل',
            },
        ),
    ]
