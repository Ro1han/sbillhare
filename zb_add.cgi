#!/usr/bin/env python
#encoding=utf-8
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: Tue 01 Jul 2014 10:03:06 PM CST

import UI_template
print 'Content-type:text/html\n'
print
import cgi
from db_handle import *
from zb_module import *
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
# variables
home_time = time.time()
form = cgi.FieldStorage()
session = form.getvalue('session')
ids=""
if session and session !='None' and session !='%s':
    my_name_id,my_name = mysql_show("name_id,names","zb_account","session_start",session)[0]
    other_users=mysql_show("name_id,names","zb_account","names",my_name,1)
    for x in other_users:
        ids+=str(x[0])+"_"
else:
    my_name_id,my_name=None,''
    other_users,session=None,None


# import the bootstrap template
UI_template.bootstrap("Welcom "+my_name,session)

# test fileds
print "<br>session is : ",session
print "<br>my name is: ",my_name
print "<br>id is:",my_name_id


# list other users in checkbox: mysql_show("name_id,names","zb_account","names","simon",1)
def list_users(id,name):
    print """
  <div class="form-group">
        <div class="col-sm-10">
            <div class="checkbox">
                <label  class="control-label">
                <input  name =%s type="checkbox"> %s 
                </label>
            </div>
            <!-- <input type="txt" class="form-control"  placeholder="Amount" > -->
        </div>
  </div>          
    """  %(id,name)
    
print """
    <div class="container">
      <form class="form-inline" role="form" action="zb_bill.cgi?session=%s&ids=%s" method="post">
        <h2 class="form-signin-heading">Add bill</h2>
        <input name="total" type="text" class="form-control" placeholder="Total Amount" required autofocus> 
        <input name="location" type="text" class="form-control" placeholder="Location" required>
        <input name="my_name" type="hidden" value =%s >
        <input name="my_name_id" type="hidden" value =%s >
        <input name="home_time" type="hidden" value =%s >
"""  %(session,ids,my_name,my_name_id,home_time)    

     
if other_users is not None:
    for (x,y) in other_users:
        list_users(x,y)
        
print """        
        
        <button name="bootstraplogin" class="btn btn-lg btn-danger btn-block" type="submit">Add bill</button>
      </form>

    </div> <!-- /container -->

"""

if session is None:
    jump_page('zb_login.cgi')
elif float(home_time) - float(session) >600:
    jump_page("zb_logout.cgi")


# tag endings
print """
  </body>
</html>

"""