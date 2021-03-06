# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Producto.categorias'
        db.delete_column(u'catalogo_producto', 'categorias_id')

        # Adding M2M table for field categorias on 'Producto'
        m2m_table_name = db.shorten_name(u'catalogo_producto_categorias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('producto', models.ForeignKey(orm[u'catalogo.producto'], null=False)),
            ('categoria', models.ForeignKey(orm[u'catalogo.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['producto_id', 'categoria_id'])


    def backwards(self, orm):
        # Adding field 'Producto.categorias'
        db.add_column(u'catalogo_producto', 'categorias',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Categoria'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field categorias on 'Producto'
        db.delete_table(db.shorten_name(u'catalogo_producto_categorias'))


    models = {
        u'catalogo.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'meta_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'padre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Categoria']", 'null': 'True', 'blank': 'True'}),
            'posicion': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120'})
        },
        u'catalogo.producto': {
            'Meta': {'object_name': 'Producto'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['catalogo.Categoria']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.Color']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'meta_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'nombre_mostrar': ('django.db.models.fields.CharField', [], {'max_length': '120', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'oferta': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'precio_minorista': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Producto']"}),
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