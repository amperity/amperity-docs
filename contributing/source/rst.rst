.. 
.. https://docs.amperity.com/internal/
..


==================================================
Formatting guide
==================================================

.. TODO: The HTML codes from this page https://www.toptal.com/designers/htmlarrows/arrows/ can be used in the nav-docs file inline with the TOC elements. Which can be useful.

This is the formatting guide for |rst| as it may be used with |theme|.

* :ref:`format-content-admonitions`
* :ref:`format-content-card-walls-inline`
* :ref:`format-content-code-blocks`
* :ref:`format-content-fontawesome`
* :ref:`Headers (Levels 1-4) <format-content-header-h1>`
* :ref:`format-content-images`
* :ref:`format-content-includes`
* :ref:`format-content-inline-markup`
* :ref:`format-content-links`
* :ref:`format-content-lists`
* :ref:`format-content-tables`
* :ref:`format-content-toctree`
* :ref:`format-content-tokens`
* :ref:`format-content-topic-title`
* :ref:`format-content-additional-resources`


.. _format-content-admonitions:

Admonitions
==================================================

.. format-content-admonitions-start

Admonitions are notes and warnings, and other types of alerts that give readers a visible way to identify certain types of content messages. Use notes and warnings often, the rest sparingly or only when you need them.

.. format-content-admonitions-end


.. _format-content-admonition-attention:

Attention
--------------------------------------------------

.. format-content-attention-start

Use ``.. attention::`` as shown here:

.. code-block:: rst

   .. attention:: The words for the attention itself.

to create an admonition like this:

.. attention:: The words for the attention itself.

.. format-content-attention-end


.. _format-content-admonition-caution:

Caution
--------------------------------------------------

.. format-content-caution-start

Use ``.. caution::`` as shown here:

.. code-block:: rst

   .. caution:: The words for the caution itself.

to create an admonition like this:

.. caution:: The words for the caution itself.

.. format-content-caution-end


.. _format-content-admonition-custom:

Custom admonitions
--------------------------------------------------

.. format-content-custom-start

|theme| uses the default admonition to enable the use of custom admonition titles. The default admonition is styled the same as a note.

For a custom admonition, use ``.. admonition:: some string`` as shown here:

.. code-block:: rst

   .. admonition:: Custom admonition title

      Contents of custom admonition.

Which will appear in the documentation like this:

.. admonition:: Custom admonition title

   Contents of custom admonition.

.. format-content-custom-end


.. _format-content-admonition-danger:

Danger
--------------------------------------------------

.. format-content-danger-start

Use ``.. danger::`` as shown here:

.. code-block:: rst

   .. danger:: The words for the danger itself.

to create an admonition like this:

.. danger:: The words for the danger itself.

.. format-content-danger-end


.. _format-content-admonition-error:

Error
--------------------------------------------------

.. format-content-error-start

Use ``.. error::`` as shown here:

.. code-block:: rst

   .. error:: The words for the error itself.

to create an admonition like this:

.. error:: The words for the error itself.

.. format-content-error-end


.. _format-content-admonition-hint:

Hint
--------------------------------------------------

.. format-content-hint-start

Use ``.. hint::`` as shown here:

.. code-block:: rst

   .. hint:: The words for the hint itself.

to create an admonition like this:

.. hint:: The words for the hint itself.

.. format-content-hint-end


.. _format-content-admonition-important:

Important
--------------------------------------------------

.. format-content-important-start

Use ``.. important::`` as shown here:

.. code-block:: rst

   .. important:: The words for the important itself.

to create an admonition like this:

.. important:: The words for the important itself.

.. format-content-important-end


.. _format-content-admonition-note:

Note
--------------------------------------------------

.. format-content-note-start

Use ``.. note::`` as shown here:

.. code-block:: rst

   .. note:: The words for the note itself.

to create an admonition like this:

.. note:: The words for the note itself.

.. format-content-note-end


.. _format-content-admonition-tip:

Tip
--------------------------------------------------

.. format-content-tip-start

Use ``.. tip::`` as shown here:

.. code-block:: rst

   .. tip:: The words for the tip itself.

to create an admonition like this:

.. tip:: The words for the tip itself.

.. format-content-tip-end


.. _format-content-admonition-warning:

Warning
--------------------------------------------------

.. format-content-warning-start

Use ``.. warning::`` as shown here:

.. code-block:: rst

   .. warning:: The words for the warning itself.

to create an admonition like this:

.. warning:: The words for the warning itself.

.. format-content-warning-end


.. _format-content-card-walls-inline:

Card walls, inline
==================================================

.. format-content-card-walls-inline-start

An inline card wall is a series of cards that show content groupings, such as on the main page of a docs site or on a marketing page that's full of links to resources.

.. important:: Inline card walls exist within the page and within the left- and right-side navigation. Use sparingly as occasionally. These are different from standalone card walls in that these are authored using reStructuredText container objects and can use all standard formatting options, whereas standalone card walls are written in HTML and do not have access to reStructuredText formatting.

A card may contain standard inline formatting (plain text, bold, italics, and so on, along with links to topics in other parts of the documentation collection). A card wall may be placed inline on a page. It may also be used as a index page, where the only contents on the index page are cards in the card wall.


.. container:: card-group

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Getting Started

         .. container:: card-wall-description

            The getting started guide is how to get started and learns you how to get started.

            Links for :ref:`le success <format-content-links>`.

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Deployment Guide

         .. container:: card-wall-description

            The deployment guide is the deployment guide and learns you how to deploy.

            Links for :ref:`le success <format-content-links>`.

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            User Guide

         .. container:: card-wall-description

            The user guide is the user guide and learns you how to user.

            Links for :ref:`le success <format-content-links>`.

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Admin Guide

         .. container:: card-wall-description

            The admin guide is the admin guide and learns you how to admin.

            Links for :ref:`le success <format-content-links>`.

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Reference

         .. container:: card-wall-description

            The reference guide is the reference guide and learns you how to reference.

            Links for :ref:`le success <format-content-links>`.


   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Diagrams

         .. container:: card-wall-description

            The diagrams guide is just a list of sweet diagrams.

            Links for :ref:`le success <format-content-links>`.

.. format-content-card-walls-inline-end


.. _format-content-card-walls-standalone:

Card walls, standalone
==================================================

.. format-content-card-walls-standalone-start

A standalone card wall is built using an HTML template that contains a block of HTML and associated CSS that builds a nice card wall that does not contain the left- or right-side navigation. Use a standalone card wall to present items in a scrolling list, either alphabetically or (in certain cases) in a specific order.

