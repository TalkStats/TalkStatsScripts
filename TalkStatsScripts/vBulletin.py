import mechanize
from getpass import getpass

usr = "Dason"
sitename = "http://www.talkstats.com/"
thread_number = "23161"
post = "Last test post... I swear"

message = "Hi " + usr + ". Please enter your talkstats password: "
pas = getpass(prompt = message)

br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open(sitename)
 
br.select_form(nr=0)
br["vb_login_username"] = usr
br["vb_login_password"] = pas
br.submit()

url_newpost = sitename + "newreply.php?t=" + thread_number
br.open(url_newpost)
br.select_form(nr=1)
br["message"] = post
sentPost = br.submit()

