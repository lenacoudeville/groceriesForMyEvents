# Generated by Django 2.0.7 on 2018-08-03 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myGroceries', '0004_auto_20180803_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='id_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myGroceries.Event'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitprod',
            name='id_invit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myGroceries.Invitation'),
        ),
        migrations.AlterField(
            model_name='invitprod',
            name='id_prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myGroceries.Product'),
        ),
    ]