.. tip:: Look in the ``_templates/`` directory and review the ``cardwall.html`` file as a working example of how to build the card wall. Click the **Cardwall** link in the top navigation to see an example of a card wall.

.. format-content-card-walls-standalone-end


.. _format-content-card-walls-standalone-block:

Card wall block
--------------------------------------------------

.. format-content-card-walls-standalone-block-start

The entire block of content for the document body is replaced by this block of HTML and Jinja:

.. code-block:: none

   <div class="document markup-docs">
     {%- block document %}
       <div class="documentcardwrapper">
         <div class="cardwrapper">
           <div class="body" role="main">
             {% block body %}

             <div class="firstcard">...</div>

             <div class="cards">...</div>

             {% endblock %}
           </div>
         </div>
       </div>
     {% endblock %}
   </div>

.. format-content-card-walls-standalone-block-end


.. _format-content-card-walls-standalone-configure:

Configure card wall
--------------------------------------------------

.. format-content-card-walls-standalone-configure-start

To configure the card wall you have to tell the ``conf.py`` file which file in the ``_templates`` directory to use for the template, and then what the file name will be in the content directory. Find the following section:

.. code-block:: none

   # Additional templates that should be rendered to pages, maps page names to
   # template names.
   #    '404': '/internal/404.html',
   html_additional_pages = {
     'cardwall': 'cardwall.html',
   }

and then update the ``'cardwall': 'cardwall.html',`` pattern for the template name (on the left) and the webpage filename (on the right). For example, to use the cardwall template to build an HTML file named "sources.html", do the following:

.. code-block:: none

   html_additional_pages = {
     'cardwall': 'sources.html',
   }

.. format-content-card-walls-standalone-configure-end


.. _format-content-card-walls-standalone-first:

First cards
--------------------------------------------------

.. format-content-card-walls-standalone-first-start

You should use the first card pattern to introduce the card wall *or* to break the card wall into logical groups.

The block for first cards has different class names to allow for different styles, and then comments out the image used with the other card wall type. For example:

.. code-block:: none

   <div class="firstcard">
     <a href="destinations_reference.html" class="card"><div class="firstcard-item">
       <!--<div class="firstcard-image"><img id="markup" height="80" src="_static/connector-acxiom.svg"/>
       </div>-->
       <div class="firstcard-info">
         <h4 class="firstcard-title">About Card Walls</h4>
         <p class="firstcard-intro">A card wall is a template page that builds the top-level navigation, and then presents cards instead of pages. Use these to present lists of items as a visual, scrolling page.</p>
       </div>
     </div></a>
   </div>

Use this pattern as the first card in any card wall. This locates it in the top left of the page. The image in the first card is commented out. You *can* use an image in there. You will get more room for explanatory text without the image, but when the image is in there it is styled to be exactly the same as the information cards. Change the background color as appropriate. If you need different cards, update the styles in the main theme to support the variations.

.. tip:: You *could* use it as a "category card" and place more of them within the page to break a very long list of cards into some logical groups. Or you could define more than one block of cards, and then use the first card as the first card in each block. The cardwall example in the Amperity style guide shows using multiple "firstcard" cards in the card wall.

.. format-content-card-walls-standalone-first-end


.. _format-content-card-walls-standalone-information:

Information cards
--------------------------------------------------

Use the following pattern for all other cards in the card wall:

.. code-block:: none

   <div class="cards">
     <a href="style_guide.html" class="card"><div class="card-item">
       <div class="card-image"><img id="markup" height="80" src="_static/cardwall-placeholder.svg"/>
       </div>
       <div class="card-info">
         <h4 class="card-title">Lorem ipsum #1</h4>
         <p class="card-intro">All of these cards link to the style guide, but they could be linked to anything!</p>
       </div>
     </div></a>
   </div>

.. format-content-card-walls-standalone-end


.. _format-content-code-blocks:

Code blocks
==================================================

.. format-content-code-blocks-start

For code samples (Python, YAML, JSON, Jinja, config files, and so on) and for commands run via the command line that appear in the documentation we want to set them in code blocks using variations of the ``.. code-block::`` directive.

.. note:: Code block types in the |theme| are generalized. For example: the ``text`` type is used for general text files **including** configuration files and the ``sql`` type is used for general data tables. You may customize this to make them more specific and/or add more types to the code block styling options.

Code blocks are parsed using a tool called Pygments that checks the syntax in the named code block against the lexer in Pygments to help ensure that the structure of the code in the code block, even if it's pseudocode, is formatted correctly.

.. format-content-code-blocks-end

.. format-content-code-blocks-warning-start

.. warning:: Pygments lexers check the code in a code block against a lexer. A lexer checks the structure and syntax of the code in the code block. If this check doesn't pass, a Sphinx build may fail.

   For example, if a code block contains YAML and Jinja and is defined by a ``.. code-block:: yaml`` code block, the build will fail because Jinja templating is not YAML.

   Use a ``none`` code block to (temporarily or permanently) work around any problems you may have with rendering code blocks, as a none block is more forgiving.

.. format-content-code-blocks-warning-end


.. _format-content-code-block-line-emphasis:

Line emphasis
--------------------------------------------------

.. format-content-code-block-line-emphasis-start

Individual lines in a code block may be emphasized. The presentation is similar to a yellow highlight in a book. The following example shows how to highlight lines 3 and 5 in a code block:

.. code-block:: rst

   .. code-block:: python
      :emphasize-lines: 3,5
   
      def function(foo):
        if (some_thing):
          return bar
        else:
          return 0

will display as:

.. code-block:: python
   :emphasize-lines: 3,5

   def function(foo):
     if (some_thing):
       return bar
     else:
       return 0

.. format-content-code-block-line-emphasis-end


.. _format-content-code-block-clojure:

Clojure
--------------------------------------------------

.. format-content-code-block-clojure-start

For Clojure blocks, assign ``clojure`` as the name of the code block:

.. code-block:: rst

   .. code-block:: clojure

      user=> (println "Hello, world!")
      Hello, world!
      nil

to create a code block like this:

.. code-block:: clojure

   user=> (println "Hello, world!")
   Hello, world!
   nil

.. format-content-code-block-clojure-end


.. _format-content-code-block-command-shell:

Command shell
--------------------------------------------------

.. format-content-code-block-command-shell-start

For command shell blocks, assign ``console`` as the name of the code block:

.. code-block:: rst

   .. code-block:: console

      $ service stop

to create a code block like this:

