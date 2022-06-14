#!/usr/bin/env python

'''
m.py

Copyright 2017 BA7LNN
Contact: BA7LNN@FOXMAIL.COM

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

'''
import glob
import os

post_dir = '_posts/'
tag_dir = 'series/'

filenames = glob.glob(post_dir + '*markdown')

total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'series:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.markdown')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: series\ntitle: \"Series: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Series generated, count", total_tags.__len__())
'''

'''
layout: post
title: Ultra flexible 0.06 Series Silicone wire
#permalink: 006-silicone-wire
date: 2018-05-05 14:52:44
categories: wire-cable
tags: 0.06 Silicon Robbin Wire(Flexible)
summary: Ultra flexible 0.06 Series Silicone wire
published: true 
series: FN10
part_number: 10-0006-0
mfg_part_number: 
mfg_part_number2: 
price: 0.00
thumb_img: static/202003/2-thumb-20200325150017.jpg
small_img: static/202003/2-20200325150017.jpg
'''
import os
import glob
import pymysql
import datetime
import time

post_dir = '_posts2/'

filenames = glob.glob(post_dir + '*markdown')
for filename in filenames:
	os.remove(filename)

if not os.path.exists(post_dir):
	os.makedirs(post_dir)

# pip install pymysql
# pip show pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='hingtak',charset='utf8')
cur = conn.cursor()

sql = "select n.*, c.url_name,c.category_text from `my_nodes` n left join my_category c on (n.category_id=c.id)"
cur.execute(sql)
data = cur.fetchall()

for i in data:
	post_filename = post_dir+str(i[0])+'.markdown'
	f = open(post_filename, 'a')
	write_str = '---\nlayout: post' \
	+ '\ntitle: '+i[2] \
	+ '\ncategories: ' + str(i[20])\
	+ '\nseries: ' + str(i[6])\
	+ '\ntags: ' + str(i[5]) \
	+ i[21] \
	+ '\n---\n'
	
	f.write(write_str)
	f.close()
	

print("Post generated finished")

cur.close()
conn.close()
