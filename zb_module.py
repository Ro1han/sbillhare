#!/usr/bin/env python
# Author: Simon Xie(Simon)
# E-mail: simon.xie@cbsinteractive.com
# Created Time: 2014-07-03 20:24:56

#coding utf-8
from db_handle import *

def jump_page(target,wait=None):
    if wait is None:
        print '''
<script language="javascript" type="text/javascript"> 
window.location.href='%s'; 
</script>
        '''%target
    else:
        print '''
<script language="javascript" type="text/javascript"> 
setTimeout("javascript:location.href=%s", %d); 
</script>        
        '''%(target,wait)

def get_local_ip(ifname):
    import socket, fcntl, struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    ret = socket.inet_ntoa(inet[20:24])
    return ret

def send_email(my_name,sendto_list,contents):
    from email.mime.text import MIMEText
    import smtplib
    text='''\
From: sbillhare@github.com
Subject: Bill for %s

%s    
    '''%(my_name,contents)
    s = smtplib.SMTP('localhost')
    me = 'sbillhare@github.com'
    s.sendmail(me, sendto_list,text)
    s.quit()

# In [2]: my_name='nina'
# 
# In [3]: bill_I_paid=mysql_show("bill_id,names,location,timestamp,everage","`zb_account` LEFT JOIN `zb_bills` on `zb_account`.`name_id` =`zb_bills`.`payer_id`","names",my_name,2)
# 
# In [4]: bill_I_paid[0][-1]
# 29.33
# 
# In [5]: who_owes_me(bill_I_paid[0][0],my_name,bill_I_paid[0][-1])
# {u'simon': 29.33, u'nolan': 29.33}    

def other_users(my_name):
    name_dict={}
    who_owes_me={}
    for each in mysql_show("name_id,names","zb_account","names",my_name,1):
        name_dict[each[0]]=each[1]
    return name_dict

def who_owes_me(bill_id,my_name,everage):
    name_dict={}
    who_owes_me={}
    for each in mysql_show("name_id,names","zb_account","names",my_name,1):
        name_dict[each[0]]=each[1]
#     name_dict=other_users(my_name)
    for x in range(2,len(mysql_show("*","zb_share","bill_id",bill_id)[0])):
        if mysql_show("*","zb_share","bill_id",bill_id)[0][x]==1:
            who_owes_me[name_dict[int(mysql_decs("zb_share")[x][0])]]=everage
    return who_owes_me
    
# In [2]: they_owe_me('simon')
# {10L: {u'nina': 25.0, u'nolan': 25.0, u'anna': 25.0}, 26L: {u'nina': 166.67, u'anna': 166.67}, 27L: {u'daniel': 50.0}, 28L: {u'nina': 166.67, u'anna': 166.67}, 29L: {u'nina': 166.67, u'anna': 166.67}, 30L: {u'jerry': 50.0}}
def they_owe_me(my_name):    
    bill_I_paid=mysql_show("bill_id,names,location,timestamp,everage","`zb_account` LEFT JOIN `zb_bills` on `zb_account`.`name_id` =`zb_bills`.`payer_id`","names",my_name,2)
    they_owe_me={}
    for x in range(len(bill_I_paid)):
        if bill_I_paid[x][0] is not None:
            they_owe_me[bill_I_paid[x][0]]=who_owes_me(bill_I_paid[x][0],my_name,bill_I_paid[x][-1])
        else:
            they_owe_me=None
    return they_owe_me

# In [2]: money_items('simon')
# {u'nolan': 25.0, u'jerry': 50.0, u'nina': 525.01, u'aaron': 0, u'daniel': 50.0, u'anna': 525.01}    
def money_items(my_name):
    money={}
    otu=other_users(my_name)
    for x in otu.viewvalues():
        money.setdefault(x,0)
    tom=they_owe_me(my_name)
    if tom is not None:
        for y in tom:
            for x in tom[y]:
                if x in money:
                     m=money[x]
                     money[x]=m+tom[y][x]
    return money
    
#functions for tables and charts:
def caculate(my_name,I_owe=None):
    output, f_o_m, I_o_f = {}, {}, {}

    money=money_items(my_name)
    for x in money.keys():
        f_o_m[x]=money[x]
    for his_name in other_users(my_name).values():
        he_paid=money_items(his_name)
        if my_name in he_paid:
            I_o_f[his_name]=he_paid[my_name]
    for x in I_o_f:
        if I_owe is not None:
            if I_o_f[x]-f_o_m[x] > 0:
                output[x]=I_o_f[x]-f_o_m[x]
        else:
            if f_o_m[x]-I_o_f[x] > 0:
                output[x]=f_o_m[x]-I_o_f[x]
    return  output    


def draw(my_name,I_owe=None):
    try:
        output = caculate(my_name,I_owe)
        other_list = output.keys()
        for his_name in other_list[:-1]:
            print "[\'%s\',%.2f],"%(his_name,output[his_name])
        print '''
            {
            name: \' %s\',
            y: %.2f,
            sliced: true,
            selected: true
            }
        '''%(other_list[-1],output[other_list[-1]])
    except IndexError:
        print "[\'%s\',%.2f]"%(None,0)

def table_detail(my_name,I_owe=None):
    try:
        output = caculate(my_name,I_owe)
        other_list = output.keys()
        for his_name in other_list:
            print '''
            <tr>
                <td>%s</td>
                <td>%.2f</td>
            </tr>
            '''%(his_name,output[his_name])        
    except IndexError:
        print '''
                <tr>
                    <td>%s</td>
                    <td>%.2f</td>
                </tr>
            '''%(None,0)