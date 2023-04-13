input=$1

# pdfpages=`pdfinfo ${input} | awk '/^Pages:/ {print $2}'`

# for i in `seq $pdfpages`
# do
#     pdftk $input cat $i output ${input%.pdf}"_$i.pdf"
#     convert ${input%.pdf}"_$i.pdf" ${input%.pdf}"_$i.jpg"
# done

pdftoppm ${input} ${input} -png
