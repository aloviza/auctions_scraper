# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
# print the variable html containing the webpage 
# print(html)

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("div[class='property-details-left']")

# Find something on the page using css selectors
root = lxml.html.fromstring(html)
#Change "li p a" to a different CSS selector to grab something else
#Look for an a tag inside a p tag inside an li tag
#Store the matches in 'matchedlinks'
matchedlinks = root.cssselect("li p a")
#print that
print(matchedlinks)
  
# "div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
