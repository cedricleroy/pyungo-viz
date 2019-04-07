build:
	npm install
	rm -R static/jslibs
	mkdir static/jslibs
	cp node_modules/jquery/dist/jquery.min.js static/jslibs/
	cp node_modules/lodash/lodash.min.js static/jslibs/
	cp node_modules/graphlib/dist/graphlib.core.min.js static/jslibs/
	cp node_modules/dagre/dist/dagre.core.min.js static/jslibs/
	cp node_modules/d3/build/d3.min.js static/jslibs/
	cp node_modules/dagre-d3/dist/dagre-d3.core.min.js static/jslibs/
