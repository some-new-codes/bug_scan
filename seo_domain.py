import re

#从有seo权重的顶级域名结果中（顶级域名），匹配scan_list_url（获取包括子域名的域名）内容并导出到seo_result

a = open('seo_result','a',encoding='utf-8')

with open('seo_result_topname','r',encoding='utf-8') as r:
	for i in r.readlines():
		i = i.strip()
		for j in open('scan_list_url','r',encoding='utf-8'):
			j=j.strip()
			if i in j:
				a.write(j+'\n')


a.close()
