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

##  social_account_user_id = models.CharField(max_length=255,null=True, blank=True)
##  # social_account_user_id = models.ForeignKey('social_users.SocialUser', to_field='social_account_user_id', on_delete=models.CASCADE)
##  id = models.CharField(primary_key=True,max_length=255)
##  timestamp = models.CharField(max_length=255,null=True, blank=True)
##  username = models.CharField(max_length=255,null=True, blank=True)
##  text = models.CharField(max_length=255,null=True, blank=True)
##  like_count = models.IntegerField(blank=False, null=False, default=0)
##  sentiment = models.CharField(max_length=255,null=True, blank=True)
##  toxicity = models.CharField(max_length=255,null=True, blank=True)
##  custom_category = models.CharField(max_length=255,null=True, blank=True)
##  # media_id = models.CharField(max_length=255,null=True, blank=True)
##  media_id = models.ForeignKey('social_media.SocialMedia', to_field='id', on_delete=models.CASCADE)
##  reply_text = models.CharField(max_length=255,null=True, blank=True)
##  intent = models.CharField(max_length=255,null=True, blank=True)
##  quick_replies = models.CharField(max_length=255,null=True, blank=True)
##  # quick_replies = ArrayField(models.CharField( blank=True))
