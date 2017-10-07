wdir="/home/pi/tbot2go/tbot/src/documentation"
srcpath="/home/pi/tbot2go/documentation/yocto"

for f in $srcpath/logfiles_get_and_bake/*.txt;
do
  # echo "Processing $f file..";
  # check if it contains escape sequences
  grep -qaP '\x1B\x5B' $f
  if [ $? -eq 0 ]; then
    echo 'FOUND '$f
    ansi2txt $f > tmp.txt
    mv tmp.txt $f
  fi
done

python2.7 $wdir/replace_tbot_marker.py -i $srcpath/index.rst -o $srcpath/work/index.rst -t $srcpath/logfiles_get_and_bake/ -r True -l rst -w 125
rst2pdf -s $wdir/stylesheet.txt $srcpath/work/index.rst $srcpath/pdf/index.pdf
python2.7 $wdir/mark_red.py -i $srcpath/pdf/index.pdf -o $srcpath/pdf/yocto_bbb.pdf

