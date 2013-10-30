import json
import urllib
from time import sleep
import pycurl as pc
import StringIO

# download a file
def download2file(url,count,path='./'):
    c = pc.Curl()
    c.setopt(pc.URL,url)
    b = StringIO.StringIO()
    c.setopt(pc.WRITEFUNCTION, b.write)
    c.perform()
    fname = "{0}{1}{2}".format(path,count,url.split('/')[-1])
    f = open(fname, 'wb')
    f.write(b.getvalue())
    f.close()
    return fname

# get the api key
fp = open('api.key','ra')
line = fp.readline()
fp.close()
apikey = line[0:len(line)-1]
url = 'http://octopart.com/api/v3/parts/match?'
# use plus to concat search terms
url += '&queries=[{"q":"atmega"}]' # this is a text query
url += '&apikey='
url += apikey
url += '&include[]=imagesets'
print url
data = urllib.urlopen(url).read()
response = json.loads(data)
#print response
# print request time (in milliseconds)
#if len(response['results']) == 1:
#    print "Got nuthin'"
#    exit(0)
    
print response['msec']
print "Got {0} items.".format(len(response['results']))
count = 0
# go through the results and download
print response['results']
for result in response['results']:
    for item in result['items']:
        for k,v in item.items():
            if( k == 'imagesets' ):
                for img in v:
                    for k2,v2 in img.items():
                        #print "{0}->{1}".format(k2,v2)
                        if 'image' in k2 and v2:
                            url = str(v2['url'])
                            print download2file(url,count)
                            count += 1 
