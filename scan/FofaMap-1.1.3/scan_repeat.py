import re
import os

re_ip = re.compile("(25[0-5]\.|2[0-4]\d\.|1?[1-9]?\d\.|10\d\.){3}(25[0-5]|2[0-4]\d|1?\d?[0-9])(\:(\d)*)?")
re_ip_http = re.compile("https?://(25[0-5]\.|2[0-4]\d\.|1?[1-9]?\d\.|10\d\.){3}(25[0-5]|2[0-4]\d|1?\d?[0-9])(\:(\d)*)?") 
re_url=re.compile("([\w-]*\.)*[\w-]*\.[a-z]{2,}(\:(\d)*)?(?=\x20)")
re_url_http=re.compile("https?://([\w-]*\.)*[\w-]*\.[a-z]{2,}(\:(\d)*)?(?=\x20)")		
ip_list_http=[]
url_list_http=[]
ip_list=[]
url_list=[]
#code by estalo


def ip_repeat():
	r1 = open('fofamap.log' , 'r' ,encoding='utf-8')
	for line in r1.readlines():
		s1 = re.search(re_ip_http,line)			
		if s1:							
			if s1 not in ip_list_http:
				ip_list_http.append(s1.group())			
	with open('scan_list_ip' , 'a' ,encoding='utf-8') as a:		
		for j in ip_list_http:
			a.write(j+'\n')
	r1.close()


	with open('fofamap.log' , 'r' ,encoding='utf-8') as r1:
		with open('scan_list_ip' , 'r' ,encoding='utf-8') as r:	
			temp = r.read()						
			for lines in r1.readlines():					
				s1_1 = re.search(re_ip,lines)			
				if s1_1:
					re_group=str(s1_1.group())
					test = re.search(re_group,temp)		
					if not test:
						ip_list.append(s1_1.group())

		with open('scan_list_ip' , 'a' ,encoding='utf-8') as a:
			for j in ip_list:
				a.write(j+'\n')	


def url_repeat():
	r2 = open('fofamap.log' , 'r' ,encoding='utf-8')			
	for line in r2.readlines():
		s2 = re.search(re_url_http,line)			
		if s2:
			if s2 not in url_list_http:			
				url_list_http.append(s2.group()) 
	with open('scan_list_url','a',encoding='utf-8') as a:
		for j in url_list_http:
			a.write(j+'\n')
	r2.close()

	with open('fofamap.log' , 'r' ,encoding='utf-8') as r2:
		with open('scan_list_url' , 'r' ,encoding='utf-8') as r:
			temp = r.read()
			for line in r2.readlines():					
				s2_1 = re.search(re_url,line)
				if s2_1:
					re_group=str(s2_1.group())
					test = re.search(re_group,temp)		
					if not test:
						url_list.append(s2_1.group())


		with open('scan_list_url','a',encoding='utf-8') as a:
			for j in url_list:
				a.write(j+'\n')


ip_repeat()
url_repeat()