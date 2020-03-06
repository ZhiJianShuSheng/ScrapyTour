## 简介

- python scrapy 分布式爬虫开发模板，方便快速开发。只需写对应的xpath即可完成分布式爬虫
- 内置常见pipline，包括json，excel，mongodb，mysql等数据持久化方案

## 相关技术

- 使用scrapy_redis进行分布式爬虫操作。
- 使用mongodb存储数据
- 开发环境与生产环境的配置分离
- 自动化部署爬虫脚本，爬虫部署采用scrapyd框架
- 支持部署到docker中
- 使用中间件自动处理随机user-agent
- 重写make_request_from_data，实现基于scrapy_redis的Feeding模式，可自定义发送请求

## 笔记


[Scrapy 和 scrapy-redis 的区别](https://github.com/ZhiJianShuSheng/ScrapyTour/blob/master/Note/%20Scrapy%20%E5%92%8C%20scrapy-redis%20%E7%9A%84%E5%8C%BA%E5%88%AB.md)