from itertools import islice
from math import ceil
import csv
from instascrape import *
from selenium import webdriver
from instabrade import Instagram



from instaloader import Instaloader,  Post

PROFILE = "nhl"        # profile to download from
                       # percentage of posts that should be downloaded
files_path='0_500.csv'


L = Instaloader(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36")







SHORTCODE='Bm1rDT1hTbD'
print(SHORTCODE)
post = Post.from_shortcode(L.context, SHORTCODE)
L.download_post(post, target=SHORTCODE)