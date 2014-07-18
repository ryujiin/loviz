# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UsoMaterial'
        db.create_table(u'produccion_usomaterial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Producto'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventario.Materiales'])),
            ('uso', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cant_par', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('cant_doc', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('costo_doc', self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'produccion', ['UsoMaterial'])


    def backwards(self, orm):
        # Deleting model 'UsoMaterial'
        db.delete_table(u'produccion_usomaterial')


    models = {
        u'catalogo.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'hijos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hijos_rel_+'", 'null': 'True', 'to': u"orm['catalogo.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'meta_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'meta_keyword': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '120', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'parientes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'parientes_rel_+'", 'null': 'True', 'to': u"orm['catalogo.Producto']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'inventario.materiales': {
            'Meta': {'object_name': 'Materiales'},
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.Color']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.TipoMaterial']", 'null': 'True', 'blank': 'True'}),
            'unidad_compra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'produccion.usomaterial': {
            'Meta': {'object_name': 'UsoMaterial'},
            'cant_doc': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'cant_par': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'costo_doc': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventario.Materiales']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Producto']"}),
            'uso': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'util.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'util.tipomaterial': {
            'Meta': {'object_name': 'TipoMaterial'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['produccion']