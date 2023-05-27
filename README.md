# bug_scan
批量扫漏洞脚本
#### 项目介绍
这是一个结合fofa和nuclei的批量漏洞扫描脚本，能够根据给出的关键词进行批量化扫描


#### 使用步骤

###### 给予bug\_scan.sh执行权限

scan文件下载好放到/root文件下，进入/root/scan文件内，给予执行权限chmod u+x bug\_scan.sh

###### keyword.txt（搜索关键词文件）放到/root目录下

keyword内容为我们要搜索的语句的内容
keyword.txt内容格式为,与fofa查询语句格式一致：

```
title="xxx" && after="2022-1-6"
title="xxx" && after="2022-1-10"
```

###### 填写fofa配置(需要fofa会员)

我们将fofamap的配置文件fofa.ini中email和key填写（最好是旧高级会员账号的key），以及根据自己的需求填写其他配置内容即可，而logger一定要设置为on，因为我们就是从日志文件fofamap.log中提取扫描目标的。

###### 最后一步

执行/root/scan/bug.scan.sh文件，就会开始循环keyword.txt内搜索关键词进行扫描，最后输出结果放在/root/scan\_result内，cat /root/scan\_result即可


## 题外话

关键词搜的好，cnvd证书也不在话下
