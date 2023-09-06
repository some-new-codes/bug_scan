#!/bin/bash
#code by estalo
OLDIFS="$IFS"    #将for循环的分隔符设为换行符（默认是空格）
IFS=$'\n'     
cd /root/scan/FofaMap-1.1.3/
for keyword in $(cat /root/keyword.txt)  #遍历需要fofa查询的内容，并将每次需要查询的内容带入keyword变量
do

	rm scan_list_ip
	rm scan_list_url
	rm seo_result
	rm top_url_list
	rm seo_result_topname
	rm top_url_list_repeat
	cd /root/scan/FofaMap-1.1.3/
	#fofa查询语句，查询keyword内容，后面的是只查200状态码和限定国内ip的语句
	python3 fofamap.py -q "$keyword && status_code=\"200\" && country=\"CN\" && region!=\"TW\"  && region!=\"HK\" && region!=\"MO\" " #出fofamap.log
	python3 scan_repeat.py			#出scan_list_url和scan_list_ip
	python3 top_url.py 				#出top_url_list
	python3 seo.py 						#出seo_result
	python3 seo_domain.py      #出seo_result
	nuclei -es info,low -l scan_list_url >> /root/scan_result	#出scan_result
done
