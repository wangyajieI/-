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
```
# 创建示例工程
scapy startproject prj_name <scapy startproject my_prj>
#创建spider文件
scapy genspider itcast itcast.com
# 注意，这里创建的spider名称是 itcast，allowed_domains 是itcast.com
# 创建start.py,内容如下
    from scrapy import cmdline

    cmdline.execute("scrapy crawl itcast".split())
```
- 建成的目录结构如下
```
    F:\xxx\xxx\scrapyTest\my_prj>tree /F
    卷 娱乐 的文件夹 PATH 列表
    卷序列号为 0006-E187
    F:.
    │  scrapy.cfg

    │
    └─my_prj
        │  items.py   # 爬取数据后需要的数据Fields
        │  middlewares.py  # 中间层，可以定义agent代理等
        │  pipelines.py    # spider爬取后会返回items.py中定义的数据类型，pipeline.py中需要定义如何处理这些数据，比如保存到数据库等
        │  settings.py     # settings.py中定义配置类，比如robots协议，ITEM_PIPELINES，数据库HOST PORT，DB_name，user_agent等等
        |  start.py        # 启动脚本，执行此脚本可直接启动scrapy爬虫
        │  __init__.py
        │
        ├─spiders
        │  │  itcast.py    # spider脚本
        │  │  __init__.py
        │  │
        │  └─__pycache__
        │          __init__.cpython-37.pyc
        │
        └─__pycache__
                settings.cpython-37.pyc
                __init__.cpython-37.pyc
```
## 2.2 scrapy集成mongodb
- mongodb只是数据保存的方式，因此，集成mongodb只需要改动两个地方即可
-- 2.2.1 settings中增加mongodb定义，比如MONGODB_HOST, MONGODB_PORT, MONGODB_NAME, MONGODB_DOCNAME
-- 2.2.2 pipeline.py中增加mongodb保存数据的代码，注意，需要在process_item中将item的内容按照items.py中定义的结构保存到collections中<col.insert_one()>
## 2.3 scrapy集成redis
- redis是一个典型的缓存式数据库，scrapy中经常用来作为spider爬取之后的缓存队列使用
-- 2.3.1 spider中，spider class需要继承scrapy_redis.spiders.RedisSpider类，这样，数据就直接先保存在了spider中
-- 2.3.2 spider中，去掉start_urls，而将原有的start_urls保存在redis中。
-- 2.3.3 settings中，需要定义redis相关的配置项，比如REDIS_HOST, REDIS_PORT, SCHEDULER， DUPEFILTER_CLASS， SCHEDULER_PERSIST， ITEM_PIPELINES
--- 2.3.3.1 REDIS_START_URLS_AS_SET 这个字段设置为True，那么2.3.2章节中保存reids时，应该用sadd，否则用lpush
--- 2.3.3.2 ITEM_PIPELINES中设置my_prj.pipelines.my_prjPipeline的值，一定不能是None，否则无法保存到数据库
## 2.4 scrapy添加extension层
- redis key用完之后，scrapy并不会停下来，这时候可以添加extension层，解决redis key为空后的空跑问题
