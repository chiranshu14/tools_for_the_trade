from time import thread_time
import pandas as pd
import os
from bs4 import BeautifulSoup
import requests
import time
import json 


def parse(file_name):
    with open(file_name + "",encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    data_divs = soup.find_all('div', {'class' : '_a9zs'})
    len(data_divs)
    count = 0
    output = []
    for comment in data_divs:
        # count += 1
        # if count ==5:
        #     break
        output.append(comment.find_all('span')[-1].text)

    df = pd.DataFrame(output)
    df.to_csv("output/"+file_name.replace("raw_files/","") + '.csv',encoding='utf-8-sig')



# parse("huberman_comments_cannabis.txt")
parse("raw_files/aliabdaal_3l_followers.txt")
parse("raw_files/huberman_comments_cannabis.txt")
parse("raw_files/lex_kanye.txt")
parse("raw_files/pat_david_haters.txt")
parse("raw_files/peter_attia_sleep.txt")