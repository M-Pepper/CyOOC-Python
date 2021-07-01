3: 003_introduction.adoc Gemfile reveal.js .bundle
	@bundle exec asciidoctor-revealjs 003_introduction.adoc
	@google-chrome 003_introduction.html 1>/dev/null 2>&1 || true
	
Gemfile:
	@echo "source 'https://rubygems.org'" > Gemfile
	@echo "" >> Gemfile
	@echo "gem 'asciidoctor-revealjs'" >> Gemfile
	@echo "gem 'json'" >> Gemfile
	@echo "gem 'coderay'" >> Gemfile

.bundle:
	@bundle config --local github.https true 2>/dev/null || true
	@bundle --path=.bundle/gems --binstubs=.bundle/.bin

reveal.js:
	@git clone -b 3.3.0 --depth 1 https://github.com/hakimel/reveal.js.git 2>/dev/null || true

clean:
	@rm -rf *.html


