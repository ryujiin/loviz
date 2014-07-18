# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Producto'
        db.create_table(u'catalogo_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=120, unique=True, null=True, blank=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(default='Loviz DelCarpio', max_length=120)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Categoria'], null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['util.Color'], null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('meta_descripcion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['Producto'])

        # Adding M2M table for field parientes on 'Producto'
        m2m_table_name = db.shorten_name(u'catalogo_producto_parientes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_producto', models.ForeignKey(orm[u'catalogo.producto'], null=False)),
            ('to_producto', models.ForeignKey(orm[u'catalogo.producto'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_producto_id', 'to_producto_id'])

        # Adding model 'Categoria'
        db.create_table(u'catalogo_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=120)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=250, null=True, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('padre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Categoria'], null=True, blank=True)),
            ('meta_descripcion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('meta_keyword', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('posicion', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'catalogo', ['Categoria'])

        # Adding M2M table for field hijos on 'Categoria'
        m2m_table_name = db.shorten_name(u'catalogo_categoria_hijos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_categoria', models.ForeignKey(orm[u'catalogo.categoria'], null=False)),
            ('to_categoria', models.ForeignKey(orm[u'catalogo.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_categoria_id', 'to_categoria_id'])

        # Adding model 'ProductoImagen'
        db.create_table(u'catalogo_productoimagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imagenes_producto', to=orm['catalogo.Producto'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('actualizado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('orden', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('thum', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('thum_small', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('thum_medio', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['ProductoImagen'])

        # Adding model 'ProductoVariacion'
        db.create_table(u'catalogo_productovariacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Producto'])),
            ('talla', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['util.Talla'])),
            ('precio_variante', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=10, decimal_places=2)),
            ('oferta_variante', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('stock', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'catalogo', ['ProductoVariacion'])


    def backwards(self, orm):
        # Deleting model 'Producto'
        db.delete_table(u'catalogo_producto')

        # Removing M2M table for field parientes on 'Producto'
        db.delete_table(db.shorten_name(u'catalogo_producto_parientes'))

        # Deleting model 'Categoria'
        db.delete_table(u'catalogo_categoria')

        # Removing M2M table for field hijos on 'Categoria'
        db.delete_table(db.shorten_name(u'catalogo_categoria_hijos'))

        # Deleting model 'ProductoImagen'
        db.delete_table(u'catalogo_productoimagen')

        # Deleting model 'ProductoVariacion'
        db.delete_table(u'catalogo_productovariacion')


    models = {
        u'catalogo.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'hijos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hijos_rel_+'", 'null': 'True', 'to': u"orm['catalogo.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'padre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Categoria']", 'null': 'True', 'blank': 'True'}),
            'posicion': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120'})
        },
        u'catalogo.producto': {
            'Meta': {'object_name': 'Producto'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Categoria']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.Color']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'default': "'Loviz DelCarpio'", 'max_length': '120'}),
            'meta_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '120', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'parientes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'parientes_rel_+'", 'null': 'True', 'to': u"orm['catalogo.Producto']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'catalogo.productoimagen': {
            'Meta': {'object_name': 'ProductoImagen'},
            'actualizado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imagenes_producto'", 'to': u"orm['catalogo.Producto']"}),
            'thum': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'thum_medio': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'thum_small': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'catalogo.productovariacion': {
            'Meta': {'object_name': 'ProductoVariacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oferta_variante': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'precio_variante': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Producto']"}),
            'stock': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'talla': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.Talla']"})
        },
        u'util.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'util.talla': {
            'Meta': {'object_name': 'Talla'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['catalogo']