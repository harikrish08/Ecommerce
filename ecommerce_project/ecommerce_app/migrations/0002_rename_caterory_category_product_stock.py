# Generated by Django 4.2.7 on 2023-12-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caterory',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
