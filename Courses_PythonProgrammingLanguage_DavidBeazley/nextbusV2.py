#!/usr/bin/env python
# coding: utf-8

# In[16]:


#nextbusV2.py
#!/usr/bin/env python3

import sys
if len(sys.argv) != 3:
    raise SystemExit('Usage:nextbus.py route stopid')
    
route = sys.argv[1]
stopid = sys.argv[2]

import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid))
data = u.read()

from xml.etree.ElementTree import XML
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)


# In[29]:


get_ipython().run_line_magic('run', 'nextbusV2.py 22 14787')

