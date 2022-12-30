# YiriMirai-OpenAI

通过YiriMirai调用[OpenAI](https://openai.com/)提供的API，而实现的QQ AI机器人。

使用到[YiriMirai](https://github.com/YiriMiraiProject/YiriMirai)，[Mirai](https://github.com/mamoe/mirai)两个GitHub项目，感谢它们的开源分享！


## 快速开始

在使用前，请确保您安装了Python，并在目录下通过pip install -r requirements.txt安装所需要的库。

然后，您需要改动YiriMrai+OpenAI.py文件中的第6-9行几项参数，分别输入您的OpenAI API KEY, miraiHTTP中的verifyKEY，机器人QQ号， 端口号。

一切准备完毕！

在运行YiriMirai+OpenAI.py前，请先运行装有mirai-api-http插件的MiraiConsole并在里面登录对应的机器人账号。

现在，运行YiriMirai+OpenAI.py，通过私聊或在群里at机器人账号，就可以体验到OpenAI语言模型的强大啦。


## 进一步说明

如果您的如何获取OpenAI API KEY有疑问：

  首先您需要注册一个OpenAI账号，您可以参考以下两个网站：
  
  https://juejin.cn/post/7173447848292253704
  
 
  https://mirror.xyz/boxchen.eth/9O9CSqyKDj4BKUIil7NC1Sa1LJM-3hsPqaeW_QjfFBc
  
如果您对MiraiConsole的安装，verifyKEY的获取有疑问，请移步：

  https://github.com/mamoe/mirai/blob/dev/docs/ConsoleTerminal.md
 

## 使用方法

您在私聊中直接向机器人发送语句即可得到回复，而在群聊中则需要先@机器人，才可得到相应回复。

语句前可以加#指令#，来更改机器人的设置

目前的指令有：
  #生成图片# 在此输入图片描述
      机器人将会发送生成的图片
      
  #提问# 在此输入问题
      机器人将会尽力回复准确的信息
   
  #人格设置# 在此输入人格描述，例如：“你是一位阳光快乐的十八岁少女，喜欢与他人交流。“
      在接下来的对话中，机器人将会以描述的人格来进行回复，人格描述越详细越好。
    
  #人格选择# 在此输入人格名称，目前仅有两个人格可供选择”问答“和”萌妹“。
      在接下来的对话中，机器人将会以选择的人格来进行回复。
      
  #人格说明#
      机器人将会重述一遍自己现在的人格特点。
      
  #重置#
      将机器人重置回默认人格。
      
  #清除聊天记录#
      清除机器人记录的聊天记录，如果机器人不再响应您的问题，应是聊天记录超出了OpenAI的限制，此指令可进行修复，使机器人正常工作。
      

## 其他

如果遇到其他问题或错误，欢迎您向我询问！

这是我第一次在GitHub上发布比较用心的开源项目，如果我做的有什么地方不对，请告诉我，我会对您非常感激的！
