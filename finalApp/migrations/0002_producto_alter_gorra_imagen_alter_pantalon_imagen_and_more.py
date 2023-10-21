# Generated by Django 4.2.6 on 2023-10-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='productos/')),
            ],
        ),
        migrations.AlterField(
            model_name='gorra',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='pantalon',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='remera',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
