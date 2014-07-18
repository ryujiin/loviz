# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AtributoValor'
        db.create_table(u'catalogo_atributovalor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('atributo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Atributo'])),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'catalogo', ['AtributoValor'])

        # Adding model 'Atributo'
        db.create_table(u'catalogo_atributo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['Atributo'])


    def backwards(self, orm):
        # Deleting model 'AtributoValor'
        db.delete_table(u'catalogo_atributovalor')

        # Deleting model 'Atributo'
        db.delete_table(u'catalogo_atributo')


    models = {
        u'catalogo.atributo': {
            'Meta': {'object_name': 'Atributo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'catalogo.atributovalor': {
            'Meta': {'object_name': 'AtributoValor'},
            'atributo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Atributo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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