import os
import sys
import shibuya

project = "Real-time APIs"
#copyright = "Copyright &copy; 2026, Amperity"
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
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.video",
    "sphinxcontrib.youtube",
    "sphinx_new_tab_link",
]
todo_include_todos = False

sitemap_excludes = ['404/']

extlinks = {
#    'pull': ('https://github.com/amperity/amperity-docs/pull/%s', 'pull request #%s'),
#    'issue': ('https://github.com/amperity/amperity-docs/issues/%s', 'issue #%s'),
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

templates_path = ["_templates"]
html_static_path = ["_static"]
html_extra_path = ["_public"]
html_css_files = [
    "custom.css",
    "shibuya.css",
]
html_title = "Real-time APIs"
html_theme = "shibuya"
html_baseurl = "https://docs.amperity.com/realtime/"
sitemap_url_scheme = "{link}"

html_copy_source = False
html_show_sourcelink = False

html_additional_pages = {
    'openapi-events':     'openapi-events.html',
    'openapi-profile-v3': 'openapi-profile-v3.html',
}

# Config for sphinx_new_tab_link extension
new_tab_link_show_external_link_icon = False
new_tab_link_enable_referrer = False

html_favicon = "_static/icon-light.svg"

html_theme_options = {
    "logo_target": "/",
    "light_logo": "_static/logo-light.png",
    "dark_logo": "_static/logo-dark.png",
    "accent_color": "violet",
    "globaltoc_expand_depth": 1,
    "toctree_collapse": "collapse",
    "nav_links": [
        {
            "title": "Guides",
            "children": [
                {
                    "title": "Guided setup",
                    "url": "../guides/index",
                    "summary": "Guided setup for profiles and identity resolution."
                },
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
                    "title": "Profile API v2",
                    "url": "../api/endpoint_get_profile",
                    "summary": "Batched profile lookup and enrichment."
                },
                {
                    "title": "Real-time Events API",
                    "url": "../realtime/overview",
                    "summary": "Real-time, single-profile events stream."
                },
                {
                    "title": "Real-time Profiles API",
                    "url": "../realtime/overview",
                    "summary": "Real-time profile lookups."
                },
                {
                    "title": "Streaming API",
                    "url": "../operator/api_streaming",
                    "summary": "High-volume event streaming."
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
                    "title": "Events",
                    "url": "../operator/grid_events",
                    "summary": "Measure marketing efforts across channels."
                },
                {
                    "title": "Sources",
                    "url": "../operator/sources",
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

html_context = {
}

# A string of files with substitutions.
rst_prolog = """
.. include:: ../../tokens/external_links.txt
.. include:: ../../tokens/fivetran_party.txt
.. include:: ../../tokens/internal_links.txt
.. include:: ../../tokens/names.txt
.. include:: ../../tokens/unicode.txt
"""
