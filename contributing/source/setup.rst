.. 
.. https://docs.amperity.com/contributing/
..

==================================================
Workstation setup
==================================================

Local development of documentation for Amperity can be done on your workstation and requires some configuration.




Requirements
==================================================

* Python 3.9
* Sphinx 7.3.7
* docutils 0.20
* sphinxcontrib-redoc 1.6.0 (builds the OpenAPI specification for the Ampeity API)
* sphinxcontrib-video 0.2.0 (allows embedding videos on pages)

A text editor.

EditPad Pro is recommended for PCs and TextMate is recommended for MacOS. You may use your preferred text editor as long as it supports the following:

#. Line wrapping
#. Does not automatically remove spaces at the end of strings.
#. Does not use tabs instead of spaces




.. _contributing-set-up-environment:

Set up your environment
==================================================

.. contributing-set-up-environment-start

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

     - Install Sphinx 7.3.7, which is the command-line tool that builds the documentation. Use Pip or Homebrew to install Sphinx:

       .. code-block:: text

          $ pip3 install sphinx==7.3.7

       *or*

       .. code-block:: text

          $ brew install sphinx-doc==7.3.7

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step 4.
          :align: left
          :class: no-scaled-link

     - Install Serve, which enables viewing the docs in localhost. On a Mac, use Homebrew:

       .. code-block:: text

          $ brew install serve

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step 5.
          :align: left
          :class: no-scaled-link

     - Pull down the docs repo. Use GitHub Desktop to clone the docs repo, using ``https://github.com/amperity/amperity-docs`` as the URL value.

       .. tip:: Put the docs repo into the same location on your local machine as your Amperity apps repo. For example: ``/documents/github/amperity-docs``.

   * - .. image:: ../../images/steps-06.png
          :width: 60 px
          :alt: Step 6.
          :align: left
          :class: no-scaled-link

     - Open a terminal and ``cd`` to the docs repo. For example:

       .. code-block:: text

          $ cd documents/github/amperity-docs

   * - .. image:: ../../images/steps-07.png
          :width: 60 px
          :alt: Step 7.
          :align: left
          :class: no-scaled-link

     - Run ``make``. This will build the documentation locally on your machine.

       .. note:: If you get an error similar to "make: sphinx-build: No such file or directory" verify that your $PATH variable is updated to match the location on your machine into which Homebrew or Pip installed Sphinx.

       Run ``make serve``, and then open ``http://localhost:8080/`` to view the documenation.

.. contributing-set-up-environment-end

.. _contributing-set-up-environment-venv:

Set up your environment (Python venv)
==================================================

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

