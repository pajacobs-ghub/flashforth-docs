# makefile for ASCIIdoc version of the FlashForth docs
# PJ 2021-12-30

HTML_FILES = elements-of-flashforth-5.html \
		ff5-tutorial-guide.html \
		ff5-quick-ref.html

WEB_REPO_DIR = $(HOME)/pajacobs-ghub.pajacobs-ghub.github.io/flashforth/

build-html : $(HTML_FILES)
	@echo "HTML files built"

elements-of-flashforth-5.html : elements-of-flashforth-5.adoc
	asciidoctor elements-of-flashforth-5.adoc

ff5-tutorial-guide.html : ff5-tutorial-guide.adoc
	asciidoctor ff5-tutorial-guide.adoc

ff5-quick-ref.html : ff5-quick-ref.adoc
	asciidoctor ff5-quick-ref.adoc

install : $(HTML_FILES)
	rsync -av $(HTML_FILES) $(WEB_REPO_DIR)

clean :
	- rm elements-of-flashforth-5.html
	- rm ff5-tutorial-guide.html
	- rm ff5-quick-ref.html
