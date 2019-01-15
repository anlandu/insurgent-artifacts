import csv
import os
import subprocess
import time
import random
import pandas as pd
import re
phrase="syria conflict archaeology"
paper="6976012688809100275"
no_spaces=phrase.replace(" ", "-")

def get_from_num(root, paper):
    with open("/%s/%s.csv" % (root, paper), "a+") as csvfile:
        with open("/%s/%s.txt" % (root, paper), "w+") as txtfile:
                for i in range(0, 1):
                    subprocess.call(["scholar.py", "-i", paper, "-N", str(i), "--csv"], shell=True, stdout=txtfile)
        with open("%s.txt" % paper, "r") as finishedtxt:
            lines=(line.split('|') for line in finishedtxt)
            row_writer=csv.writer(csvfile,lineterminator='\n')
            row_writer.writerows(lines)

def get_citation_tree(num):
    with open("%s.csv" % num, "r") as csvfile:
            df = pd.read_csv(csvfile)
            saved_column = df.url_citations
            citation_nums = []
            for item in saved_column:
                print(item)
                try:
                    curnum = re.search(r"(?<=cites=)\d+", item).group(0)
                    print("Curnum: "+curnum)
                    if curnum:
                        citation_nums.append(curnum)
                except:
                    continue
            for item in citation_nums:
                print(item)
                get_from_num(num, item)
get_from_num("roots", paper)
# get_citation_tree(paper)
