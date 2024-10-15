# README

This repository contains the source files for Amperity documentation (https://docs.amperity.com). This site hosts all business user, tenant operator, and API documentation for the Amperity customer data platform.

If you'd like to help improve the documentation you can:

1. Build the documentation locally
1. Report an issue
1. Request an update
1. Suggest changes

## Quick start

To build the documentation locally you'll need to install Sphinx, which is the static site generator used to build Amperity documentation. Local development requires Sphinx, a minimum version of Python, and a small collection of Python libraries, Sphinx extensions, and a makefile.

To report issues, request updates, or suggest changes without using local development, use the Edit in GitHub link located in the upper right on every Amperity documentation page to open that page in the Amperity documentation repository on GitHub.

From that page you may:

1. Report an issue
1. Request an update
1. Suggest changes

### Quick start using a Python Virtual Environment
1. Clone the docs git repository
2. Install serve if you don't have it by running ```brew install serve```
3. Run ```python3 -m venv amperity-docs``` to create a new virtual env in the docs repository
4. Navigate to the new virtual env and enable it by running ```cd amperity-docs && source bin/active```
5. Install requirements by running ```pip install -r requirements.txt```

This will keep all of the python requirements isolated to the virtual environment. If you ever have any issues with the repo delete the repository folder and re-run these instructions. 
