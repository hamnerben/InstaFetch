# Generated by Django 4.1.6 on 2023-03-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instafetch', '0003_alter_login_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.CharField(default='instafetch456', max_length=50),
            preserve_default=False,
        ),
    ]
