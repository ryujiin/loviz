# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Color'
        db.create_table(u'util_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'util', ['Color'])

        # Adding model 'Talla'
        db.create_table(u'util_talla', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'util', ['Talla'])

        # Adding model 'TipoFirme'
        db.create_table(u'util_tipofirme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'util', ['TipoFirme'])

        # Adding model 'TipoMaterial'
        db.create_table(u'util_tipomaterial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'util', ['TipoMaterial'])

        # Adding model 'TipoCorte'
        db.create_table(u'util_tipocorte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'util', ['TipoCorte'])


    def backwards(self, orm):
        # Deleting model 'Color'
        db.delete_table(u'util_color')

        # Deleting model 'Talla'
        db.delete_table(u'util_talla')

        # Deleting model 'TipoFirme'
        db.delete_table(u'util_tipofirme')

        # Deleting model 'TipoMaterial'
        db.delete_table(u'util_tipomaterial')

        # Deleting model 'TipoCorte'
        db.delete_table(u'util_tipocorte')


    models = {
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
        u'util.tipocorte': {
            'Meta': {'object_name': 'TipoCorte'},
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

    complete_apps = ['util']