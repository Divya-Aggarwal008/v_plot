import gzip
import subprocess

count = {}
f = gzip.open("mapped.bed.gz", "rt")
for line in f:
	val = line.strip().split("\t")
	pos = ((int(val[8]) + int(val[9])) /2) - ((int(val[2]) + int(val[3])) /2)
	if (pos >= -500) and (pos <= 500):
		key = f"{pos}\t{val[11]}"
		count[key] = count.get(key, 0) + 1
out = open("matrix.tsv", "w")
for key, v in count.items():
	out.write(f"{key}\t{v}\n")

gnuplot_command = f"gnuplot v_plot.gnu"
subprocess.run(gnuplot_command, shell=True)
