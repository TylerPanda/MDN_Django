# Generated by Django 2.0.7 on 2018-08-02 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_book_bookinstance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='authur',
            new_name='author',
        ),
    ]