Loviz.Routers.Base = Backbone.Router.extend({
	routes : {
		"" : "root",
		"catalogo/producto/:slug" : "productoSingle"
	},

	root : function () {
		console.log("Estamos en el root de nuesta applicacion");

		window.app.state = "root";
		window.app.categoria = null;

	},
	productoSingle : function(slug){
		console.log(slug);

		window.app.state = "productoSingle";
		window.app.categoria = slug;
	},
});