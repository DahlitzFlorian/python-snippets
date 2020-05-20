pandoc --toc $1.tex -o $1.epub
ebook-convert $1.epub $1.mobi
