Loviz.Views.Checkout = Backbone.View.extend({
	events: {
		'change .regionselct' : 'buscarProvincia',
		'change .proviselct' : 'buscarDistrito',
		'click .form_caja .metodo-pago' : 'mostrarMetodo',
	},
	initialize : function ($el) {
		this.$el = $el;

		$('.acordeon').accordion();
	},
	render : function () {
	},
	buscarProvincia : function (e) {
		$('.proviselct').empty();
		var valor = e.target.value
		if (valor!=='') {
			var provincias = new Loviz.Collections.Ubigeo();
			provincias.url = '/ubigeo/provincia/json/?region_id='+valor;
			provincias.on('add', function (model) {
				var modelo = model.toJSON();
				var option = '<option value="'+modelo.pk+'">'+modelo.fields.name+'</option>'
				$('.proviselct').append(option)
			});
			provincias.fetch();
		};
	},
	buscarDistrito : function (e) {
		$('.distrselect').empty();
		var valor = e.target.value
		if (valor!=='') {
			var provincias = new Loviz.Collections.Ubigeo();
			provincias.url = '/ubigeo/distrito/json/?province_id='+valor;
			provincias.on('add', function (model) {
				var modelo = model.toJSON();
				var option = '<option value="'+modelo.pk+'">'+modelo.fields.name+'</option>'
				$('.distrselect').append(option)
			});
			provincias.fetch();
		};
	},
	mostrarMetodo :  function (e) {
		console.log(e);
		var div = e.currentTarget.nextElementSibling;
		$(div).toggleClass('oculto');
		debugger;
	}
});