python2.7 replace_tbot_marker.py -i index.rst -o work/index.rst -t logfiles/ -r True -l rst -w 100
rst2pdf -s stylesheet.txt work/index.rst pdf/index.pdf
python2.7 mark_red.py -i pdf/index.pdf -o pdf/dulg_bbb.pdf;okular pdf/dulg_bbb.pdf

