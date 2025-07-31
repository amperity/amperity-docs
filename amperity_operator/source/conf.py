import os
import sys
import shibuya

# for example source
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "example_code"))

project = "Operators Guide"
#copyright = "Copyright &copy; 2025, Amperity"
#author = "Amperity"

#version = shibuya.shibuya_version
#release = version

extensions = [
    "sphinx.ext.autodoc",
#    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.video",
    "sphinxcontrib.youtube",
]
todo_include_todos = True
#jupyter_sphinx_thebelab_config = {
#    'requestKernel': True,
#}
#jupyter_sphinx_require_url = ''
#nbsphinx_requirejs_path = ''
sitemap_excludes = ['404/']

extlinks = {
#    'pull': ('https://github.com/lepture/shibuya/pull/%s', 'pull request #%s'),
#    'issue': ('https://github.com/lepture/shibuya/issues/%s', 'issue #%s'),
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#intersphinx_mapping = {
#    "python": ("https://docs.python.org/3", None),
#    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
#    "numpy": ("https://numpy.org/devdocs/", None),
#}

templates_path = ["_templates"]
html_static_path = ["_static"]
html_extra_path = ["_public"]
html_css_files = [
    "custom.css",
    "shibuya.css",
]
html_title = "Amperity"
html_theme = "shibuya"
#html_theme_path = ['../../_themes/']
html_baseurl = "https://docs.amperity.com/"
sitemap_url_scheme = "operator/{link}"

html_copy_source = False
html_show_sourcelink = False

html_additional_pages = {
#    "branding": "branding.html",
}

if os.getenv('USE_DOCSEARCH'):
    extensions.append("sphinx_docsearch")
    docsearch_app_id = "3RU4IG0D1E"
    docsearch_api_key = "ec63fbf7ade2fa535b0b82c86e7d1463"
    docsearch_index_name = "shibuya-lepture"

if os.getenv("TRIM_HTML_SUFFIX"):
    html_link_suffix = ""

html_favicon = "_static/icon-light.svg"

html_theme_options = {
    "logo_target": "/",
    "light_logo": "_static/logo-light.png",
    "dark_logo": "_static/logo-dark.png",
    "accent_color": "violet",
#    "og_image_url": "https://shibuya.lepture.com/icon.png",
#    "twitter_creator": "lepture",
#    "twitter_site": "lepture",

#    "discussion_url": "https://amperity-docs.discourse.group/",
#    "twitter_url": "https://amperity.com",
#    "github_url": "https://github.com/amperity/amperity-docs",

#    "carbon_ads_code": "CE7DKK3W",
#    "carbon_ads_placement": "shibuya",

    "globaltoc_expand_depth": 1,
    "toctree_collapse": "collapse",
    "nav_links": [
        {
            "title": "Guides",
            "children": [
                {
                    "title": "Users",
                    "url": "../user/index",
                    "summary": "Audiences, campaigns, journeys, activations."
                },
                {
                    "title": "Operators",
                    "url": "../operator/index",
                    "summary": "Configuration, SQL queries, analytics, databases."
                },
            ]
        },
        {
            "title": "APIs",
            "children": [
                {
                    "title": "Amperity API",
                    "url": "../api/overview",
                    "summary": "Programmatic access to your Amperity tenant."
                },
                {
                    "title": "Profile API",
                    "url": "../operator/api_profile",
                    "summary": "Endpoints for unified customer profiles."
                },
                {
                    "title": "Streaming API",
                    "url": "../operator/api_streaming",
                    "summary": "Stream from external systems in real-time."
                },
            ]
        },
        {
            "title": "Connections",
            "children": [
                {
                    "title": "Amperity Bridge",
                    "url": "../operator/grid_bridge",
                    "summary": "Share data directly with data warehouses."
                },
                {
                    "title": "Campaigns",
                    "url": "../operator/grid_campaigns",
                    "summary": "Send audiences to marketing workflows."
                },
                {
                    "title": "Destinations",
                    "url": "../operator/grid_destinations",
                    "summary": "Send data to any downstream system."
                },
                {
                    "title": "Offline events",
                    "url": "../operator/grid_events",
                    "summary": "Measure marketing efforts across channels."
                },
                {
                    "title": "Sources",
                    "url": "../sources",
                    "summary": "Pull data from any upstream system."
                },
            ]
        },
        {
            "title": "Reference",
            "url": "../reference/index",
        },
    ]
}

#if "READTHEDOCS" in os.environ:
#    html_context = {
#        "source_type": "github",
#        "source_user": "lepture",
#        "source_repo": "shibuya",
#    }
#    html_theme_options["carbon_ads_code"] = ""
#    html_theme_options["announcement"] = (
#        "This documentation is hosted on Read the Docs only for testing. Please use "
#        "<a href='https://shibuya.lepture.com/'>the main documentation</a> instead."
#    )
#else:
html_context = {
#    "source_type": "github",
#    "source_user": "amperity",
#    "source_repo": "amperity-docs",
#        "buysellads_code": "CE7DKK3M",
#        "buysellads_placement": "shibuya",
#        "buysellads_container_selector": ".yue > section > section",
#    "github_path": "https://github.com/amperity/amperity-docs/tree/main/amperity_operator/source/", # Path in the checkout to the docs root
}


#DEBUG_RTD = False

#if DEBUG_RTD:
#    os.environ['READTHEDOCS_PROJECT'] = 'shibuya'
#    html_context["DEBUG_READTHEDOCS"] = True
#    html_theme_options["carbon_ads_code"] = None

# A string of files with substitutions.
rst_prolog = """
.. include:: ../../tokens/external_links.txt
.. include:: ../../tokens/fivetran_party.txt
.. include:: ../../tokens/internal_links.txt
.. include:: ../../tokens/names.txt
.. include:: ../../tokens/unicode.txt
"""
