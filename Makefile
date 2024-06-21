BUILDDIR = build
BUILD_COMMAND = sphinx-build -b html -W
BUILD_HELP_COMMAND = sphinx-build -b text -W

all: base ampiq amp360 datagrid reference api contributing

static:
	cp -vr downloads $(BUILDDIR)/

base: static ## Build Amperity Documentation
	# Building amperity_base/source...
	$(BUILD_COMMAND) amperity_base/source $(BUILDDIR)/

ampiq: static ## Build the /ampiq topic collection
	# Building User Guides for AmpIQ pages...
	$(BUILD_COMMAND) amperity_ampiq/source $(BUILDDIR)/ampiq

amp360: static ## Build the /amp360 topic collection
	# Building User Guides for Amp360 pages...
	$(BUILD_COMMAND) amperity_amp360/source $(BUILDDIR)/amp360

datagrid: static ## Build only the "/datagrid" section
	# Building Configuration Guide pages...
	$(BUILD_COMMAND) amperity_datagrid/source $(BUILDDIR)/datagrid

reference: static ## Build only the "/reference" section
	# Building A-Z Reference pages...
	$(BUILD_COMMAND) amperity_reference/source $(BUILDDIR)/reference

api: static ## Build only the "/api" section
	# Building Amperity API pages...
	$(BUILD_COMMAND) amperity_api/source $(BUILDDIR)/api

contributing: static ## Build only the "/contributing" section
	# Building Contributing pages...
	$(BUILD_COMMAND) contributing/source $(BUILDDIR)/contributing

clean: ## Flush the entire build directory
	# Cleaning out build directory...
	@rm -rf $(BUILDDIR)

serve: ## Start up a server on http://locahost:8080
	serve -dir build
	open http://localhost:8080

dependencies: ## Install all the required dependencies. You must have Homebrew installed first
	brew install python
	pip3 install -r requirements.txt
	brew install serve

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1|\3/p' \
		| column -t  -s '|'
