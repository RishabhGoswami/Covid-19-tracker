#!/usr/bin/env python
# coding: utf-8

# In[3]:

import requests
import bs4
re=requests.get("https://www.worldometers.info/coronavirus/")
a=bs4.BeautifulSoup(re.text,'lxml')
z=a.select('.maincounter-number')[0].span.text
d=a.select('.maincounter-number')[1].span.text
c=a.select('.maincounter-number')[2].span.text
from plyer import notification
if __name__=='__main__':
    notification.notify(
    title='corona',
    message='Total cases in world '+str(z)+'\n'+'Total deaths in world ' +str(d) +'\n'+ 'Total people recovered'+str(c),
    timeout=10
    )


# In[ ]:




