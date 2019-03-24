$pdflatex = "xelatex %O %S";
$pdf_mode = 1;
$dvi_mode = 0;
$postscript_mode = 0;
add_cus_dep('glo', 'gls', 0, 'makeglo2gls');
sub makeglo2gls {
    system("makeindex -s '$_[0]'.ist -t '$_[0]'.glg -o '$_[0]'.gls '$_[0]'.glo");
}
