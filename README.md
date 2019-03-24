# Python Snippets #
## Description ##
A collection of useful Python snippets.

**standard_lib:** Contains those snippets, which do not depend
on third-party packages.

**third-party:** As the name suggests, it contains those snippets
depending on third-party packages, even though it's only `requests`
or `click`.

**ebook:** Contains an ebook including the provided snippets and additional explanations and insights.
The ebook is available as `.epub`, `.mobi` and `.pdf`.
Currently `pandoc` doesn't support LaTeX `\ref{...}` handling, which is used in the ebook.
That said, the `epub` and `mobi` version won't show the correct Listing numbers in the text, whereas the `pdf` version does.
