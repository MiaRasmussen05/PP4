# Generated by Django 3.2.18 on 2023-04-26 17:05

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('title', models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('item', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(4)])),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('saved', models.ManyToManyField(blank=True, related_name='save_shop', to=settings.AUTH_USER_MODEL)),
                ('shop_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='blog.shopcategory')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('rating', models.PositiveIntegerField(choices=[(0, '0 stars'), (1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
