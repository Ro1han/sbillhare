#!/usr/bin/env python
#encoding=utf-8
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: 2014-07-06

import UI_template
print 'Content-type:text/html\n'
print
import cgi
import time
import datetime
import db_handle
from db_handle import *
from zb_module import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# variables
form = cgi.FieldStorage()
home_time = form.getvalue('home_time')
session = form.getvalue('session')
bill_time=time.time()
if float(bill_time) - float(home_time) >60:
    print "This page has been opened for so long, please refresh!"
    jump_page("zb_add.cgi?session=%s"%session)
    sys.exit()
#ids is the string including other users' id
ids = form.getvalue('ids')
#check_list is listing everybody, non-relavent with checkbox.
check_list=[]
# bill is the dict:: key=>debtor_id, vaule=>1
bill={}
for x in range(10):
    print "<br>"
check_list=ids.split("_")[:-1] 
for e in check_list:
    if form.getvalue(e):
        bill[e]=form.getvalue(e)

my_name=form.getvalue('my_name')

# fileds needed in table zb_share
#bill_id
debtor_number = len(bill.keys())
# bill.keys() will be the list of the debtor_ids

# fileds needed in table zb_bills
location = form.getvalue('location')
timestamp = str(datetime.datetime.today()).split('.')[0]
people_number = debtor_number + 1
total_amount = float(form.getvalue('total'))
payer_id = form.getvalue('my_name_id')
everage = "%.2f"%(total_amount / people_number)

# db stuffs
mysql_bill_a(timestamp,people_number,total_amount,int(payer_id),float(everage),session,location)
bill_id = mysql_show("*","zb_bills","timestamp",timestamp)[0][0]
mysql_share_a(bill_id,debtor_number,bill.keys())

# print the bootstrap template
UI_template.bootstrap("Bill bill bill",session)

#test
print check_list


print """
<br>location: %s
<br>timestamp: %s
<br>people_number: %s
<br>total_amount: %s
<br>payer_id: %s
<br>everage: %s
<br>debtors: %s
<br>bill_id: %s
"""%(location,timestamp,people_number,total_amount,payer_id,everage,bill.keys(),bill_id)



print "<a href='zb_home.cgi?session=%s'>Back</a>"%session

jump_page("zb_details.cgi?session=%s"%session)

# tag endings
print """
  </body>
</html>

"""