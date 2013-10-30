import json
import urllib
from SimpleCV import *
from time import sleep
fp = open('api.key','ra')
line = fp.readline()
fp.close()
apikey = line[0:len(line)-1]
print "."+apikey+"."
url = 'http://octopart.com/api/v3/parts/match?'
url += '&queries=[{"q":"atmega"}]'
url += '&apikey='
url += apikey
url += '&include[]=imagesets'
print url
data = urllib.urlopen(url).read()
response = json.loads(data)

# print request time (in milliseconds)
print response['msec']


#print response['results']
for result in response['results']:
    for item in result['items']:
        for k,v in item.items():
            #print k
            if( k == 'imagesets' ):
                for img in v:
                    for k2,v2 in img.items():
                        print "{0}->{1}".format(k2,v2)
                        if k2 == 'swatch_image':
                            print v2['url']
                            test = str(v2['url'])
                            if(test.lower().startswith('http://')):
                                print "dafuq"
                                img = Image(str(v2['url']))
                                img.show()
                                sleep(1)
                            
