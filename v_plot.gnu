set terminal png
set output "v_plot.png"
set title "v_plot"
set xlabel "Relative_Distance"
set ylabel "length"
set palette defined (0 "white",1 "blue", 2 "red")

plot "matrix.tsv" using 1:2:3 with points palette
