# OpenAI+MicrosoftTTS QQ Robot by YiriMirai

### 支持语音聊天的ChatGPT QQ机器人

通过YiriMirai调用[OpenAI](https://openai.com/)和[Microsoft TTS服务](https://azure.microsoft.com/products/cognitive-services/text-to-speech/#overview)提供的API，而实现的QQ AI机器人。

使用到[YiriMirai](https://github.com/YiriMiraiProject/YiriMirai)，[Mirai](https://github.com/mamoe/mirai)两个GitHub项目，感谢它们的开源分享！

程序中的代码非常简单，您应该可以非常轻松地读懂它们，并做出修改。

## 快速开始

在使用前，请确保您安装了Python，并在目录下通过`pip install -r requirements.txt`安装所需要的库。

然后，您需要改动Start.py文件中的第10-19行的几项参数，

分别输入您miraiHTTP中的verifyKEY，机器人QQ号， 端口号，以及OpenAI的API KEY和微软TTS服务的API KEY及服务区域。

如果您不需要语言聊天功能的话，可以省略掉微软TTS服务的API KEY。


接下来,请您先修改MiraiConsole中的http通讯设置文件中的内容，文件位置为config\net.mamoe.mirai-api-http\settings.yml。

1. 在adapters一项中，加入

   ` -ws`

2. 在adapterSettings一项中，加入
```
    ws:
    host: localhost #这里填写mirai运行主机的ip地址，默认为localhost，即本机地址。
    port: 8080      #这里填写http通讯所用的端口号，默认为8080.
    reservedSyncId: -1
```

一切准备就绪！

现在，运行Start.py，通过私聊或在群里at机器人账号，就可以体验到OpenAI语言模型的强大啦。


## 进一步说明

- 如果您的如何获取OpenAI API KEY有疑问：

  首先您需要注册一个OpenAI账号，您可以参考以下两个网站：

  https://juejin.cn/post/7173447848292253704

  https://mirror.xyz/boxchen.eth/9O9CSqyKDj4BKUIil7NC1Sa1LJM-3hsPqaeW_QjfFBc
  

- 如果您对MiraiConsole的安装，verifyKEY的获取有疑问，请移步：

  https://github.com/mamoe/mirai/blob/dev/docs/ConsoleTerminal.md
 

## 使用方法

您在私聊中直接向机器人发送语句即可得到回复，而在群聊中则需要先@机器人，才可得到相应回复。

语句前可以加#指令#，来更改机器人的设置

目前的支持指令有：


  - `#帮助#`
     机器人将会叙述一遍自己的使用说明，介绍目前支持的指令。


  - `#生成图片# 在此输入图片描述`
      机器人将会发送生成的图片
      
   
  - `#人格设置# 在此输入人格描述` 例如：“你是一位阳光快乐的十八岁少女，喜欢与他人交流。“

      在接下来的对话中，机器人将会以描述的人格来进行回复，人格描述越详细越好。

    
  - `#人格选择# 在此输入人格名称` 目前仅有两个人格可供选择”AI助理“和”萌妹“。
      在接下来的对话中，机器人将会以选择的人格来进行回复。
      

  - `#启动语音聊天#`
      机器人接下来将会发送语音进行回复。


  - `#关闭语音聊天#`
      机器人接下来将会以文本的方式进行回复


  - `#启动消息记录#`
      机器人接下来将会记住用户的消息，并根据消息记录生成回答。


  - `#关闭消息记录#`
      机器人接下来将不会记住用户的消息。


  - `#设置情绪#`
      设置机器人发送语音时候的语气情绪，目前支持的有”快乐，难过，感性“。


  - `#清除聊天记录#`
      清除机器人的聊天记录，如果机器人不再响应您的问题，应是聊天记录超出了OpenAI的限制，此指令可进行修复，使机器人正常工作。

      
  - `#重置#`
      将机器人重置回默认人格。
      

## 其他

如果遇到其他问题或错误，欢迎您向我询问！

这是我第一次在GitHub上发布比较用心的开源项目，

如果我有什么地方做得不对，或代码有写得不好的部分，请告诉我，我会对您非常感激的！

