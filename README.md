# Python Snippets #
## Description ##
A collection of useful Python snippets.

**standard_lib:** Contains those snippets, which do not depend
on third-party packages.

**third_party:** As the name suggests, it contains those snippets
depending on third-party packages, even if it's only `requests`
or `click`.

**ebook:** Contains an ebook including the provided snippets and additional explanations and insights.
The ebook is available as `.epub`, `.mobi` and `.pdf`.
Currently `pandoc` doesn't support LaTeX `\ref{...}` handling, which is used in the ebook.
That said, the `epub` and `mobi` version won't show the correct Listing numbers in the text, whereas the `pdf` version does.


## Installation

The code snippets in the [`third_party`](third_party) directory depend on other packages you need to install.
A `pyproject.toml` and a `poetry.lock` are in the directory, too, as poetry is used for dependency management.

> **Note:** Due to the changed distribution settings of the library `tensorflow`, you need to install it separately on your system in order to run some of the snippets in this repo.
> `tensorflow` is no longer part of the repositories `pyproject.toml`.
