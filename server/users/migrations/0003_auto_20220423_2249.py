# Generated by Django 3.1.7 on 2022-04-23 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.CharField(blank=True, default='https://firebasestorage.googleapis.com/v0/b/top-cubist-344010.appspot.com/o/files%2Ficon-students-3.jpg?alt=media&token=69e9185d-846d-429b-a078-e21c51cc21ae%22', max_length=200, null=True),
        ),
    ]
