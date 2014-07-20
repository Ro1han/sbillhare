#!/usr/bin/env python
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: Sat 28 Jun 2014 08:43:56 PM CST
#coding utf-8
print 'Content-type:text/html\n'
print
from db_handle import *
from zb_module import *
import cgi
import sys
import md5
import UI_template
form = cgi.FieldStorage()

# try:
#     session=form.getvalue('session') 
#     if session:
#         jump_page("zb_home.cgi?session=%s"%session)
# except:
#     pass


username = form.getvalue('username')
corpmail = form.getvalue('corpmail')
private = form.getvalue('private')
pass1 = form.getvalue('pass1')
pass2 = form.getvalue('pass2')
if pass1:
    pass_m = md5.md5(pass1).hexdigest()
# print username,corpmail,private,pass1,pass2
# if type(username) is str:
#     print "aaa"

UI_template.bootstrap("Apply account for sBillHare")

print '''

<!-- 
    <h1>Apply account for sBillHare</h1>
	<form action='zb_reg.cgi' method='POST'>
	UserName:	<input type="txt" name="username" value=""/><br>
	Corpmail:	<input type="txt" name="corpmail" value="xxx@cbsinteractive.com"/><br>
	PrivateMail	<input type="txt" name="private" value="888@qq.com"/><br>
	Password:	<input type="password" name="pass1" value=""/><br>
	Re-password:	<input type="password" name="pass2" value=""/>
    <div class="container">
 -->

      <form class="form-signin" role="form" action="zb_reg.cgi" method="post">
        <h2 class="form-signin-heading">Register account</h2>
        <input name="username" type="text" class="form-control" placeholder="User Name" required autofocus>
        
        <span class="help-block">Please add your company email:</span>
        <div class="form-group">
            <div class="input-group">
              <div class="input-group-addon">@</div>
              <input name="corpmail" class="form-control" type="email" placeholder="xxx@cbsinteractive.com" required>
            </div>
        </div>
        
        <span class="help-block">Please add your private email:</span>
        <div class="form-group">
            <div class="input-group">
              <div class="input-group-addon">@</div>
              <input name="private" class="form-control" type="email" placeholder="xxx@qq.com" required>
            </div>
        </div>
                
        <span class="help-block">Password Must be longer than 8 characters!</span>
        <input name="pass1" type="password" class="form-control" placeholder="Password" required>
        <input name="pass2" type="password" class="form-control" placeholder="Re-Password" required>
        <span class="help-block">Select if you need email report every week:</span>
        <label class="checkbox">
        <input name="digest" type="checkbox" value="1"> Email Digest
        </label>
        



'''
if pass1 != pass2:
    print """
	<br>
		<button name="bootstraplogin" class="btn btn-lg btn-success btn-block" type="submit">Register</button>
      </form>

    </div> <!-- /container -->
    <h3 style=color:red align="center">Twice Passwords not matched!! Please re-try!!</h3><br>
    
"""

else:
	if pass1 and len(pass1)<8 :
		print """
		<br>
		<button name="bootstraplogin" class="btn btn-lg btn-success btn-block" type="submit">Register</button>
      </form>

    </div> <!-- /container -->
    <h3 style=color:red>Password needs to be longer than 8!!!</h3>
		"""
	elif pass1:
		#print "Matched, go to db!"
		print "<br>"
		rc=mysql_new_account(username.lower(),corpmail,private,pass_m)
		if rc:
		    jump_page("zb_login.cgi")
# 		    print "<h3 style=color:red>Successful</h3>"
# 		    print "<br><a href='zb_login.cgi'>go to Login</a>"
        else: 
            print """<br>
		<button name="bootstraplogin" class="btn btn-lg btn-success btn-block" type="submit">Register</button>
      </form>

    </div> <!-- /container -->"""

print '''
 </body>
</html>
'''



