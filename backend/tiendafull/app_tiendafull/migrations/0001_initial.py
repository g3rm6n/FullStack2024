# Generated by Django 4.2 on 2024-05-18 17:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('nro_documento', models.IntegerField()),
                ('telefono', models.CharField(blank=True, max_length=45, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BrandType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoMarca',
                'verbose_name_plural': 'TipoMarcas',
                'db_table': 'tipo_marca',
            },
        ),
        migrations.CreateModel(
            name='ColorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoColor',
                'verbose_name_plural': 'TiposColor',
                'db_table': 'tipo_color',
            },
        ),
        migrations.CreateModel(
            name='DeliveryStatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoEstadoEntrega',
                'verbose_name_plural': 'TipoEstadoEntregas',
                'db_table': 'tipo_estado_entrega',
            },
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoMaterial',
                'verbose_name_plural': 'TiposMateriales',
                'db_table': 'tipo_material',
            },
        ),
        migrations.CreateModel(
            name='PaymentModeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoModoPago',
                'verbose_name_plural': 'TiposModoPago',
                'db_table': 'tipo_modo_pago',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=45)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('imagen', models.CharField(blank=True, max_length=200, null=True)),
                ('detalle', models.TextField(blank=True, max_length=500, null=True)),
                ('id_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.colortype')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_factura', models.IntegerField()),
                ('fecha', models.DateField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_modo_pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.paymentmodetype')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compra',
            },
        ),
        migrations.CreateModel(
            name='StyleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoEstilo',
                'verbose_name_plural': 'TiposEstilo',
                'db_table': 'tipo_estilo',
            },
        ),
        migrations.CreateModel(
            name='WheelSizeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'TipoRodado',
                'verbose_name_plural': 'TiposRodado',
                'db_table': 'tipo_rodado',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tiendafull.purchase')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tiendafull.product')),
            ],
            options={
                'verbose_name': 'DetalleCompra',
                'verbose_name_plural': 'DetallesCompra',
                'db_table': 'detalle_compra',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='id_estilo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.styletype'),
        ),
        migrations.AddField(
            model_name='product',
            name='id_marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.brandtype'),
        ),
        migrations.AddField(
            model_name='product',
            name='id_material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.materialtype'),
        ),
        migrations.AddField(
            model_name='product',
            name='id_rodado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.wheelsizetype'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_seguimiento', models.CharField(max_length=45)),
                ('domicilio_entrega', models.CharField(max_length=200)),
                ('fecha_estimada', models.DateField()),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('compra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_tiendafull.purchase')),
                ('id_estado_entrega', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tiendafull.deliverystatustype')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
                'db_table': 'entrega',
            },
        ),
    ]
