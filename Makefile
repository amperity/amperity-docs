BUILDDIR = build
BUILD_COMMAND = python3.9 -m sphinx -b html --jobs auto -W
BUILD_HELP_COMMAND = python3.9 -m sphinx -b text --jobs auto -W

all: base user operator api reference amp360 ampiq contributing tooltips modals legacy llmkb

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