.. code-block:: console

   $ service stop

.. format-content-code-block-command-shell-end


.. _format-content-code-block-config-file:

Config file
--------------------------------------------------

.. format-content-code-block-config-file-start

For generic configuration file blocks, assign ``text`` as the name of the code block:

.. code-block:: rst

   .. code-block:: text

      spark.setting.hours 1h
      spark.setting.option -User.timezone=UTC
      spark.setting.memory 20g

to create a code block like this:

.. code-block:: text

   spark.setting.hours 1h
   spark.setting.option -User.timezone=UTC
   spark.setting.memory 20g

.. note:: We're using ``text`` because there are not specific lexers available for all of the various configuration files. The ``text`` lexer allows us to style the code block similar to all of the others, but will not apply any highlighting to the formatting within the code block.

.. format-content-code-block-config-file-end


.. _format-content-code-block-css:

CSS
--------------------------------------------------

.. format-content-code-block-css-start

For CSS code blocks, assign ``css`` as the name of the code block:

.. code-block:: rst

   .. code-block:: css

      ul.tab-selector {
        display: block;
        list-style-type: none;
        margin: 10 0 10px;
        padding: 0;
        line-height: normal;
        overflow: auto;
      }

to create a code block like this:

.. code-block:: css

   ul.tab-selector {
     display: block;
     list-style-type: none;
     margin: 10 0 10px;
     padding: 0;
     line-height: normal;
     overflow: auto;
   }

.. format-content-code-block-css-end


.. _format-content-code-block-data-table:

Data table
--------------------------------------------------

.. format-content-code-block-data-table-start

Table blocks are used to show the inputs and outputs of processing data. For table code blocks, assign ``mysql`` as the name of the code block:

.. code-block:: rst

   .. code-block:: mysql

      --------- ---------
       column1   column2 
      --------- ---------
       value     value   
       value     value   
       value     value  
      --------- ---------

to create a code block like this:

.. code-block:: mysql

   --------- ---------
    column1   column2 
   --------- ---------
    value     value   
    value     value   
    value     value  
   --------- ---------

.. format-content-code-block-data-table-end


.. _format-content-code-block-html:

HTML
--------------------------------------------------

.. format-content-code-block-html-start

For HTML code blocks, assign ``html`` as the name of the code block:

.. code-block:: rst

   .. code-block:: html

      <div class="admonition warning">
        <p class="first admonition-title">Warning</p>
        <p class="last">The text for the warning built from raw HTML.</p>
      </div>

to create a code block like this:

.. code-block:: html

   <div class="admonition warning">
     <p class="first admonition-title">Warning</p>
     <p class="last">The text for the warning built from raw HTML.</p>
   </div>

.. format-content-code-block-html-end


.. _format-content-code-block-javascript:

JavaScript
--------------------------------------------------

.. format-content-code-block-javascript-start

For JavaScript code blocks, assign ``javascript`` as the name of the code block:

.. code-block:: rst

   .. code-block:: javascript

      $('div.content-tabs').each(function() {
          var tab_sel = $('<ul />', { class: "tab-selector" });
          var i = 0;

          if ($(this).hasClass('right-col')){
              tab_sel.addClass('in-right-col');
          }

          $('.tab-content', this).each(function() {
              var sel_item = $('<li />', {
                  class: $(this).attr('id'),
                  text: $(this).find('.tab-title').text()
              });
              $(this).find('.tab-title').remove();
              if (i++) {
                  $(this).hide();
              } else {
                  sel_item.addClass('selected');
              }
              tab_sel.append(sel_item);
              $(this).addClass('contenttab');
          });

          $('.tab-content', this).eq(0).before(contenttab_sel);
          contenttab_sel = null;
          i = null;
      });

to create a code block like this:

.. code-block:: javascript
      
   $('div.content-tabs').each(function() {
       var tab_sel = $('<ul />', { class: "tab-selector" });
       var i = 0;

       if ($(this).hasClass('right-col')){
           tab_sel.addClass('in-right-col');
       }

       $('.tab-content', this).each(function() {
           var sel_item = $('<li />', {
               class: $(this).attr('id'),
               text: $(this).find('.tab-title').text()
           });
           $(this).find('.tab-title').remove();
           if (i++) {
               $(this).hide();
           } else {
               sel_item.addClass('selected');
           }
           tab_sel.append(sel_item);
           $(this).addClass('contenttab');
       });

       $('.tab-content', this).eq(0).before(contenttab_sel);
       contenttab_sel = null;
       i = null;
   });

.. format-content-code-block-javascript-end


.. _format-content-code-block-json:

JSON
--------------------------------------------------

.. format-content-code-block-json-start

For JSON code blocks, assign ``json`` as the name of the code block:

.. code-block:: rst

   .. code-block:: json
      
      {
        "foo": [
          {
            "one": "12345",
            "two": "abcde",
            "three": "words"
          },
        ]
      }

to create a code block like this:

.. code-block:: json
      
   {
     "foo": [
       {
         "one": "12345",
         "two": "abcde",
         "three": "words"
       },
     ],
   }

.. format-content-code-block-json-end


.. _format-content-code-block-json-jinja:

JSON w/Jinja
--------------------------------------------------

.. format-content-code-block-json-jinja-start

For JSON code blocks that also embed Jinja templating, such as the nav-docs.html files that are used to build the documentation site's left navigation structures, the standard ``.. code-block:: json`` block will not work because the code block is not parsable as JSON. Instead, for code blocks that require a mix of JSON and Jinja templating, assign ``django`` as the name of the code block:

.. code-block:: rst

   .. code-block:: django

      {% extends "!nav-docs.html" %}
      {% set some_jinja = "12345" %}
      {% set navItems = [
        {
          "title": "Start Here",
          "iconClass": "fas fa-arrow-alt-circle-right fa-fw",
          "subItems": [
            {
              "title": "Start Here",
              "hasSubItems": false,
              "url": "/some_file.html"
            },
            {
              "title": "FAQ",
              "hasSubItems": false,
              "url": "/faq.html"
            },
            {
              "title": "Additional Resources",
              "hasSubItems": false,
              "url": "/resources.html"
            },
          ]
        },
      ] -%}

to create a code block like this:

.. code-block:: django

   {% extends "!nav-docs.html" %}
   {% set some_jinja = "12345" %}
   {% set navItems = [
     {
       "title": "Start Here",
       "iconClass": "fas fa-arrow-alt-circle-right fa-fw",
       "subItems": [
         {
           "title": "Start Here",
           "hasSubItems": false,
           "url": "/some_file.html"
         },
         {
           "title": "FAQ",
           "hasSubItems": false,
           "url": "/faq.html"
         },
         {
           "title": "Additional Resources",
           "hasSubItems": false,
           "url": "/resources.html"
         },
       ]
     },
   ] -%}

