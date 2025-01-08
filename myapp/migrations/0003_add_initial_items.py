from django.db import migrations


def forward_func(apps, schema_editor):
    Item = apps.get_model('myapp', 'Item')

    Item.objects.bulk_create([
        Item(name='Item 1', description='Описание для первого элемента'),
        Item(name='Item 2', description='Описание для второго элемента'),
        Item(name='Item 3', description='Описание для третьего элемента'),
    ])


def reverse_func(apps, schema_editor):
    Item = apps.get_model('myapp', 'Item')
    Item.objects.filter(name__in=['Item 1', 'Item 2', 'Item 3'])


class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0002_add_items')
    ]

    operations = [
        migrations.RunPython(forward_func, reverse_func),
    ]