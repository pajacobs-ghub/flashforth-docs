# makefile for ASCIIdoc version of the FlashForth docs
# PJ 2021-12-30

build-html : elements-of-flashforth-5.html ff5-tutorial-guide.html
	@echo "HTML files built"

elements-of-flashforth-5.html : elements-of-flashforth-5.adoc
	asciidoctor elements-of-flashforth-5.adoc

ff5-tutorial-guide.html : ff5-tutorial-guide.adoc
	asciidoctor ff5-tutorial-guide.adoc

clean :
	- rm elements-of-flashforth-5.html
	- rm ff5-tutorial-guide.html
