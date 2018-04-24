# Generated by Django 2.0.4 on 2018-04-24 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0008_auto_20180423_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='weekly_entry_id',
        ),
        migrations.AddField(
            model_name='insight',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.MonthlyEntry'),
        ),
        migrations.AddField(
            model_name='lookingforwardto',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.DailyEntry'),
        ),
        migrations.AddField(
            model_name='monthlygoal',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.MonthlyEntry'),
        ),
        migrations.AddField(
            model_name='obstacle',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.MonthlyEntry'),
        ),
        migrations.AddField(
            model_name='project',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.WeeklyEntry'),
        ),
        migrations.AddField(
            model_name='thankfulfor',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.DailyEntry'),
        ),
        migrations.AddField(
            model_name='weeklygoal',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notebook.WeeklyEntry'),
        ),
    ]