BUILDDIR = build
BUILD_COMMAND = python3.9 -m sphinx -b html --jobs auto -W
BUILD_HELP_COMMAND = python3.9 -m sphinx -b text --jobs auto -W

all: base ampiq amp360 datagrid operator reference api tooltips modals contributing legacy llmkb

static:
	cp -vr downloads $(BUILDDIR)/

base: static ## Build Amperity Documentation
	# Building amperity_base/source...
	$(BUILD_COMMAND) amperity_base/source $(BUILDDIR)/

ampiq: static ## Build the /ampiq topic collection
	# Building User Guides for Marketers...
	$(BUILD_COMMAND) amperity_ampiq/source $(BUILDDIR)/ampiq

amp360: static ## Build the /amp360 topic collection
	# Building User Guides for Analysts...
	$(BUILD_COMMAND) amperity_amp360/source $(BUILDDIR)/amp360

datagrid: static ## Build only the "/datagrid" section
	# Building Operators Guide pages...
	$(BUILD_COMMAND) amperity_datagrid/source $(BUILDDIR)/datagrid

operator: static ## Build only the "/operator" section
	# Building Operators Guide pages...
	$(BUILD_COMMAND) amperity_operator/source $(BUILDDIR)/operator

reference: static ## Build only the "/reference" section
	# Building A-Z Reference pages...
	$(BUILD_COMMAND) amperity_reference/source $(BUILDDIR)/reference

api: static ## Build only the "/api" section
	# Building Amperity API pages...
	$(BUILD_COMMAND) amperity_api/source $(BUILDDIR)/api

tooltips: static ## Build only the "/tooltips" section
	# Building tooltips pages...
	$(BUILD_COMMAND) amperity_help/source $(BUILDDIR)/tooltips

modals: static ## Build only the "/modals" section
	# Building destination modal pages...
	$(BUILD_COMMAND) amperity_modals/source $(BUILDDIR)/modals

contributing: static ## Build only the "/contributing" section
	# Building Contributing pages...
	$(BUILD_COMMAND) contributing/source $(BUILDDIR)/contributing

legacy: static ## Build only the "/llm_kb" section
	# Building Legacy pages...
	$(BUILD_COMMAND) legacy/source $(BUILDDIR)/legacy

llmkb: static ## Build only the "/legacy" section
	# Building Legacy pages...
	$(BUILD_COMMAND) llm_kb/source $(BUILDDIR)/llmkb

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
