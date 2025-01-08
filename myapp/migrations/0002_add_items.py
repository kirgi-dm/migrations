from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial')
    ]

    operations = [
        migrations.RunSQL(
            sql="INSERT INTO myapp_item (name, description) VALUES ('Название 1', 'Описание для названия 1');",
            reverse_sql="DELETE FROM myapp_item WHERE name='Название 1';",
        ),
        migrations.RunSQL(
            sql="INSERT INTO myapp_item (name, description) VALUES ('Название 2', 'Описание для названия 2');",
            reverse_sql="DELETE FROM myapp_item WHERE name='Название 2';",
        ),
    ]
