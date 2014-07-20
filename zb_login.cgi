#!/usr/bin/env python
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: Sat 28 Jun 2014 08:43:56 PM CST
#coding utf-8
print 'Content-type:text/html\n'
print
import md5
import cgi
import UI_template
from db_handle import *
from time import time
from zb_module import *


form = cgi.FieldStorage()

if form.getvalue('session'):
    jump_page("zb_home.cgi?session=%s"%form.getvalue('session'))
else:
    session = time()
    

usr = form.getvalue('username')
password = form.getvalue('password')
# count=int(mysql_show("count","zb_account","names",username)[0][0])

if password:
    pass_m = md5.md5(password).hexdigest()

# def jump_page(target):
#     print '''
# <script language="javascript" type="text/javascript"> 
# window.location.href='%s'; 
# </script>
#     '''%target

UI_template.bootstrap("Zoom Billpin platform")


print """
	
    <div class="container">

      <form class="form-signin" role="form" action="zb_login.cgi" method="post">
        <h2 class="form-signin-heading">Please sign in</h2>
        <input name="username" type="text" class="form-control" placeholder="User Name" required autofocus>
        <input name="password" type="password" class="form-control" placeholder="Password" required>
        <label class="checkbox">
        <input name="keeptime" type="checkbox" value="1"> Remember me
        </label>
        <button name="bootstraplogin" class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>

    </div> <!-- /container -->
"""


if usr and password:
    username = usr.lower()
    pair = mysql_show("names,password","zb_account","names" ,username)[0]
    if pair == (username,pass_m):
        count=int(mysql_show("count","zb_account","names",username)[0][0])
        mysql_session(str(session).split('.')[0],username)
        count=0
        mysql_count_a(count,username)
        if mysql_show("locked","zb_account","names",username)[0][0] == 0:
            jump_page("zb_home.cgi?session=%s"%(str(session).split('.')[0]))
        else:
            print "<h3>Wrong password over 5 times, account %s is locked!</h3>"%username
    else:
        count=int(mysql_show("count","zb_account","names",username)[0][0])
        
        if count < 5:
            count+=1
            mysql_count_a(count,username)
            if mysql_show("locked","zb_account","names",username)[0][0] == 0:
                print "<h3>Wrong password ",count," times</h3>"
            else:
                print "<h3>Wrong password over 5 times, account %s is locked!</h3>"%username

        elif count == 5:
            mysql_lock(username)
            mysql_count_a(count,username)
            jump_page("zb_login.cgi")
        else:
            print "<h3>Wrong password over 5 times, account %s is locked!</h3>"%username

# except:
#     print "<br>No this user, please register!<br>"
#     jump_page("zb_reg.cgi")

# print username
# print mysql_show("count","zb_account","names",username)
print   """
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
<!-- 
        <script src="http://10.0.0.188/bootstrap/dist/js/jquery.min.js"></script>
        <script src="http://10.0.0.188/bootstrap/dist/js/bootstrap.min.js"></script>
 -->
        
  </body>
</html>

"""