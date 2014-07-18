Loviz.Views.Ubigeo = Backbone.View.extend({
	events: {
	},
	initialize : function () {
		this.template = swig.compile( $('#optiones').html() );
	},
	render : function () {
		var data = this.model.toJSON();
		var html = this.template(data);
		this.$el.html( html );
	},
});