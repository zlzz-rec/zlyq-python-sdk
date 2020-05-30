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

##### 集成中量分析服务(私有化)
集成中量分析服务的用户, 请使用private_client下的SyncClient, 初始化参数需要从私有化服务后台获取。 

SyncClient提供了上报埋点的方法及设置用户画像方法。

调用方式请参考`zlyqtest`目录下的`XXXtest.py`文件

* private_tracktest.py    
    + presetEvent         上报预置事件埋点
    + customEvent         上报自定义事件埋点
* private_profiletest.py  设置用户画像

##### 集成中量引擎推荐服务(Saas)
集成中量引擎推荐服务的用户, 请使用client下的SyncClient, SyncClient初始化参数需要从中量引擎后台获取。

Saas服务方式提供了向中量引擎服务同步用户数据、媒资数据及埋点数据(以及用户历史交互数据)的方法。 

注意:`同步`是指将用户或物品的基本信息同步到中量引擎服务, 因为业务方只需要推荐结果然后自行组装数据所以不需要将源文件上传到中量服务。

调用方式请参考`zlyqtest`目录下的`XXXtest.py`文件

* tracktest.py          埋点数据同步
* usertest.py           用户数据同步
* videotest.py          
    + syncVideo         视频数据同步         
* articletest.py        
    + syncArticle       图文数据同步               

##### 集成中量引擎推荐服务(私有化)
中量引擎私有化服务可以针对任何形式的物品进行推荐分发, 例如:音乐、游戏、商品等等。如果您有这类的推荐分发需求请在中量引擎官网联系客服。

##### 集成中量引擎推荐服务及客户端信息流SDK(Sass)
集成中量引擎推荐服务的用户, 请使用client下的SyncClient, SyncClient初始化参数需要从中量引擎后台获取。

Saas服务方式提供了向中量引擎服务同步用户数据、媒资数据及埋点数据(以及用户历史交互数据)的方法。 

注意:`上传`是指将源文件上传到中量引擎进而获取主键id的过程; `同步`是指将信息(包括上传得到的id)同步到中量引擎服务。因为业务方需要使用推荐结果加上配到的客户端信息流SDK, 所以需要上传源文件到中量服务。

调用方式请参考`zlyqtest`目录下的`XXXtest.py`文件

* tracktest.py          埋点数据同步
* usertest.py           用户数据同步
* videotest.py          
    + uploadVideo       上传视频及封图源文件并同步  
* articletest.py        
    + uploadArticle     上传图片源文件并同步(图片源文件可能多个, 需要先通过`imagetest`上传图片获取主键id再调用此方法)
* imagetest.py          上传图片, 获取图片主键

3.项目使用相对路径, 请在工程根目录上一级以模块方式运行test文件, 示例
```
python3 -m zlyq-python-sdk.zlyqtest.tracktest
```
