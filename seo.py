import re
import requests
import time
from fake_useragent import UserAgent
from urllib.error import HTTPError

#查询顶级域名seo,输出为seo_result_topname


def get_data():
    r = open('top_url_list','r',encoding='utf-8')
    for domain in r.readlines():                                                    #seo查询
        domain = domain.strip()
        result_pc = get_pc(domain)
        result_mobile = get_mobile(domain)
        time.sleep(0.1)
        # if (result_mobile is None or result_pc is None):
        #     continue
        if(result_mobile is None or result_pc is None):
            continue
        if(result_mobile > 0 or result_pc > 0 ):
            with open('seo_result_topname' , 'a' ,encoding = 'utf-8') as a:
                a.write(domain+'\n')    
        else:
            continue
        #except Exception as u:
            #break
    r.close()

def get_pc(domain):
    ua_header = UserAgent()
    url_pc = "https://baidurank.aizhan.com/api/br?domain={}&style=text".format(domain)
    url_mobile = "https://baidurank.aizhan.com/api/mbr?domain={}&style=text".format(domain)
    headers = {
        'Host': 'baidurank.aizhan.com',
        'User-Agent': ua_header.random,
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': ''
    }
    try:
        response_pc = requests.get(url_pc, headers=headers,timeout=15)
        pc = pc_re(response_pc.text,domain)
        return pc
    except HTTPError:
        time.sleep(3)
        return get_pc(domain)
    except IndexError:
        pass
    except requests.exceptions.ReadTimeout:
        pass

def get_mobile(domain):
    ua_header = UserAgent()
    url_mobile = "https://baidurank.aizhan.com/api/mbr?domain={}&style=text".format(domain)
    headers = {
        'Host': 'baidurank.aizhan.com',
        'User-Agent': ua_header.random,
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': ''
    }
    try:
        response_mobile = requests.get(url_mobile, headers=headers,timeout=15)
        mobile = mobile_re(response_mobile.text,domain)
        return mobile
    except HTTPError:
        time.sleep(3)
        return get_mobile(domain)
    except IndexError:
        pass
    except requests.exceptions.ReadTimeout:
        pass

def pc_re(response,domain):            #匹配权重值，并将权重大于0的url导出
    pc_rank = re.findall(re.compile(r'>(.*?)</a>'),response)[0]
    try:
        pc = int(pc_rank[0])
    except ValueError:
        pass
    if pc is not None:
        return pc

def mobile_re(response,domain):         #匹配权重值，并将权重大于0的url导出
    mobile_rank = re.findall(re.compile(r'>(.*?)</a>'),response)[0]
    try:
        mobile = int(mobile_rank[0])
    except ValueError:
        pass
    if mobile is not None:
        return mobile

get_data()


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
