
#for f in logfiles/*.txt;
#do
#    sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" $f > tmp.txt
#    mv tmp.txt $f
#done

for f in logfiles/*.txt;
do
  # echo "Processing $f file..";
  # check if it contains escape sequences
  grep -q $'\x1B' $f
  if [ $? -eq 0 ]; then
    echo 'FOUND '$f
    ansi2txt $f > tmp.txt
    mv tmp.txt $f
  fi
done

python2.7 replace_tbot_marker.py -i index.rst -o work/index.rst -t logfiles/ -r True -l rst -w 125
rst2pdf -s stylesheet.txt work/index.rst pdf/index.pdf
python2.7 mark_red.py -i pdf/index.pdf -o pdf/dulg_bbb.pdf;okular pdf/dulg_bbb.pdf

