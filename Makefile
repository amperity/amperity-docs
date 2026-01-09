BUILDDIR = build
BUILD_COMMAND = .venv/bin/python -m sphinx -b html --jobs auto -W

all: deps base user operator api reference guides amp360 ampiq contributing tooltips modals legacy

static:
	cp -vr downloads $(BUILDDIR)/

base: static ## Build only the "/user" section
	# Building base pages...
	$(BUILD_COMMAND) amperity_base/source $(BUILDDIR)/

user: static ## Build only the "/user" section
	# Building User Guides pages...
	$(BUILD_COMMAND) amperity_user/source $(BUILDDIR)/user

operator: static ## Build only the "/operator" section
	# Building Operators Guide pages...
	$(BUILD_COMMAND) amperity_operator/source $(BUILDDIR)/operator

api: static ## Build only the "/api" section
	# Building Amperity API pages...
	$(BUILD_COMMAND) amperity_api/source $(BUILDDIR)/api

reference: static ## Build only the "/reference" section
	# Building A-Z Reference pages...
	$(BUILD_COMMAND) amperity_reference/source $(BUILDDIR)/reference

guides: static ## Build only the "/guides" section
	# Building A-Z Reference pages...
	$(BUILD_COMMAND) amperity_guides/source $(BUILDDIR)/guides

amp360: static ## Build only the "/amp360" section
	# Building redirects for Amp360 pages...
	$(BUILD_COMMAND) amperity_amp360/source $(BUILDDIR)/amp360

ampiq: static ## Build only the "/ampiq" section
	# Building redirects for AmpIQ pages...
	$(BUILD_COMMAND) amperity_ampiq/source $(BUILDDIR)/ampiq

contributing: static ## Build only the "/contributing" section
	# Building redirects for Contributing pages...
	$(BUILD_COMMAND) contributing/source $(BUILDDIR)/contributing

tooltips: static ## Build only the "/tooltips" section
	# Building tooltips pages...
	$(BUILD_COMMAND) amperity_help/source $(BUILDDIR)/tooltips

modals: static ## Build only the "/modals" section
	# Building destination modal pages...
	$(BUILD_COMMAND) amperity_modals/source $(BUILDDIR)/modals

legacy: static ## Build only the "/legacy" section
	# Building Legacy pages...
	$(BUILD_COMMAND) legacy/source $(BUILDDIR)/legacy

clean: ## Flush the entire build directory
	# Cleaning out build directory...
	@rm -rf $(BUILDDIR)
	# Cleaning out .venv directory...
	@rm -rf .venv

deps: ## Create a Python virtualenv and install dependencies.
	python3 -m venv .venv
	.venv/bin/pip install --quiet -r requirements.txt

render:
	$(BUILD_COMMAND)

serve: all ## Build and serve the docs from a local HTTP server.
	# Serving docs on http://localhost:8080 ...
	.venv/bin/python -m http.server --directory build --bind localhost 8080

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1|\3/p' \
		| column -t  -s '|'
