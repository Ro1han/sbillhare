#!/usr/bin/env python
#encoding=utf-8
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: 2014-07-15

import UI_template
print 'Content-type:text/html\n'
print
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from zb_module import *

#variables
IP=get_local_ip('eth0')


print """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Carousel Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="http://%s/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="http://%s/bootstrap/dist/js/ie-emulation-modes-warning.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="http://%s/bootstrap/dist/js/ie10-viewport-bug-workaround.js"></script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Custom styles for this template -->
    <link href="http://%s/bootstrap/dist/css/carousel.css" rel="stylesheet">
  </head>
<!-- NAVBAR
================================================== -->
  <body>
    <div class="navbar-wrapper">
      <div class="container">

        <div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">sBillHare</a>
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <li class="Accounts">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu" role="menu">
                    <li><a href="zb_reg.cgi">Register</a></li>
                    <li><a href="#">Manage Account</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li class="divider"></li>
                    <li class="dropdown-header">Help</li>
                    <li><a href="#">Separated link</a></li>
                    <li><a href="#">One more separated link</a></li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>


    <!-- Carousel
    ================================================== -->
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
        <div class="item active">
          <img src="http://%s/bootstrap/dist/images/slide-01.jpg" alt="First slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>Share the bill today.</h1>
              <p>出来混，迟早要还的。</p>
              <p><a class="btn btn-lg btn-primary" href="zb_login.cgi" role="button">Sign up today</a></p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="http://%s/bootstrap/dist/images/slide-02.jpg" alt="Second slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>Register now.</h1>
              <p>Haven't account yet? Come on!</p>
              <p><a class="btn btn-lg btn-primary" href="zb_reg.cgi" role="button">Register</a></p>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="http://%s/bootstrap/dist/images/slide-03.jpg" alt="Third slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>铁公鸡不拔毛? No way!</h1>
              <p>Let's A-A制</p>
              <p><a class="btn btn-lg btn-primary" href="zb_login.cgi" role="button">Come here</a></p>
            </div>
          </div>
        </div>
      </div>
      <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right"></span>
        <span class="sr-only">Next</span>
      </a>
    </div><!-- /.carousel -->



<!-- 
        Marketing messaging and featurettes
        ==================================================    Wrap the rest of the page in another container to center all the content.
        <div class="container marketing">

          Three columns of text below the carousel      <div class="row">
            <div class="col-lg-4">
              <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">
              <h2>Heading</h2>
              <p>Donec sed odio dui. Etiam porta sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.</p>
              <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
            </div>/.col-lg-4        <div class="col-lg-4">
              <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">
              <h2>Heading</h2>
              <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Cras mattis consectetur purus sit amet fermentum. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh.</p>
              <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
            </div>/.col-lg-4        <div class="col-lg-4">
              <img class="img-circle" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" style="width: 140px; height: 140px;">
              <h2>Heading</h2>
              <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
              <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
            </div>/.col-lg-4      </div>/.row
 -->

      <!-- START THE FEATURETTES -->

      <hr class="featurette-divider">

      <div class="row featurette">
        <div class="col-md-7">
          <h2 class="featurette-heading">Feature 1: <span class="text-muted">Email notifications for your actions. Allow you use 2 email addresses.</span></h2>
          <p class="lead">It depends on your decision for booking the weekly report. Allow you to use 2 emails addresses to get the report. Eg. one company email and private email. When you leave the company, what happens? Your company email might be terminated, but here,  you can recieve the last bill report via private email!!!</p>
        </div>
        <div class="col-md-5">
          <img class="featurette-image pull-right" src="http://%s/bootstrap/dist/images/email_icon.jpg" alt="500x500" >
        </div>
      </div>

      <hr class="featurette-divider">

      <div class="row featurette">
        <div class="col-md-5">
          <img class="featurette-image pull-left" src="http://%s/bootstrap/dist/images/pie.png" alt="500x500">
        </div>
        <div class="col-md-7">
          <h2 class="featurette-heading">Feature 2:  <span class="text-muted">Pie Charts for the bills. See for visualized bills.</span></h2>
          <p class="lead">Details are the key.</p>
        </div>
      </div>

      <hr class="featurette-divider">

      <div class="row featurette">
        <div class="col-md-7">
          <h2 class="featurette-heading">Feature 3: <span class="text-muted">Navigators. Supports different size of screen.</span></h2>
          <p class="lead">Allows you manage the bills via the browsers on  PC and also mobile device.</p>
        </div>
        <div class="col-md-5">
          <img class="featurette-image pull-right" src="http://%s/bootstrap/dist/images/phone.png">
        </div>
      </div>

      <hr class="featurette-divider">

      <!-- /END THE FEATURETTES -->


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2014 sBillHare, Inc. &middot; <a href="#">Privacy</a> &middot; <a href="#">Simon Xie</a></p>
      </footer>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://%s/bootstrap/dist/js/jquery.min.js"></script>
    <script src="http://%s/bootstrap/dist/js/bootstrap.min.js"></script>
    <script src="http://%s/bootstrap/dist/js/docs.min.js"></script>
  </body>
</html>


    """%(IP,IP,IP,IP,IP,IP,IP,IP,IP,IP,IP,IP,IP)