Loviz.Views.LineaCarro = Backbone.View.extend({
	className : 'linea',

	template : swig.compile( $('#linea_modal').html() ),

	templateCarrito : swig.compile( $('#linea_carrito').html()),

	templateBolsa : swig.compile( $('#linea_bolsa').html() ),

	initialize : function () {
    	this.listenTo(this.model, "change", this.render);
	},
	render : function () {
		var data = this.model.toJSON();
		var html = this.template(data);
		this.$el.html( html );
		return this;
	},
	renderCarrito : function () {
		var data = this.model.toJSON();
		data.precio = data.precio.toFixed(2);
		var html = this.templateCarrito(data);
		this.$el.html( html );
	},
	renderBolsa :function () {
		var data = this.model.toJSON();
		data.precio = data.precio.toFixed(2);
		data.total_linea = data.total_linea.toFixed(2);		
		var html = this.templateBolsa(data);
		this.$el.html( html );
		return this;
	}
});