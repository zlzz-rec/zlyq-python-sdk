### 中量引擎服务端SDK (Python)

##### 安装方法

```
pip install zlyq-python-sdk
```

##### 中量引擎官网

``` https://www.zplatform.cn/
https://www.zplatform.cn/
```

##### 中量引擎官方文档

```https://wiki.zplatform.cn/
https://wiki.zplatform.cn/
```

##### SDK说明

对于以下接入方式:"中量引擎Saas服务接入"或"私有化部署方式接入", 本SDK提供了两个不同的SyncClient来解决数据同步的问题, 其中:

* 私有化部署方式提供了向私有化部署服务上报埋点的方法及设置用户画像方法; SyncClient初始化参数需要从私有化服务后台获取

* Saas服务方式提供了向中量引擎服务同步用户数据、媒资数据及埋点数据(用户历史交互数据)的方法; SyncClient初始化参数需要从中量引擎后台获取

##### 调用方式

调用方式请参考`zlyqtest`目录下的`XXXtest.py`文件
注意:
1.以下是面向私有化方式的test文件:

* tracktest.py    埋点上报到私有化服务
* profiletest.py    设置用户画像到私有化服务

2.以下是面向Saas方式的test文件:

* saastracktest.py    埋点及历史交互行为同步
* usertest.py    同步用户信息到中量服务
* mediatest.py    同步媒资相关交互行为信息到中量服务
* videotest.py    同步视频到中量服务
* articletest.py    同步图文到中量服务
* imagetest.py    上传图片到中量服务

3.请在工程根目录上一级以模块方式运行test文件, 示例
```
python3 -m zlyq-python-sdk.zlyqtest.tracktest
```
