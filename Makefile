BUILDDIR = build
BUILD_COMMAND = sphinx-build -b html -W
BUILD_HELP_COMMAND = sphinx-build -b text -W

all: base ampiq amp360 datagrid reference api support internal help

static:
	cp -vr downloads $(BUILDDIR)/

base: static ## Build the root topic collection
	# Building amperity_base/source...
	$(BUILD_COMMAND) amperity_base/source $(BUILDDIR)/

ampiq: static ## Build the /ampiq topic collection
	# Building amperity_ampiq/source...
	$(BUILD_COMMAND) amperity_ampiq/source $(BUILDDIR)/ampiq

amp360: static ## Build the /amp360 topic collection
	# Building amperity_amp360/source...
	$(BUILD_COMMAND) amperity_amp360/source $(BUILDDIR)/amp360

datagrid: static ## Build only the "/datagrid" section
	# Building amperity_datagrid/source...
	$(BUILD_COMMAND) amperity_datagrid/source $(BUILDDIR)/datagrid

reference: static ## Build only the "/reference" section
	# Building amperity_reference/source...
	$(BUILD_COMMAND) amperity_reference/source $(BUILDDIR)/reference

api: static ## Build only the "/api" section
	# Building amperity_api/source...
	$(BUILD_COMMAND) amperity_api/source $(BUILDDIR)/api

support: static ## Build only the "/support" section
	# Building amperity_support/source...
	$(BUILD_COMMAND) amperity_support/source $(BUILDDIR)/support

help: static ## Build only the "/help" section
	# Building amperity_help/source...
	$(BUILD_HELP_COMMAND) amperity_help/source $(BUILDDIR)/help

internal: static ## Build only the "/internal" section
	# Building amperity_internal/source...
	$(BUILD_COMMAND) amperity_internal/source $(BUILDDIR)/internal

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
