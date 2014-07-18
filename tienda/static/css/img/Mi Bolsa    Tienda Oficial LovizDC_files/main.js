//Loviz Tienda
$(document).ready(function(){
	console.log('main.js loaded');
	window.views.navegador = new Loviz.Views.Navegador( $('#main-nav') );
	window.views.productoSingle = new Loviz.Views.ProductoSingle( $('#producto-single') );

	window.collections.carro = new Loviz.Collections.Carro();
	window.collections.lineas = new Loviz.Collections.Lineas();

	window.collections.carro.on('add', function (model) {
		// console.log('Se agrego un nuevo articulo', model.toJSON() );
		// Aqui agregaremos una vista para cada uno de nuesto articulos;
		carro = new Loviz.Views.Carro({model:model});
		carro.render();
		window.collections.lineas.fetch();
	});

	window.collections.lineas.on('add', function (model) {
		var linea = new Loviz.Views.LineaCarro({model:model});
		linea.renderCarrito();
		$('.lineas-carrito').prepend(linea.$el);
	});
	//sona de la bolsa
	if ($('#mi-bolsa').length) {
		window.views.listaLinea = new Loviz.Views.ListaLinea({
			collection : window.collections.lineas
		});
	};

	//Buscar Carro
	window.collections.carro.fetch();
	//Buscar Lineas
	//Envio de token
	$(document).ajaxSend(function(e, xhr, settings) {
		var csrf = $('input[name=csrfmiddlewaretoken]').val();
		xhr.setRequestHeader('X-CSRFToken', csrf);
	});

	window.routers.base = new Loviz.Routers.Base();
	Backbone.history.start({
		root : '/',
		pushState:true
	});

});