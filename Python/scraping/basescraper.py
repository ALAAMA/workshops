from lxml import etree
import csv     
import urllib
import re
f = open('/tmp/files.csv','w')
entries = ["Day","Month","Year","Title","Remote","Local"]
c = csv.DictWriter(f,entries)


destpath = '/tmp/'
fname = '/tmp/page1.html'
fp = open(fname, 'rb')
parser = etree.HTMLParser()
tree   = etree.parse(fp, parser)
dateelems = tree.xpath('.//span[@class="date-display-single"]')
linkelems = tree.xpath('.//div[@class="views-field-title"]/span[@class="field-content"]/a')
for (d,l) in zip(dateelems,linkelems):
    entry = dict()
    myDate = d.text.split()
    urlname = l.get('href')
    nodenum = re.search("\d+",urlname).group()
    dest = destpath+nodenum+".html"
    urllib.urlretrieve (urlname,dest)
    entry["Day"] = myDate[0]
    entry["Month"] = myDate[1]
    entry["Year"] = myDate[2]
    entry["Local"] = dest
    entry["Remote"] = urlname
    entry["Title"] = l.text.encode("utf-8")
    c.writerow(entry)
    print entry
     
f.close()
fp.close()
