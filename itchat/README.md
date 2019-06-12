# itchat简单介绍
----
## 1. what is itchat?
首先给出[itchat项目主页](https://itchat.readthedocs.io/zh/latest/)和[github地址](https://github.com/littlecodersh/ItChat)。  
 简单地说，itchat就是使用python对网页版的身微信进行了封装，它提供常用的api,直接在python中调用来完成你想要的功能。  

## 2. itchat的安装方法：
`` pip install itchat ``

## 3. 常使用的api(更多api见[此处](https://itchat.readthedocs.io/zh/latest/api/)）

```
# 导入itchat  
import itchat  

# 登录itchat,提供了两个api
login(self, enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None)

auto_login(self, hotReload=False, statusStorageDir='itchat.pkl',
        enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None):

# 查看登录状态
itchat.check_login(self, uuid=None)

# 给某个人发送信息
itchat.send_msg(self, msg='Test Message', toUsername=None)

# 给自己发送信息, 即接收者为filehelper
itchat.send_msg(msg='我自己',toUsername='filehelper')

# 注销itchat
itchat.logout()
```

## 4.补充说明
用到了什么就写什么，用不到就不写!
