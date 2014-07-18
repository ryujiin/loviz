Loviz.Views.Carro = Backbone.View.extend({
	events: {
		'click' : 'mostrarLineas',
		'click .checkout' : 'evitarslide'
	},
	initialize : function () {
		this.template = swig.compile( $('#carro_mini').html() );

    	this.listenTo(this.model, "change", this.render);
	},
	render : function () {
		var data = this.model.toJSON();
		data.total_carro = data.total_carro.toFixed(2);
		var html = this.template(data);
		this.$el.html( html );
		$('.mini-cart').append(this.$el);
	},
	mostrarLineas :function () {
		$('.checkout').fadeToggle('fast');
		$('.carrito_content').slideToggle("slow");
	},
	evitarslide : function (e) {
		e.stopPropagation();
	},

});