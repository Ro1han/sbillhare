#!/usr/bin/env python
#encoding=utf-8
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: 2014-07-13 CST

print 'Content-type:text/html\n'
print
import md5
import cgi
import UI_template
from time import time
from zb_module import *

#variables
jump=0
IP=get_local_ip('eth0')
form = cgi.FieldStorage()
session = form.getvalue('session')
try:
    I_owe= form.getvalue('I_owe')
except:
    I_owe = None
    
if I_owe is  None:
    phrase= 'Friends totally owe me: '
else:
    phrase='I totally owe friends: '

try:
    if session != 'None':    
        my_name=mysql_show('names','zb_account','session_start',session)[0][0]
        total=0
   

        for x in caculate(my_name,I_owe).values():
            total+=x
    else:
        my_name=None
        total=0
except IndexError:
    my_name=None
    total=0

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
          <h1 class="page-header">Hello %s ^^</h1>

          <div class="row placeholders">
            <div id="container" style="min-width:800px;height:400px"></div>
			<script type="text/javascript">
				$(function () {
                        $('#container').highcharts({
                            chart: {
                                plotBackgroundColor: null,
                                plotBorderWidth: null,
                                plotShadow: false
                            },
                            title: {
                                text: 'Bill share'
                            },
                            tooltip: {
                                pointFormat: '{series.name}: <b>{point.percentage:.1f}%%</b>'
                            },
                            plotOptions: {
                                pie: {
                                    allowPointSelect: true,
                                    cursor: 'pointer',
                                    dataLabels: {
                                        enabled: true,
                                        color: '#000000',
                                        connectorColor: '#000000',
                                        format: '<b>{point.name}</b>: {point.percentage:.1f} %%'
                                    }
                                }
                            },
                            series: [{
                                type: 'pie',
                                name: 'Bill share',
                                data: [
'''%(session,session,session,session,session,session,session,my_name)                               



# draw the charts
# try:
if my_name:
    draw(my_name,I_owe)
# except IndexError:
#     jump=1

# data details in table                            
print      '''                           


                                ]
                            }]
                        });
                    });				
				</script>
		  </div>

          <h2 class="sub-header">%s :￥%.2f</h2>
          <div class="table-responsive">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>Friend Name</th>
                  <th>Owes me</th>
                </tr>
              </thead>
              <tbody>


'''%(phrase,total)

# try:
if my_name:
    table_detail(my_name,I_owe)
# except IndexError:
#     jump=1

#eding tags                
print '''

              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
'''
if jump==1:
    jump_page('zb_add.cgi?session=%s'%session)
    sys.exit()
    
if session == 'None' or my_name is None:
    jump_page('sbillhare.cgi')

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

# //                                     ['Nina',   20],
# //                                     ['Daniel',       50],
# //                                     {
# //                                         name: 'Nolan',
# //                                         y: 30,
# //                                         sliced: true,
# //                                         selected: true
# //                                     }