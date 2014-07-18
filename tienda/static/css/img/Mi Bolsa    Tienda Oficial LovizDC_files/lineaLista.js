Loviz.Views.ListaLinea = Backbone.View.extend({
	el:$('#mi-bolsa .lineas'),
	initialize : function () {
    	this.listenTo(this.collection, "add", this.addOne, this);
	},
	render : function () {
    	this.collection.forEach(this.addOne, this);
	},
	addOne : function (modelo) {
		var LineaCarro = new Loviz.Views.LineaCarro({ model: modelo });
    	this.$el.append(LineaCarro.renderBolsa().el);
	}
});