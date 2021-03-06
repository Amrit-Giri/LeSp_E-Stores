# Generated by Django 4.0.4 on 2022-06-17 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_brand_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('EA', 'Electronic Accessories')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
