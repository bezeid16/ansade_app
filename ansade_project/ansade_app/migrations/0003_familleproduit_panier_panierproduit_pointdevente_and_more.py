# Generated by Django 4.2.8 on 2023-12-27 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansade_app', '0002_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilleProduit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PanierProduit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ponderation', models.FloatField()),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansade_app.panier')),
            ],
        ),
        migrations.CreateModel(
            name='PointDeVente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('wilaya', models.TextField()),
                ('moughtaa', models.TextField()),
                ('commune', models.TextField()),
                ('gps_lat', models.FloatField()),
                ('gps_long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('point_de_vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansade_app.pointdevente')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.TextField()),
                ('price_unit', models.TextField()),
                ('code', models.TextField()),
                ('famille_produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansade_app.familleproduit')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductFamily',
        ),
        migrations.AddField(
            model_name='price',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansade_app.produit'),
        ),
        migrations.AddField(
            model_name='panierproduit',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ansade_app.price'),
        ),
    ]