//Loviz Tienda
$(document).ready(function(){
	console.log('main.js loaded');
	window.views.tienda = new Loviz.Views.Tienda( $('body') );
	if ($('#checkout').length) {
		window.views.checkout = new Loviz.Views.Checkout( $('#checkout') );
	};

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
		if ($('#mi-bolsa').length) {
			total = new Loviz.Views.Carro({model:model});
			total.renderTotal();
		};
	});

	window.collections.lineas.on('add', function (model) {
		var linea = new Loviz.Views.LineaCarro({model:model});
		linea.renderCarrito();
		$('.lineas-carrito').prepend(linea.$el);
	});
	//sona de la bolsa
	
	//zona de chechout

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