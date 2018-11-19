import csv
import os
import subprocess
import time
import random
phrase="syria conflict archaeology";
no_spaces=phrase.replace(" ", "-");
with open("%s.csv" % no_spaces, "a+") as csvfile:
    with open("%s.txt" % no_spaces, "w+") as txtfile:
            for i in range(0, 1):
                time.sleep(random.randrange(3, 5))
                subprocess.call(["scholar.py", "-p", phrase, "-N", str(i), "--csv"], shell=True, stdout=txtfile)
    with open("%s.txt" % no_spaces, "r") as finishedtxt:
        lines=(line.split('|') for line in finishedtxt)
        row_writer=csv.writer(csvfile,lineterminator='\n')
        row_writer.writerows(lines)