.. admonition:: Why django?

   Using ``django`` seems like an odd way to specify a code block that contains both Jinja and JSON.

   Django is a site templating language that is part of the Python world. The Sphinx themes are actually built using a combination of Django, Jinja, JSON, and other stuff. The left-side navigation, in particular, is a mix of JSON structure and Jinja variables.

   ``django`` identifies the Pygments lexer that parses a code block that contains both Jinja and JSON.

.. format-content-code-block-json-jinja-end



.. 
.. .. _format-content-code-block-markdown:
.. 
.. Markdown
.. --------------------------------------------------
.. 
.. .. format-content-code-block-markdown-start
.. 
.. For Markdown code blocks, assign ``md`` as the name of the code block:
.. 
.. .. code-block:: rst
.. 
..    .. code-block:: md
.. 
..       ~~~
..       ```eval_rst
..       .. note:: This is the text for the note built from a directive.
..       ```
..       ~~~
.. 
..       builds as:
.. 
..       ```eval_rst
..       .. note:: This is the text for the note built from a directive.
..       ```
.. 
.. .. note:: The Markdown lexer requires Pygments 2.2, but is configured to display the same as the reStructuredText code-block, but with MD in the upper right corner.
.. 
.. 
.. to create a code block like this:
.. 
.. .. code-block:: md
.. 
..    ~~~
..    ```eval_rst
..    .. note:: This is the text for the note built from a directive.
..    ```
..    ~~~
.. 
..    builds as:
.. 
..    ```eval_rst
..    .. note:: This is the text for the note built from a directive.
..    ```
.. 
.. .. format-content-code-block-markdown-end



.. _format-content-code-block-none:

None
--------------------------------------------------

.. format-content-code-block-none-start

For text that needs to be formatted as if it were a code block, but isn't actually code, assign ``none`` as the name of the code block:

.. code-block:: rst

   .. code-block:: none

      This is a none block. It's formatted as if it were code, but isn't actually code.

      Can include code-like things:

      function_foo()
        does: something
      end

to create a code block like this:

.. code-block:: none

   This is a none block. It's formatted as if it were code, but isn't actually code.

   Can include code-like things:

   function_foo()
     does: something
   end

.. format-content-code-block-none-end


.. _format-content-code-block-python:

Python
--------------------------------------------------

.. format-content-code-block-python-start

For Python code blocks, assign ``python`` as the name of the code block:

.. code-block:: rst

   .. code-block:: python

      def function(foo):
        if (some_thing):
          return bar
        else:
          return 0

to create a code block like this:

.. code-block:: python

   def function(foo):
     if (some_thing):
       return bar
     else:
       return 0

.. format-content-code-block-python-end


.. _format-content-code-block-rest-api:

REST API
--------------------------------------------------

.. format-content-code-block-rest-api-start

For REST API code blocks that show how to use an endpoint, assign ``rest`` as the name of the code block:

.. code-block:: rst

   .. code-block:: rest
      
      https://www.yoursite.com/endpoint/{some_endpoint}

to create a code block like this:

.. code-block:: rest
      
   https://www.yoursite.com/endpoint/{some_endpoint}


.. note:: Use the :ref:`format-content-code-block-json` code block style for the JSON request/response part of the REST API.

.. format-content-code-block-rest-api-end


.. _format-content-code-block-rst:

reStructuredText
--------------------------------------------------

.. format-content-code-block-rst-start

For reStructured Text code blocks, assign ``rst`` as the name of the code block:

.. code-block:: rst

   .. code-block:: rst

      This is some *reStructured* **Text** formatting.

      .. code-block:: none

         that has some(code);

to create a code block like this:

.. code-block:: rst

   This is some *reStructured* **Text** formatting.

   .. code-block:: none

      that has some(code);

.. format-content-code-block-rst-end


.. _format-content-code-block-ruby:

Ruby
--------------------------------------------------

.. format-content-code-block-ruby-start

For Ruby code blocks, assign ``ruby`` as the name of the code block:

.. code-block:: rst

   .. code-block:: ruby

      items = [ 'one', 1, 'two', 2.0 ]
      for it in items
        print it, " "
      end

      print "\n"

to create a code block like this:

.. code-block:: ruby

   items = [ 'one', 1, 'two', 2.0 ]
   for it in items
     print it, " "
   end

   print "\n"

.. format-content-code-block-ruby-end


.. _format-content-code-block-script:

Shell script
--------------------------------------------------

.. format-content-code-block-script-start

For shell script blocks, assign ``bash`` as the name of the code block:

.. code-block:: rst

   .. code-block:: bash

      # The product and version information.
      readonly MARKUP_PRODUCT="markup-app"
      readonly MARKUP_VERSION="1.23.45-6"
      readonly MARKUP_RELEASE_DATE="2019-04-01"

to create a code block like this:

.. code-block:: bash

   # The product and version information.
   readonly MARKUP_PRODUCT="markup-app"
   readonly MARKUP_VERSION="1.23.45-6"
   readonly MARKUP_RELEASE_DATE="2019-04-01"

.. format-content-code-block-script-end


.. _format-content-code-block-sql:

SQL query
--------------------------------------------------

.. format-content-code-block-sql-start

For SQL statements, assign ``sql`` as the name of the code block:

.. code-block:: rst

   .. code-block:: sql

      SELECT * FROM Customers WHERE Last_Name='Smith';

to create a code block like this:

.. code-block:: sql

   SELECT * FROM Customers WHERE Last_Name='Smith';

.. format-content-code-block-sql-end


.. _format-content-code-block-yaml:

YAML
--------------------------------------------------

.. format-content-code-block-yaml-start

For YAML code blocks, assign ``yaml`` as the name of the code block:

.. code-block:: rst

   .. code-block:: yaml

      config:
        - some_setting: 'value'
        - some_other_setting: 12345

to create a code block like this:

.. code-block:: yaml

   config:
     - some_setting: 'value'
     - some_other_setting: 12345

.. format-content-code-block-yaml-end


.. _format-content-code-block-yaml-jinja:

YAML w/Jinja
--------------------------------------------------

.. format-content-code-block-yaml-jinja-start

