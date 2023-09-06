import re
import os

#输出顶级域名top_url_list，并且不重复
			

r = open('scan_list_url','r',encoding='utf-8')			#匹配出顶级域名，会带重复的top_url_list_repeat
for domain_temp in r.readlines():
	try:
		domain = re.search(re.compile('[\w-]*\.((com|edu|gov|org|net)\.)?([a-z]{2,4})((?=\n)|(?=\:))'),domain_temp).group() 
	except AttributeError:
		continue 
	if domain:
		with open('top_url_list_repeat' , 'a' ,encoding = 'utf-8') as a:
			a.write(domain+'\n')

temp_list = []

with open('top_url_list_repeat' , 'r' ,encoding='utf-8') as r:			#任一行不存在temp_list内则添加到temp_list内，相当于去重
	for lines in r.readlines():	
		if lines not in temp_list:
			temp_list.append(lines)		

with open('top_url_list' , 'a' ,encoding='utf-8') as w:
	for i in temp_list:
		w.write(i)

os.remove('top_url_list_repeat')			#删除未去重文件
