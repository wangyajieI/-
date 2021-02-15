# -烂笔头
## 1、git 基础
### 1.1 clone别人的项目到自己的工程
- fork：github上面，别人的工程目录下点击fork，这时候项目会加入自己的repository中，然后在命令行中把自己repository中的项目clone到本地，如第二步
- 命令行：git clone url<例如 git clone https://github.com/wangyajieI/stock-crawler>
### 1.2 本地修改，开淦
### 1.3 提交修改到远程工程
- git add .
- git commit -m "commit message" <注意这里要用双引号>
- git push origin master <master 可以换成对应的project 别名>
### 1.4 本地修改，提交修改给原作者
- github上面直接pull request
***
## 2、scrapy
## 2.1、建工程
'''
# 创建示例工程
scapy startproject prj_name <scapy startproject my_prj>
#创建spider文件
scapy genspider itcast itcast.com
# 注意，这里创建的spider名称是 itcast，allowed_domains 是itcast.com
# 创建start.py,内容如下
    from scrapy import cmdline

    cmdline.execute("scrapy crawl itcast".split())
'''
