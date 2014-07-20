#!/usr/bin/env python
#encoding=utf-8
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: Sat 28 Jun 2014 05:12:48 PM CST



import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def mysql_conn():
	conn = MySQLdb.connect(db='pythonDB',host='localhost',user='root',passwd='mysql123',charset='utf8')
	return conn

def mysql_show(field,table,where=None,value=None,opt=None):
    #opt : 1 = unequal,2 = join
	conn=mysql_conn()
	curs = conn.cursor()
	if where is None:
	    sql = 'SELECT %s FROM `%s` '%(field,table)
	elif opt is None:
	    sql = 'SELECT %s FROM `%s` where `%s` = \'%s\' '%(field,table,where,value)
	elif opt == 2:
	    sql = 'SELECT %s FROM %s where `%s` = \'%s\' '%(field,table,where,value)
	else:
	    sql = 'SELECT %s FROM `%s` where `%s` != \'%s\' '%(field,table,where,value)
	#print sql
	curs.execute(sql)
	conn.commit()
	rows = curs.fetchall()
	curs.close()
	conn.close()
	return rows

def mysql_drop(table,field):
	conn=mysql_conn()
        curs = conn.cursor()
        sql = 'ALTER TABLE `%s`  DROP  `%s` '%(table,field)
        curs.execute(sql)
        conn.commit()
        rows = curs.fetchall()
        curs.close()
	conn.close()
        return rows


def mysql_new_c(table,field,Type):

	conn=mysql_conn()
        curs = conn.cursor()
        sql = 'ALTER TABLE `%s`  ADD  `%s` %s'%(table,field,Type)
        curs.execute(sql)
        conn.commit()
        rows = curs.fetchall()
        curs.close()
	conn.close()
        return rows

def mysql_new_account(name,c_mail,p_mail,passwd):
    conn=mysql_conn()
    curs = conn.cursor()
    sql = 'INSERT INTO  `zb_account` (`names`,`corp_mail`,`pri_mail`,`password`) VALUES (\'%s\' , \'%s\' ,\'%s\' ,\'%s\')'%(name,c_mail,p_mail,passwd)
    #print sql
    try:
        curs.execute(sql)
        conn.commit()
        curs.fetchall()
        curs.close()
        conn.close()
        rc = 1
    except:
        print "<h3 style=color:red>User %s already exsists, Please try others!</h3>"%name
        print """<br>
		<button name="bootstraplogin" class="btn btn-lg btn-primary btn-block" type="submit">Register</button>
      </form>

    </div> <!-- /container -->"""
        rc= 0
    
    rows = mysql_show("name_id","zb_account","names",name)
    #print "rows:",rows
    try:
        if len(rows[0])>1:
            print "Account  already exsists!"
            rc = 0
            sys.exit()
        elif rows:
            name_id=rows[0][0]
            mysql_new_c("zb_share",name_id,"INT")
    except:
        #print "Failed to insert!"
        rc = 0
        
    return rc

def mysql_session(session,name):
    conn=mysql_conn()
    curs = conn.cursor()
    sql= 'UPDATE `zb_account` SET `session_start`=\'%s\' WHERE `names`=\'%s\''%(session,name)
    #sql= 'update `zb_account` set `session_start`=%f where `names`= \'%s\' '%(session,name)
    curs.execute(sql)
    conn.commit()
    curs.fetchall()
    curs.close()
    conn.close()
    rc = 1 
    return rc  
    
def mysql_count_a(num,name):
    conn=mysql_conn()
    curs = conn.cursor()
    sql= 'UPDATE `zb_account` SET `count`=%d WHERE `names`=\'%s\''%(num,name)
    #sql= 'update `zb_account` set `session_start`=%f where `names`= \'%s\' '%(session,name)
    curs.execute(sql)
    conn.commit()
    curs.fetchall()
    curs.close()
    conn.close()
    rc = 1 
    return rc  

def mysql_lock(name):
    conn=mysql_conn()
    curs = conn.cursor()
    sql= 'UPDATE `zb_account` SET `locked`=1 WHERE `names`=\'%s\''%(name)
    #sql= 'update `zb_account` set `session_start`=%f where `names`= \'%s\' '%(session,name)
    curs.execute(sql)
    conn.commit()
    curs.fetchall()
    curs.close()
    conn.close()
    rc = 1 
    return rc    
    
def mysql_bill_a(timestamp,people_number,total_amount,payer_id,everage,session,location=None):
    conn=mysql_conn()
    curs = conn.cursor()
    if location:
        sql = 'insert into zb_bills (`timestamp`,`people_number`,`total_amount`,`payer_id`,`everage`,`location`) values (\'%s\',%d,%.2f,%d,%.2f,\'%s\')'%(timestamp,people_number,total_amount,payer_id,everage,location)
    else:
        sql = 'insert into zb_bills (`timestamp`,`people_number`,`total_amount`,`payer_id`,`everage`) values (\'%s\',%d,%.2f,%d,%.2f)'%(timestamp,people_number,total_amount,payer_id,everage)
  
    curs.execute(sql)

       #  print e
#         rc = 0
#         print "<h2>Please Don't input Chinese Character, USE English!!</h2>"
#         print "<a href=zb_home.cgi?session=%s>Add bill</a>"%session
#         sys.exit(0)
    conn.commit()
    curs.fetchall()
    curs.close()
    conn.close()
    rc = 1 
    return rc 
    
    
def mysql_share_a(bill_id,debtor_number,debtors_list):
    #insert into `zb_share` (`bill_id`,`debtor_number`,`3`,`8`) values (1,2,1,1);
    field=''
    values=''
    for d in debtors_list:
        field+=',`%s`'%d
    for v in debtors_list:
        values+=',1'
    conn=mysql_conn()
    curs = conn.cursor()
    sql='insert into `zb_share` (`bill_id`,`debtor_number`%s) values(%s,%s%s);'%(field,bill_id,debtor_number,values)
    print "sql: %s"%sql
    curs.execute(sql)
    conn.commit()
    curs.fetchall()
    curs.close()
    conn.close()
    rc = 1 
    return rc

def mysql_decs(table):
    conn=mysql_conn()
    curs = conn.cursor()
    sql= 'desc %s'%table
    curs.execute(sql)
    conn.commit()
    fields=curs.fetchall()
    curs.close()
    conn.close()
    return fields    
        
    
#mysql_new_c('zb_share',7,'INT')
#mysql_action('zb_share','DROP',8)
#In [2]: mysql_show('*','zb_account')
#Out[2]: ((1L, 'Simon'), (2L, 'Daniel'))
