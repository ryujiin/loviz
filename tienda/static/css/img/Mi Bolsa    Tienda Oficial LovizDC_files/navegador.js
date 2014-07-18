Loviz.Views.Navegador = Backbone.View.extend({
	events: {
		'click .mobil-menu' : 'expandir',
		'click .menu-cates .glyphicon' : "expandir_interno",
	},
	initialize : function ($el) {
		this.$el = $el;
	},
	render : function () {
	},
	expandir : function () {
		$("#main-nav .menu").slideToggle("slow");
	},
	expandir_interno:function (clase) {
		var icono = clase.target
		var menu = "." + $(icono).data('clase') + ' .'+$(icono).data('nivel');
		$(icono).toggleClass('glyphicon-minus');
		$(menu).slideToggle("slow");
	}
});