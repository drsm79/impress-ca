function app_load(scripts, base) {
  for (var i=0; i < scripts.length; i++) {
    document.write('<script src="'+ base + '/' + scripts[i]+'"><\/script>');
  };
};

app_load([
    "vendor/jqueryui/jquery-1.6.2.min.js",
    "vendor/jqueryui/jquery-ui-1.8.16.custom.min.js",
    "vendor/underscore/underscore-min.js",
    "vendor/backbone/backbone.js",
    "vendor/backbone.couch/js/jquery.couch.js?special",
    "vendor/backbone.couch/js/backbone.couch.js",
    "vendor/pagedown/Markdown.Converter.js",
    "js/impress.js"
  ], "/talk/_design/impress-ca/");
