# Contributing

Thank you for helping improve the Amperity documentation.

## Report a documentation problem

GitHub Issues are disabled in this repository. To report a documentation problem or request an update, open the affected page on the [Amperity documentation site](https://docs.amperity.com/) and use the feedback button. Include:

- A clear summary of the problem or requested improvement.
- The affected page URL or file path.
- The current behavior and the change you expect, with reproduction steps when relevant.
- Any suggested wording, examples, or other context that may help.

## Submit a pull request

External contributors should use a fork:

1. Fork the [amperity-docs repository](https://github.com/amperity/amperity-docs).
2. Clone your fork and create a focused branch from `main`.
3. Make your documentation changes and follow the [style guidance](#style).
4. Build the affected documentation locally and review the generated pages.
5. Push your branch to your fork and open a pull request against `amperity/amperity-docs:main`.
6. In the pull request description, explain what changed, why it changed, and link any related issue.

Please keep pull requests focused. Review the automated build results and respond to review feedback until the change is ready to merge.

## Style

Follow the [Amperity style guide](https://docs.amperity.com/contributing/styles.html). The [Terminology](https://docs.amperity.com/contributing/terminology.html), [Verbs](https://docs.amperity.com/contributing/verbs.html), and [Formatting guide](https://docs.amperity.com/contributing/rst.html) pages cover common writing and reStructuredText conventions.

## Develop locally

The documentation is built with Sphinx. For the complete environment setup, see [Set up your writing environment](https://docs.amperity.com/contributing/setup.html).

From the repository root, create a virtual environment and install the dependencies:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create the build output directory:

```shell
mkdir -p build
```

Build only the contributing documentation:

```shell
make contributing
```

There is no separate unit-test suite. The Sphinx build is the repository's documentation check, and warnings are treated as errors. Run `make` to build every documentation collection before submitting a pull request when your change affects shared content or build behavior. If an unrelated collection fails, record that failure and confirm that the focused build passes.

After building, start the local server:

```shell
make serve
```

Open [http://localhost:8080/contributing/](http://localhost:8080/contributing/) to view the contributing documentation. The `serve` command must be installed separately; the setup guide describes the supported installation method.
