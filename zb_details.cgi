#!/usr/bin/env python
#encoding=utf-8
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: 2014-07-19

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

#variables
all_users=[]
for each in mysql_show("names","zb_account"):
     all_users.append(each[0])
jump=0
IP=get_local_ip('eth0')
form = cgi.FieldStorage()
session = form.getvalue('session')
bill_tuple = mysql_show("bill_id,location,timestamp,everage,payer_id,total_amount","zb_bills")
bills_list = list(bill_tuple)
bills_list.reverse()

try:
    if session != 'None':    
        my_name=mysql_show('names','zb_account','session_start',session)[0][0]
    else:
        my_name=None
except IndexError:
    my_name=None

# UI bootstrap header
print '''

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    <title>History</title>

    <!-- Bootstrap core CSS -->
    <link href="http://%s/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="http://%s/bootstrap/dist/css/dashboard.css" rel="stylesheet">

	<script type="text/javascript" src="http://%s/bootstrap/dist/js/jquery.min.js"></script>
	<script type="text/javascript" src="http://%s/highcharts/js/highcharts.js"></script>
  </head>
'''%(IP,IP,IP,IP)

#Left side bar
print '''
  <body>


	 <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
			<div class="navbar-header">
				  <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				  </button>
				  <a class="navbar-brand" href="zb_login.cgi?session=%s"><img src="../../bootstrap/dist/images/logo-1.png">sBillHare</a>
			</div>
			<div class="collapse navbar-collapse">
			  <ul class="nav navbar-nav">
				<li class="active"><a href="zb_home.cgi?session=%s">Home</a></li>
				<li><a href="zb_reg.cgi?session=%s">Register</a></li> 
				<li><a href="zb_logout.cgi">Log out</a></li> 
				 
			  </ul>
			</div><!--/.nav-collapse -->
		</div>
    </div>


    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li class="active"><a href="zb_home.cgi?session=%s">Friends Owe me</a></li>
            <li><a href="zb_home.cgi?session=%s&I_owe=yes">I Owe Friends</a></li>
            <li><a href="zb_details.cgi?session=%s">Bills Details</a></li>
            <li><a href="zb_add.cgi?session=%s">Add New Bill</a></li>
          </ul>
        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
          <h1 class="page-header">Hi %s ^^</h1>
'''%(session,session,session,session,session,session,session,my_name)



# Display the table

print '''
          <div class="table-responsive">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Bill Id</th>
                  <th>location</th>
                  <th>When</th>
                  <th>Everage</th>
                  <th>Payer</th>
                  <th>Total Amount</th>
                  <th>Debtors</th>
                </tr>
              </thead>
              <tbody>
'''

for bill in bills_list:
    debtors = ''
    bill_id,location,timestamp,everage,payer_id,total_amount = bill
    payer_name = mysql_show("names","zb_account","name_id",payer_id)[0][0]
    for who in they_owe_me(payer_name)[bill_id].keys():
        debtors+=who+", "
    print '''
    <tr>
        <td>%d</td>
        <td>%s</td>
        <td>%s</td>
        <td>%.2f</td>
        <td>%s</td>
        <td>%.2f</td>
        <td>%s</td>
    </tr>
    '''%(bill_id,location,timestamp,everage,payer_name,total_amount,debtors)    

print '''

              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
'''


#footer
print '''
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://%s/bootstrap/dist/js/bootstrap.min.js"></script>
    <script src="http://%s/bootstrap/dist/js/docs.min.js"></script>
  </body>
</html>

'''%(IP,IP)