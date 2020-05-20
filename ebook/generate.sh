NAME=$(basename -s .tex "$1")
latexmk "$1"
pandoc --toc $NAME.tex -o $NAME.epub
ebook-convert $NAME.epub $NAME.mobi
