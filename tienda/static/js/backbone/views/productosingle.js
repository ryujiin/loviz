Loviz.Views.ProductoSingle = Backbone.View.extend({
	events: {
		'change #productoID': 'cambiarproducto',
		'change #talla': 'variacionproducto',
		'click #add-cart' : 'agregarcarro',
		'mouseover #add-cart' : 'seleccionatalla',
		'mouseleave #add-cart' : 'seleccionatalla',
	},
	initialize : function ($el) {
		this.$el = $el;
	},
	render : function () {
	},
	cambiarproducto:function (e) {
		var slug = $('#productoID option:selected').data('slug')
		var id = $('#productoID option:selected').val()
		if (slug !== null) {
			window.location.href = "/catalogo/producto/"+slug+"_"+id;
		};
		console.log(slug)
	},
	variacionproducto:function () {
		var clase = $('#talla option:selected').val()
		clase = '.'+clase;
		$('#producto-single .price-box .visible').removeClass('visible').addClass('oculto');
		$(clase).removeClass('oculto').addClass('visible');
	},
	agregarcarro: function () {
		//obtengo datos
		var talla = $('#talla option:selected').val();
		if (talla ==='sintalla') {
			return false
		};
		var carrito = carro.model.get('id');
		var producto = $('#productoID option:selected').val();
		var variacion = $('#talla option:selected').val();
		var precio = $('#talla option:selected').data('precio');
		var data = {
	        "carro": carrito, 
	        "producto": producto, 
	        "variacion": variacion, 
	        "cantidad": 1,
		};
		var modelo = new Loviz.Models.LineaCarro(data);
		if (modelo.save()) {
			var vistaLinea = new Loviz.Views.LineaCarro({model:modelo});
			vistaLinea.render();
			$('#modal_minicarrito .modal-body').append(vistaLinea.$el);

			//Comienza a modificar datos del carro
			var items = carro.model.get('num_items')+1;
			var total = (parseFloat(carro.model.get('total_carro'))*100+precio*100)/100;

			carro.model.set({num_items : items,total_carro : total});
			$('#modal_minicarrito').modal();
			$('#modal_minicarrito').on('hidden.bs.modal', function (e) {
				vistaLinea.$el.hide();
				window.collections.lineas.reset();
				window.collections.lineas.fetch();
			});
		}else{
			alert('Error al compra, porfavor intentelo mas tarde o comuniquese con el administrador');
		};
	},
	seleccionatalla:function (argument) {
		var talla = $('#talla option:selected').val();
		if (talla ==='sintalla') {
			$('#talla').toggleClass('caja_advertencia');
		};
	},
});