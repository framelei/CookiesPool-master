# CookiesPool

可扩展的Cookies池，目前对接了新浪微博，[m.weibo.cn](https://m.weibo.cn)，可自行扩展其他站点


## 安装

```
pip3 install -r requirements.txt
```

## 基础配置 

### 接口基本配置

```# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填Non
# REDIS_PASSWORD = 'foobared'
REDIS_PASSWORD = None

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
# Key  为Redis数据库的表名
# Value为生成cookies的类名。用于调度器动态实例化对象
GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
# Key  为Redis数据库的表名
# Value为验证cookies的类名。用于调度器动态实例化对象
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 检测器检测接口
# test_url = TEST_URL_MAP[self.website]
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
# 分布式爬虫时使用可公网访问的服务器ip
# API_HOST = '192.168.43.68'
API_HOST = '127.0.0.1'
API_PORT = 5000

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = False
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
```

### 进程开关

在config.py修改

```python
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = True
# API接口服务
API_PROCESS = True
```


## 导入账号

```
python3 importer.py
```

```
新建account_pwd.txt文件
按照如下格式写入

18459748505----astvar3647
14760253606----gmidy8470
14760253607----uoyuic8427
18459749258----rktfye8937

```


## 运行

请先导入一部分账号之后再运行，运行命令：

```
python3 run.py
```

## 运行效果

三个进程全部开启：


```
API接口开始运行
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
Cookies生成进程开始运行
Cookies检测进程开始运行
正在生成Cookies 账号 14747223314 密码 asdf1129
正在测试Cookies 用户名 14747219309
Cookies有效 14747219309
正在测试Cookies 用户名 14740626332
Cookies有效 14740626332
正在测试Cookies 用户名 14740691419
Cookies有效 14740691419
正在测试Cookies 用户名 14740618009
Cookies有效 14740618009
正在测试Cookies 用户名 14747222472
Cookies有效 14747222472
Cookies检测完成
验证码位置 420 580 384 544
成功匹配
拖动顺序 [1, 4, 2, 3]
成功获取到Cookies {'SUHB': '08J77UIj4w5n_T', 'SCF': 'AimcUCUVvHjswSBmTswKh0g4kNj4K7_U9k57YzxbqFt4SFBhXq3Lx4YSNO9VuBV841BMHFIaH4ipnfqZnK7W6Qs.', 'SSOLoginState': '1501439488', '_T_WM': '99b7d656220aeb9207b5db97743adc02', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 'SUB': '_2A250elZQDeRhGeBM6VAR8ifEzTuIHXVXhXoYrDV6PUJbkdBeLXTxkW17ZoYhhJ92N_RGCjmHpfv9TB8OJQ..'}
成功保存Cookies
```
