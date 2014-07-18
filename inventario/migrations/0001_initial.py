# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Materiales'
        db.create_table(u'inventario_materiales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['util.TipoMaterial'], null=True, blank=True)),
            ('unidad_compra', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inventario', ['Materiales'])

        # Adding model 'Firme'
        db.create_table(u'inventario_firme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['util.TipoFirme'])),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['util.Color'])),
            ('talla', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['util.Talla'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('cantidad', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('alarma', self.gf('django.db.models.fields.PositiveIntegerField')(default=20)),
        ))
        db.send_create_signal(u'inventario', ['Firme'])


    def backwards(self, orm):
        # Deleting model 'Materiales'
        db.delete_table(u'inventario_materiales')

        # Deleting model 'Firme'
        db.delete_table(u'inventario_firme')


    models = {
        u'inventario.firme': {
            'Meta': {'object_name': 'Firme'},
            'alarma': ('django.db.models.fields.PositiveIntegerField', [], {'default': '20'}),
            'cantidad': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.Color']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'talla': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.Talla']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.TipoFirme']"})
        },
        u'inventario.materiales': {
            'Meta': {'object_name': 'Materiales'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['util.TipoMaterial']", 'null': 'True', 'blank': 'True'}),
            'unidad_compra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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
        },
        u'util.tipofirme': {
            'Meta': {'object_name': 'TipoFirme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'util.tipomaterial': {
            'Meta': {'object_name': 'TipoMaterial'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['inventario']