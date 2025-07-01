.. https://docs.amperity.com/contributing/


==================================================
Set up your writing environment
==================================================

Local development of documentation for Amperity is done on your workstation and requires some configuration.


Requirements
==================================================

* Python 3.9
* Sphinx 7.3.7
* docutils 0.20

A text editor.

EditPad Pro is recommended for PCs and TextMate is recommended for macOS. You may use your preferred text editor as long as it supports the following:

#. Line wrapping
#. Does not automatically remove spaces at the end of strings.
#. Does not use tabs instead of spaces



Pull the Amperity docs repo
==================================================

Download the following GitHub repo using GitHub Desktop:

https://github.com/amperity/amperity-docs

This repo contains a functioning version of Amperity docs with the Shibuya theme applied with some layout/theme tweaks and updated navigation. It's not done, but it's functional and works.

Create Python virtual environment
==================================================

Run the following commands to create a Python virtual environment:

#. $ ``cd documents/github/amperity-docs-test``
#. $ ``python3 -m venv .venv``
#. $ ``source .venv/bin/activate``
#. $.venv ``python3 -m pip install sphinx``
#. $.venv ``sphinx-build --version``

   Returns something like:

   "sphinx-build 7.4.7"


Note. The ``$.venv`` isn't part of the command you should run. This just means "In the Python virtual environment, run this command".

Install dependencies
==================================================

In the same virtual environment, run the following commands:

#. $.venv ``pip install shibuya``
#. $.venv ``pip install sphinx-togglebutton``
#. $.venv ``pip install sphinx_sitemap``
#. $.venv ``pip install sphinxcontrib-mermaid``
#. $.venv ``pip install sphinxcontrib-video``
#. $.venv ``pip install sphinxcontrib-youtube``
#. $.venv ``pip install sphinx-copybutton``
#. $.venv ``pip install sphinx_design``


Build the docs
==================================================

Open a new command shell window, and then run the following commands:

#. $ ``cd documents/github/amperity-docs``
#. $ ``make``
#. $ ``make serve``
#. Open another command shell to run the ``make`` command and regular docs development.




.. _contributing-set-up-environment-venv:

Set up your environment (Python venv)
==================================================

.. TODO: Make this the "default" and let's get rid of the more convoluted steps that use the built-in macOS Pythonisms.

.. contributing-set-up-environment-venv-start

To set up your local authoring environment:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step 1.
          :align: left
          :class: no-scaled-link

     - Choose your favorite text editor. On a Mac, TextMate is recommended.

       .. important:: On a Mac, please do not use the built-in TextEdit application to make changes to files in the documentation repo. Its behavior is inconsistent, sometimes unreliable, and *can* introduce unwanted formatting behaviors and build outcomes.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step 2.
          :align: left
          :class: no-scaled-link

     - `Install GitHub Desktop (recommended) <https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop>`__ or use your preferred tool of choice for interacting with GitHub repos.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step 3.
          :align: left
          :class: no-scaled-link

     - Install Serve, which enables viewing the docs in localhost. On a Mac, use Homebrew:

       .. code-block:: text

          $ brew install serve

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link

     - Pull down the docs repo. Use GitHub Desktop to clone the docs repo, using ``https://github.com/amperity/amperity-docs`` as the URL value.

       .. tip:: Put the docs repo into the same location on your local machine as your Amperity apps repo. For example: ``/documents/github/amperity-docs``.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link

     - Open a terminal and ``cd`` to the folder containing the docs repo. For example:

       .. code-block:: text

          $ cd documents/github/
         
   * - .. image:: ../../images/steps-06.png
          :width: 60px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link

     - Create a python virtual environment in the repository by running:

       .. code-block:: text

          $ python3 -m venv amperity-docs

         
   * - .. image:: ../../images/steps-07.png
          :width: 60px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link

     - Enter the virtual environment and install the requirements by running:

       .. code-block:: text

          $ cd amperity-docs && source /bin/activate \
          && pip install -r requirements.txt


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step 8.
          :align: left
          :class: no-scaled-link

     - Run ``make``. This will build the documentation locally on your machine.

       .. note:: If you get an error similar to "make: sphinx-build: No such file or directory" verify that your $PATH variable is updated to match the location on your machine into which Homebrew or Pip installed Sphinx.

       Run ``make serve``, and then open ``http://localhost:8080/`` to view the documenation.

.. contributing-set-up-environment-venv-end

