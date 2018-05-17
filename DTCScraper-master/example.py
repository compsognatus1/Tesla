#!/usr/bin/python
# -*- coding: utf-8 -*-

from DTCScrapper import DTCScrapper
import sys

# Get the quote number from the arguments
user_limit = sys.argv[1]

# Initiate the class
e = DTCScrapper()

# Create the url
url_dtc = "http://danstonchat.com/"+str(user_limit)+".html"

# Get the results
result_from_scrapper =  e.main(url_dtc)

final_quote = ""

iter = 0

for a in result_from_scrapper:
    if iter % 2 == 0 :
        final_quote += a
    else:
        final_quote += a + "\n"
    iter += 1

print final_quote