For YAML code blocks that also embed Jinja templating, the standard ``yaml`` block will not work because the code block is not parsable as YAML. Instead, these code blocks must be able to parse a mix of YAML and Jinja templating. Assign ``salt`` as the name of the code block:

.. code-block:: rst

   .. code-block:: salt

      {%- set some_jinja = "12345" %}

      config:
        - some_setting: 'value'
        - some_other_setting: {{ some_jinja }}

to create a code block like this:

.. code-block:: salt

   {%- set some_jinja = "12345" %}

   config:
     - some_setting: 'value'
     - some_other_setting: {{ some_jinja }}

.. admonition:: Why salt?

   Using ``salt`` seems like an odd way to specify a code block that contains both Jinja and YAML.

   SaltStack is a configuration management tool similar to Ansible, Chef, and Puppet. SaltStack uses a mix of Jinja and YAML to define system states that are to be configured and maintained. The ``salt`` lexer exists in Pygments originally because of how SaltStack defines system states, their use of Python and documentation built via Sphinx, and the need for a lexer that could parse a file with code samples that contain both Jinja and YAML.

   ``salt`` identifies the Pygments lexer that parses a code block that contains both Jinja and YAML.

.. format-content-code-block-yaml-jinja-end


.. _format-content-fontawesome:

Font Awesome
==================================================

.. format-content-fontawesome-start

The docs themes use the `free-for-web Font Awesome library <https://fontawesome.com/download>`__ as a local font library, primarily to add some flair to the left-side navigation. It's possible (though should be done sparingly) to place Font Awesome icons inline within paragraphs, like this: |fa-meh|.

This requires the tokens file to have an entry similar to:

.. code-block:: text

   .. |fa-meh| raw:: html

       &nbsp; <i class="fas fa-meh"></i> &nbsp;

after which ``|fa-meh|`` used inline in a paragraph results in |fa-meh|.

.. format-content-fontawesome-end


.. _format-content-header-h1:

Header (level 1)
==================================================

.. note:: The CSS for |theme| understands headers below H4; however it's recommended to not use headers below that level for some (aesthetic) reasons:

   #. The left-side navigation supports 3 levels.
   #. The right-side navigation, while built automatically from the headers that exist on that page, indents each header level, and then wraps the text when the header is longer than the width of the right-side column.

   As such, H4 headers are as much formatting as they are organization. Anything below H4 is recommended to be formatted as **Bold** so that it doesn't appear in the right-side navigation, but still looks on the page as if it were an H5 header. Headers formatted via **Bold** cannot be linked from the left-side navigation because only headers generate an anchor reference. Consider also reformatting the structure of your page to minimize the depth of the header levels. Or use H5 headers: it's up to you!

.. format-content-header-h1-start

An H1 header appears in the documentation like this:

.. code-block:: rst

   H1 headers
   ==================================================
   An H1 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h1-end


.. _format-content-header-h2:

Header (level 2)
--------------------------------------------------

.. format-content-header-h2-start

An H2 header appears in the documentation like this:

.. code-block:: rst

   H2 headers
   --------------------------------------------------
   An H2 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h2-end


.. _format-content-header-h3:

Header (level 3)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-content-header-h3-start

An H3 header appears in the documentation like this:

.. code-block:: rst

   H3 headers
   ++++++++++++++++++++++++++++++++++++++++++++++++++
   An H3 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h3-end


.. _format-content-header-h4:

