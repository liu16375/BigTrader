# Generated by Django 3.1.6 on 2021-02-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rice', '0006_auto_20210208_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rice_sell_order',
            name='add',
            field=models.CharField(blank=True, max_length=32, verbose_name='收货地址'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='amount',
            field=models.IntegerField(blank=True, verbose_name='数量(斤)'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='buyer',
            field=models.CharField(blank=True, max_length=8, verbose_name='购买人'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='delivery',
            field=models.CharField(blank=True, max_length=8, verbose_name='收货人'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='delivery_co',
            field=models.CharField(blank=True, max_length=8, verbose_name='发货物流'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='delivery_fee',
            field=models.FloatField(blank=True, verbose_name='运费(元/斤)'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='mark',
            field=models.CharField(blank=True, max_length=32, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='package',
            field=models.FloatField(blank=True, verbose_name='件数(个)'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='收货人电话'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='price',
            field=models.FloatField(blank=True, verbose_name='单价(元)'),
        ),
        migrations.AlterField(
            model_name='rice_sell_order',
            name='sign_time',
            field=models.DateField(blank=True, verbose_name='签收日期'),
        ),
    ]