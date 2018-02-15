wdir="/home/pi/tbot2go/tbot/src/documentation"
srcpath="/home/pi/tbot2go/documentation/yocto"
logfilespath="/home/pi/tbot2go/documentation/yocto/logfiles_get_and_bake/"
logfilespath="/home/pi/tbot2go/documentation/yocto/logfiles_bbb/"

for f in $logfilespath*.txt;
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

for f in $logfilespath*.txt;
do
    found=`echo $f | grep -c cpc`
    if [ $found -ne 0 ]; then
        echo "FOUND " $f
        n=${f/cpc/ctrl}
        echo "FOUND " $n
        mv $f $n
    fi
done

python2.7 $wdir/replace_tbot_marker.py -i $srcpath/index.rst -o $srcpath/work/index.rst -t $logfilespath -r True -l rst -w 125
rst2pdf -s $wdir/stylesheet.txt $srcpath/work/index.rst $srcpath/pdf/index.pdf
python2.7 $wdir/mark_red.py -i $srcpath/pdf/index.pdf -o $srcpath/pdf/yocto_bbb.pdf