Header (level 4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-content-header-h4-start

An H4 header appears in the documentation like this:

.. code-block:: rst

   H4 headers
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   An H4 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h4-end


.. _format-content-header-markup-length:

Header markup length
==================================================

.. format-content-header-markup-length-start

Sphinx requires the length of the header to be at least the same length as the content string that defines the header.

Short headers, short title markup. Makes sense!

That said, in large files, it's easier to scan the structure of the content when you can actually see where the headers are. That's why the header markup strings are recommended to be 50 characters long:

.. code-block:: none

   Short title
   ==================================================

This makes it easier to see the structure of the file when scrolling up and down a long topic page. This is pretty much the only reason to use consistent header markup length. Copy, paste, done.

.. format-content-header-markup-length-end


.. _format-content-images:

Images
==================================================

.. format-content-images-start

Images may be embedded in the documentation using the ``.. image::`` directive. For example:

.. code-block:: rst

   .. image:: ../../images/busycorp.svg
      :width: 600 px
      :alt: Welcome to Busycorp!
      :align: left
      :class: no-scaled-link

with the ``:width:`` and ``:align:`` attributes being aligned underneath ``image`` in the block. The ``no-scaled-link`` class option prevents images from being clickable.

This image will appear in the documentation like this:

.. image:: ../../images/busycorp.svg
   :width: 600 px
   :alt: Welcome to Busycorp!
   :align: left
   :class: no-scaled-link

Images should be SVG when only HTML output is desired. Printing to PDF from HTML pages requires PNG images.

**Wholesome Memes**

You can add your favorite GIF images (but please add them to internal-facing topics only):

.. image:: https://media.giphy.com/media/tXL4FHPSnVJ0A/giphy.gif

.. format-content-images-end


.. _format-content-includes:

Includes
==================================================

.. format-content-includes-start

Inclusions are a great way to single-source content. Write it in one place, publish it in many. There are two ways to handle inclusions, though both require using the ``.. includes::`` directive.

#. :ref:`format-content-include-via-file`
#. :ref:`format-content-include-via-snippet`

.. format-content-includes-end


.. _format-content-include-via-file:

via file
--------------------------------------------------

.. format-content-include-via-files-start

Inclusions may be done from standalone files. These standalone files are typically kept as a standalone file located in a dedicated directory within the docs repository, such as ``/shared/some_file.rst``.

The ``.. includes::`` is used to declare the path to that file. At build time, the contents of the included file are built into the location specified by the ``.. includes::`` directive.

For example:

.. code-block:: rst

   .. include:: ../../includes/terms.rst

will pull in the contents of that file right into the location of the directive.

.. format-content-include-via-files-end


.. _format-content-include-via-snippet:

via snippet
--------------------------------------------------

.. format-content-include-via-snippet-start

Inclusions may be done from within existing files as long as the target for that snippet is located in another file in the repository.

.. warning:: Snippets may not be used within the same file. What this means is the source of the snippet may not also be the target for that snippet. This will cause a rendering issue in the output or an error in the build.

These types of inclusions require two steps:

#. Declare a start and an end for the snippet; this declaration must be unique across the entire documentation repository.

   .. tip:: To help ensure unique snippet identifiers are built in the output, ensure that the snippet identifiers are directly assocaited with the name of the source directory and source file. These identifiers don't have to be long (though they can be), but they must be unique within a doc set.

      For example, a file locatated at ``internal_docs/source/tips.rst`` should have snippet identifiers like ``.. internal-docs-tips-some-identifier-start`` or ``.. internal-docs-tips-some-identifier-end``.
#. Specify the ``.. includes::`` directive, along with the ``:start-after:`` and ``:end-before:`` attributes.

   The ``:start-after:`` and ``:end-before:`` attributes effectively use a unique code comment located in the file defined by the ``.. includes::`` directive to know the start and end of the snippet to be included.

For example, a snippet is defined in ``docs/source/snippet.rst``:

.. code-block:: rst

   This is the file named snippet.rst. It has a few paragraphs and a
   reusable snippet.

   Paragraph one.

   .. docs-snippet-p2-start

   Paragraph two.

   .. docs-snippet-p2-end

   Paragraph three.

This snippet can be included in other files like this:

.. code-block:: rst

   Some content.

   .. include:: ../../docs/source/snippet.rst
      :start-after: .. docs-snippet-p2-start
      :end-before: .. docs-snippet-p2-end

   Some more content.

This should result in a file that looks similar to:

.. code-block:: rst

   Some content.

   Paragraph two.

   Some more content.

.. format-content-include-via-snippet-end

.. format-content-include-via-snippet-hint-start

.. hint:: Snippets may be sourced from large files that contain lists. For example, let's say the docs site has multiple docs collections (by application, by role, by internal vs. external, etc.) and you want each docs collection to have its own dedicated glossary to both enable consistency across doc sets for the same terms, but to also allow specific glossary terms for each doc set.

   In this case, all glossary terms can be created and managed from a single file like ``shared/terms.rst`` in which the snippet start-end pairs are defined and the glossary terms are managed. Then each ``glossary.rst`` file across the docs set can use the ``.. includes::`` directive to pull in the terms it needs.

.. format-content-include-via-snippet-hint-end


.. _format-content-inline-markup:

Inline markup
==================================================

.. format-content-inline-markup-start

Paragraphs, lists, and other strings of text behave here like they do in any text editor, with line breaks before and after, the usual. Use any of these formatting options within paragraphs, lists, tables, and so on:

* :ref:`format-content-inline-markup-bold`
* :ref:`format-content-inline-markup-italics`
* :ref:`format-content-inline-markup-code`

.. format-content-inline-markup-end


.. _format-content-inline-markup-bold:

Bold
--------------------------------------------------

.. format-content-inline-markup-bold-start

Use two asterisks (``**``) around the word to apply bold formatting: ``**bold**``. For example: **this is bold content**.

You may not use bold in headers or within the text strings for hyperlinks.

.. format-content-inline-markup-bold-end


.. _format-content-inline-markup-italics:

Italics
--------------------------------------------------

.. format-content-inline-markup-italics-start

Use a single asterisk (``*``) around the word to apply italics formatting: ``*italics*``. For example: *this is italicized content*.

You may not use italics in headers or within the text strings for hyperlinks.

.. format-content-inline-markup-italics-end


.. _format-content-inline-markup-code:

Code strings
--------------------------------------------------

.. format-content-inline-markup-code-start

Use two backticks around the code string to apply formatting to inline code strings. This will present them in a monospaced, bold format. For example:

.. code-block:: rst

   ``inline code string``

renders like this: ``inline code string``.

.. note:: An inline code string should only be used within lists and paragraphs for function names, commands for command-line tools, values, and so on, and only in a way where the contents of that code string reads normally in a sentence. Use the code-block directive for blocks of code or a none block for things that should be presented as code blocks, but might not be actual code blocks and/or may be incomplete code blocks.

.. format-content-inline-markup-code-end


.. _format-content-links:

Links
==================================================

.. format-content-links-start

There are three types of links:

#. :ref:`External <format-content-links-external>`
#. :ref:`External, with icon and opens in new tab <format-content-links-external-opens-new-tab>`
#. :ref:`Reference <format-content-links-reference>`
#. :ref:`Topic <format-content-links-topic>`

.. format-content-links-end


.. _format-content-links-external:

External
--------------------------------------------------

.. format-content-links-external-start

Use external links for links that stay within the Amperity knowledge center. These will generally take the form of a relative URL: ``../tutorials/start_here.html``.

You must embed the external link naturally within a sentence:

.. code-block:: rst

   `some link text here <../tutorials/start_here.html>`__

For example: `some link text here <../tutorials/start_here.html>`__

Use a double underscore (``__``) at the end of the external link.

.. format-content-links-external-end


.. _format-content-links-external-opens-new-tab:

External, opens new tab
--------------------------------------------------

.. format-content-links-external-opens-new-tab-start

Links that open to a page outside of the Amperity Documentation require using a token to ensure that ``target="_blank"`` can be added to the link.

**To use a link that opens in a new tab**

#. Open the file /tokens/external_links.txt.
#. Review the list of links. Use one that exists already if you can. Add the ``|ext_linkname|`` to your topic.
#. If the link is new, add the following:

   ::

      .. |ext_linkname| raw:: html

         <a href="href_goes_here" target="_blank">the string people see in the topic</a> <i class="fas fa-external-link-square-alt"></i>

   .. tip:: Be sure to prefix with ``ext_``.

For example: You should read all about |ext_stitchpatents| on the Amperity corpsite!

.. format-content-links-external-opens-new-tab-end


.. _format-content-links-reference:

Reference
--------------------------------------------------

.. format-content-links-reference-start

There are two ways to link to internal headers across the doc set.

First, a pre-requisite: the header to which the link is targeted must have an anchor. For example:

.. code-block:: rst

   .. _anchor-name:

   Internal Reference
   --------------------------------------------------
   There are two ways to link to internal headers across the doc set.
   First, a pre-requisite: the header that is the target of the link
   must be tagged:

where the internal reference is the ``.. _anchor-name:``. The string "anchor-name" must be unique across the entire doc set, so the required pattern for these is <file-name-header-name>, like this:

.. code-block:: rst

   .. _format-content-code-block-yaml:

and then there are two ways to link to that anchor. The first will pull in the header name as the link:

.. code-block:: rst

   :ref:`format-content-code-block-yaml`

and the second will use the string you put there and will not pull in the header name as the link:

.. code-block:: rst

   This links to some information about using
   :ref:`YAML code blocks <format-content-code-block-yaml>`
   in your documentation.

These first example renders like this: :ref:`format-content-code-block-yaml`. The second example is preferred and looks like the next sentence. This links to some information about using :ref:`YAML code blocks <format-content-code-block-yaml>` in your documentation.

.. format-content-links-reference-end


.. _format-content-links-topic:

Topic
--------------------------------------------------

.. format-content-links-topic-start

To link to internal topic use the following format:

.. code-block:: rst

   :doc:`a string that introduces the link and/or topic title <filename>`

and the second uses a string to replace (and override) the header name as the link:

.. code-block:: rst

   This links to some information about using :doc:`blocks </blocks>`
   to build a pipeline.

.. important:: You *must* put a string in the "a string that introduces the link and/or topic title" part of the format. If you don't, because of how we're using the ``.. rubric`` directive to hide the topic title from the right-side nav, you'll get a link to the first header in the topic. LOL.

.. format-content-links-topic-end


.. _format-content-lists:

Lists
==================================================

.. format-content-lists-start

Three types of lists are available:

* :ref:`format-content-list-definition`
* :ref:`format-content-list-ordered`
* :ref:`format-content-list-unordered`

.. format-content-lists-end


.. _format-content-list-definition:

Definition list
--------------------------------------------------

.. format-content-list-definition-start

A definition list is a specially formatted list that uses whitespace to indent the descriptive text underneath a word or a short phrase. This type of list should be used to describe settings, such as command line parameters, API arguments, glossary terms, and so on.

For example:

.. code-block:: rst

   **list_item_one**
      The description must be indented three spaces.

   **list_item_two**
      The description must be indented three spaces.

Which will appear in the documentation like this:

**list_item_one**
   The description must be indented three spaces.

**list_item_two**
   The description must be indented three spaces.

.. format-content-list-definition-end

.. format-content-list-definition-complex-start

.. note:: A definition list may contain a definition list. For example, some configuration settings (already in a definition list) have specific additional settings that must also be in a definition lists. These must be indented and must use the correct amount of whitespace.

.. format-content-list-definition-complex-start

.. format-content-list-definition-warning-start

.. warning:: A definition list title may not contain :ref:`inline markup <format-content-inline-markup>`.

.. format-content-list-definition-warning-start


.. _format-content-list-ordered:

Ordered list
--------------------------------------------------

.. format-content-list-ordered-start

An ordered list has each list item preceded by ``#.`` followed by a space. For example:

.. code-block:: rst

   #. one
   #. two
   #. three

Which will appear in the documentation like this:

#. one
#. two
#. three

.. tip:: You can create ordered lists that start with specific numbers, like this:

   .. code-block:: rst

      2. two
      3. three
      4. four

   which will appear in the documentation like this:

   2. two
   3. three
   4. four

   A list that does not start at 1 must specify sequential numbers with the list, but can be spread across paragraphs like this:

   2. two
   3. three
   4. four

   some more text.

   5. five
   6. six
   7. seven

.. format-content-list-ordered-end


.. _format-content-list-table:

Table list
--------------------------------------------------

.. format-content-list-table-start

A table list uses a table without a header row, and then only two columns, one for an image, and the other for the text for the step. For example:

.. code-block:: rst

   .. list-table::
      :widths: 80 520
      :header-rows: 0

      * - .. image:: ../../images/steps-01.png
             :width: 60 px
             :alt: Step one.
             :align: left
             :class: no-scaled-link
        - description
      * - .. image:: ../../images/steps-02.png
             :width: 60 px
             :alt: Step two.
             :align: left
             :class: no-scaled-link
        - description
      * - .. image:: ../../images/steps-03.png
             :width: 60 px
             :alt: Step two.
             :align: left
             :class: no-scaled-link
        - description

Which will appear in the documentation like this:

.. list-table::
   :widths: 80 520
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - An intro for a series of steps.

       #. Step one.
       #. Step two.
       #. Step three.
       #. Click **Resolve** to retry.

   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: left
          :class: no-scaled-link
     - An intro for a different series of steps. Lorem ipsum dolor set atemit.

       #. Step one.
       #. Step two.
       #. Step three.
       #. Click **Save**.

   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: left
          :class: no-scaled-link
     - An intro for another different series of steps.

       #. Step one.
       #. Step two.
       #. Step three.
       #. Click **Save**.

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link
     - Troubleshoot random authorization error!

       #. Step one.
       #. Step two.
       #. Step three.
       #. Click **Activate**.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: left
          :class: no-scaled-link
     - Five steps is probably starting to get a little long ...

       #. Step one.
       #. Step two.
       #. Step three.
       #. Click **Save**.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step six.
          :align: left
          :class: no-scaled-link
     - A sixth step is here for the infrequent use case that needs a sixth step.

       #. Do this.
       #. Do that.
       #. Check out this diagram:

          .. image:: ../../images/modal-file-uploads.png
             :width: 320 px
             :alt: Step six.
             :align: left
             :class: no-scaled-link

       #. Click **Save**.

   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step seven.
          :align: left
          :class: no-scaled-link
     - You should try not to build a table list with seven steps. But in rare cases, this is far as you're allowed to go.


**Example: A variety of left-side icons**

This is an example of a table-list:

.. list-table::
   :widths: 80 520
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - 1-9, plus 0

   * - .. image:: ../../images/steps-arrow-off-black-alt.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - Arrow, for some types of unordered lists. Refer to the overview of |destination_meta_ads_manager| for an example.

   * - .. image:: ../../images/steps-check-off-black.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link
     - Checkmark, for "you must know/do this" unordered lists, like a "Get details" section in a source or destination topic.

.. format-content-list-table-end


.. _format-content-list-unordered:

Unordered list
--------------------------------------------------

.. format-content-list-unordered-start

An unordered list has each list item preceded by a single asterisk (``*``) followed by a space. For example:

.. code-block:: rst

   * one
   * two
   * three

Which will appear in the documentation like this:

* one
* two
* three

.. format-content-list-unordered-end


.. _format-content-meta-tag:

Meta tags
==================================================

.. format-content-meta-tag-start

Each topic should have a ``meta`` tag that provides the description of the topic for use by external search engines, such as Google.

::

   .. meta::
       :description lang=en:
           This topic describes how to use orchestrations to send query results from Amperity to Adobe Experience Platform.

.. format-content-meta-tag-end


.. _format-content-tables:

Tables
==================================================

.. format-content-tables-start

Tables are always fun! This theme supports the following table types:

* :ref:`CSV tables <format-content-table-csv>`
* :ref:`Grid tables <format-content-table-grid>`
* :ref:`List tables <format-content-table-list>`
* :ref:`Simple tables <format-content-table-simple>`

You can see from the examples below that there are slight differences between how you can set up the tables to get various table structures. Some table types are more fun than others.

.. format-content-tables-end


.. _format-content-table-csv:

CSV table
--------------------------------------------------

.. format-content-table-csv-start

Tables may be built from a CSV file as long as the CSV file is available to Sphinx at build time. For example:

.. code-block:: rst

   .. csv-table::
      :file: ../../misc/test.csv
      :widths: 30, 70
      :header-rows: 1

with the ``:widths:`` and ``:header-rows:`` attributes being aligned underneath ``csv-table`` in the block. The ``:file:`` must be the path to a CSV file that is available to Sphinx at build time.

.. note:: |theme| has an example of a CSV file in the ``/misc`` directory. In fact, it's the same one for the ``:file`` parameter used in this example!

A CSV file is similar to:

.. code-block:: rst

   Header1,Header2
   12345,67890
   abcdefghijklmnopqrstuvwxyz,abcdefghijklmnopqrstuvwxyz

where the first line in the CSV file is the header row.

.. format-content-table-csv-end


.. _format-content-table-grid:

Grid table
--------------------------------------------------

.. format-content-table-grid-start

Grid tables are built by physically spacing out the table in the text file, similar to how it will appear on the page. These are easy when they are small.

.. code-block:: none

   +------------+------------+-----------+ 
   | Header 1   | Header 2   | Header 3  | 
   +============+============+===========+ 
   | body row 1 | column 2   | column 3  | 
   +------------+------------+-----------+ 
   | body row 2 | Cells may span columns.| 
   +------------+------------+-----------+ 
   | body row 3 | Cells may  | - Cells   | 
   +------------+ span rows. | - contain | 
   | body row 4 |            | - blocks. | 
   +------------+------------+-----------+

builds as:

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

.. format-content-table-grid-end


.. _format-content-table-list:

List table
--------------------------------------------------

.. format-content-table-list-start

A list-table is built using the ``.. list-table::`` directive.

.. code-block:: rst

   .. list-table::
      :widths: 30 70
      :header-rows: 1

      * - columnName
        - columnName
      * - **item1**
        - description
      * - **item2**
        - description

with the ``:widths:`` and ``:header-rows:`` attributes being aligned underneath ``list-table`` in the block. The number of rows (identified by the dashes (``-``) must equal the number of integers specified by ``:widths:``. The integers specified by ``:widths:`` specifies each column's width, from left to right in pixels *or* in percentages. When ``:widths:`` specifies percentages, the total for all column widths must equal 100. Table widths should not exceed 600 pixels, as a general rule.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - columnName
     - columnName
   * - **item1**
     - description
   * - **item2**
     - description

.. format-content-table-list-end


.. _format-content-table-simple:

Simple table
--------------------------------------------------

.. format-content-table-simple-start

Simple tables are simple. The markup is focused mostly on the vertical layout. Like grid tables, they are easy when they are small.

.. code-block:: none

   =====  =====  ====== 
      Inputs     Output 
   ------------  ------ 
     A      B    A or B 
   =====  =====  ====== 
   False  False  False 
   True   False  True 
   False  True   True 
   True   True   True 
   =====  =====  ======

builds as:

=====  =====  ====== 
   Inputs     Output 
------------  ------ 
  A      B    A or B 
=====  =====  ====== 
False  False  False 
True   False  True 
False  True   True 
True   True   True 
=====  =====  ======

.. format-content-table-simple-end


.. _format-content-toctree:

Toctree
==================================================

.. format-content-toctree-start

A Sphinx project must declare all of the topics that are part of it within a directive named ``toctree``.

.. note:: Because |theme| doesn't build its left navigation automatically from the header structures in topics and because there's no previous/next linking, there's no reason to put a ``toctree`` on more than one page. Instead, just put the ``toctree`` on the root page for the project (default root page name is ``index.rst``), and then add to that ``toctree`` an alphabetical list of every other topic in the collection.

A toctree is similar to:

.. code-block:: none

   .. Hide the TOC from this file.

   .. toctree::
      :hidden:

      test

which defines the list of files--in this case just ``test.rst``--in the documentation collection. Be sure to keep ``:hidden:`` as a property of ``toctree``.

View the ``index.rst`` file in the ``/markup_theme`` directory to see a full and complete example of a toctree.

.. format-content-toctree-end


.. _format-content-tokens:

Tokens
==================================================

.. format-content-tokens-start

Tokens are defined in the file ``names.txt`` located in the ``/tokens`` directory. Each token is defined similar to:

.. code-block:: rst

   .. |company_name| replace:: YourCompanyName

When used in a sentence, use the ``|company_name|`` token to replace the string that follows ``replace::``. For example: use ``|theme|`` to add |theme|.

.. warning:: Tokens may not be used in the left-side navigation template (``nav-docs.html``).

The following example tokens exist at ``/tokens/names.txt``:

* ``|company_name|`` => |company_name|
* ``|theme|`` => |theme|
* ``|md|`` => |md|
* ``|rst|`` => |rst|

Use tokens in headers or topic titles carefully. Sphinx will build them correctly in the topic, but anchor references from the left-side navigation will not work unless the anchor reference specifies the token. For example, a token named ``|abc|`` used for a title must be specified in the left navigation as ``"url": "/path/to/file.html#abc"``. Tokens cannot be used within :ref:`inline markup <format-content-inline-markup>`.

.. note:: Too many tokens can really slow builds down. Sphinx will check each file for the presence of tokens, and then check the tokens file to up each token for matching strings. The point at which tokens can slow builds down depends on a) the number of tokens and b) the number of files in each documentation collection. It should be stated that slower builds don't start to become noticeable until there are a couplefew hundred tokens and documentation collections with 60+ topics, some of which are very long reference topics. For small doc sets you may never notice any performance issues and the points at which you may notice performance issues, the benefits of using tokens and reusable strings may outweigh slower build times.
.. format-content-tokens-end


.. _format-content-topic-title:

Topic titles
==================================================

.. format-content-tokens-start

A topic title header appears in the documentation like this:

.. code-block:: rst

   ==================================================
   Topic title
   ==================================================

Which will appear in the documentation like the actual topic title for this topic.

.. warning:: Do not use rubric for topic titles. When you do it looks great in the right-side navigation, but not so great in search results. Boo.

.. format-content-tokens-end


.. _format-content-additional-resources:

Additional resources
==================================================

The following resources may be useful:

* `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_

