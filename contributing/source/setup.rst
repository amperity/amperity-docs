.. https://docs.amperity.com/contributing/


==================================================
Set up your writing environment
==================================================

Local development of documentation for Amperity is done on your workstation and requires some configuration.


.. _contributing-set-up-environment-venv:

Set up your Python virtual environment
==================================================

.. contributing-set-up-environment-venv-start

To set up your local authoring environment:

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - .. image:: ../../images/steps-01.png
          :width: 60 px
          :alt: Step one.
          :align: left
          :class: no-scaled-link

     - Choose your favorite text editor. On a Mac, TextMate is recommended.

       .. important:: On a Mac, do not use the built-in TextEdit application to make changes to files in the documentation repo. Its behavior is inconsistent, sometimes unreliable, and *can* introduce unwanted formatting behaviors and build outcomes.


   * - .. image:: ../../images/steps-02.png
          :width: 60 px
          :alt: Step two.
          :align: left
          :class: no-scaled-link

     - `Install GitHub Desktop (recommended) <https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop>`__ or use your preferred tool of choice for interacting with GitHub repos.


   * - .. image:: ../../images/steps-03.png
          :width: 60 px
          :alt: Step three.
          :align: left
          :class: no-scaled-link

     - Install Serve, which enables viewing the docs in localhost. On a Mac, use Homebrew:

       .. code-block:: text

          $ brew install serve

   * - .. image:: ../../images/steps-04.png
          :width: 60 px
          :alt: Step four.
          :align: left
          :class: no-scaled-link

     - Pull down the docs repo. Use GitHub Desktop to clone the docs repo, using ``https://github.com/amperity/amperity-docs`` as the URL value.

       .. tip:: Put the docs repo into the same location on your local machine as your Amperity apps repo. For example: ``/documents/github/amperity-docs``.

   * - .. image:: ../../images/steps-05.png
          :width: 60 px
          :alt: Step five.
          :align: left
          :class: no-scaled-link

     - Open a terminal and ``cd`` to the folder containing the docs repo. For example:

       .. code-block:: text

          $ cd documents/github/
         
   * - .. image:: ../../images/steps-06.png
          :width: 60px
          :alt: Step six.
          :align: left
          :class: no-scaled-link

     - Create a Python virtual environment inside the repository by running:

       .. code-block:: text

          $ cd amperity-docs && python3 -m venv .venv

         
   * - .. image:: ../../images/steps-07.png
          :width: 60px
          :alt: Step seven.
          :align: left
          :class: no-scaled-link

     - Enter the virtual environment and install the requirements by running:

       .. code-block:: text

          $ source .venv/bin/activate && pip install -r requirements.txt


   * - .. image:: ../../images/steps-08.png
          :width: 60 px
          :alt: Step eight.
          :align: left
          :class: no-scaled-link

     - Run ``make``. This builds the documentation locally on your machine.

       .. note:: If you get an error similar to "make: sphinx-build: No such file or directory" verify that your $PATH variable is updated to match the location on your machine into which Homebrew or Pip installed Sphinx.

       Run ``make serve``, and then open ``http://localhost:8080/`` to view the documenation.

.. contributing-set-up-environment-venv-end


Install Vale
==================================================

.. contributing-install-vale-start

Vale is a command-line style linter that checks documentation against the Amperity style guide. Install it using Homebrew:

.. code-block:: text

   $ brew install vale

Verify the installation:

.. code-block:: text

   $ vale --version

.. contributing-install-vale-end

