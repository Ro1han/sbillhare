#!/usr/bin/env python
from zb_module import *
IP=get_local_ip('eth0')

def bootstrap(title,session=None):
    print """
<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">

    <title>%s</title>

    <!-- Bootstrap core CSS -->

    <link href="http://%s/bootstrap/dist/css/bootstrap.css" rel="stylesheet">
    <link href="http://%s/bootstrap/dist/css/signin.css" rel="stylesheet">
  </head>

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
	<!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->

        <script src="http://%s/bootstrap/dist/js/jquery.min.js"></script>
        <script src="http://%s/bootstrap/dist/js/bootstrap.min.js"></script>        
    """%(title,IP,IP,session,session,session,IP,IP)