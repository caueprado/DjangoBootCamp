# Generated by Django 3.2.4 on 2021-06-04 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('data_contato', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=264, unique=True)),
                ('cidade', models.CharField(max_length=264, unique=True)),
                ('cep', models.CharField(max_length=9, unique=True)),
                ('estado', models.CharField(max_length=2, unique=True)),
                ('complemento', models.CharField(max_length=100, unique=True)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=256, unique=True)),
                ('titulo', models.CharField(max_length=256, unique=True)),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.diretor')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, unique=True)),
                ('nome_fantasia', models.CharField(max_length=256, unique=True)),
                ('cnpj', models.CharField(max_length=256, unique=True)),
                ('descricao', models.CharField(max_length=256, unique=True)),
                ('data_cadastro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=256, unique=True)),
                ('situacao', models.CharField(max_length=10)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.filme')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9, unique=True)),
                ('telefone', models.CharField(max_length=9, unique=True)),
                ('celular', models.CharField(max_length=9, unique=True)),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evolution_app.pessoa')),
            ],
            bases=('evolution_app.pessoa',),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='evolution_app.pessoa')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.funcionario')),
            ],
            bases=('evolution_app.pessoa',),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=256, unique=True)),
                ('numero', models.CharField(max_length=256, unique=True)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.contato')),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.filme')),
            ],
        ),
        migrations.AddField(
            model_name='contato',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.fornecedor'),
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('midia', models.ManyToManyField(to='evolution_app.Midia')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='MidiaCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('situacao', models.CharField(max_length=10)),
                ('data_pedido', models.DateField()),
                ('data_entrega', models.DateField()),
                ('quantidade', models.IntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.fornecedor')),
                ('midia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.midia')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256, unique=True)),
                ('tipo', models.CharField(max_length=256, unique=True)),
                ('data_nascimento', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evolution_app.cliente')),
            ],
        ),
    ]
