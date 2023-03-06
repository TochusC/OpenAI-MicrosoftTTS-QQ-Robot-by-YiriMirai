import re

import openai
from mirai import Plain, At, Mirai, WebSocketAdapter, FriendMessage, GroupMessage, Image
from mirai.models import NewFriendRequestEvent

import AIEngine
import VoiceEngine

qq_number = 205329624  # 请在这里输入您的机器人QQ号
g_port = 8080  # 默认端口号是8080，如果您进行了修改，请输入相应的端口。
verifyKEY = "INITKEYF7MdE0SC"  # 请在这里输入miraiHTTPS中的verifyKEY

openai_api_key = "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"  # 请在这里输入你的OpenAI API KEY

# 可选
# 如果不启动语音功能,就不需要输入
speech_key = "32530f5917e7417fbd891d61f6d1af37"  # 请在这里输入微软文字转语音服务的API KEY
service_region = "eastus"  # 在这里输入服务所在的区域

def initialize():
    global openai_api_key
    global speech_key
    global service_region

    AIEngine.openai_api_key = openai_api_key

    VoiceEngine.speech_key = speech_key
    VoiceEngine.service_region = service_region


if __name__ == '__main__':
    bot = Mirai(qq_number, adapter=WebSocketAdapter(
        verify_key=verifyKEY, host='localhost', port=g_port
    ))

    initialize()

    @bot.on(NewFriendRequestEvent)  # 自动接受好友申请
    async def allow_request(event: NewFriendRequestEvent):
        await bot.allow(event)


    @bot.on(FriendMessage)
    def on_friend_message(event: FriendMessage):
        raw_text = event.message_chain.__repr__();

        plain = str(event.message_chain[Plain])
        text = re.search(r"\[Plain\('(.*)'\)\]", plain)[1].strip()
        command = re.search(r"#(.*)#", text)
        prompt = re.search(r"(?:#.*?#)?(.*)", text)[1].strip()

        if command is None:
            return bot.send(event, AIEngine.gen_chat(prompt))
        else:
            command = command[1]
            command = command.split(',')

            if command[0] == "生成图片":
                return bot.send(event, Image(url=AIEngine.gen_img(prompt)))
            if command[0] == "系统设置":
                return bot.send(event, AIEngine.def_settings(prompt))
            if command[0] == '人格选择':
                return bot.send(event, AIEngine.set_per(prompt))
            if command[0] == "启动语音聊天":
                return bot.send(event, AIEngine.start_voi())
            if command[0] == "关闭语音聊天":
                return bot.send(event, AIEngine.end_voi())
            if command[0] == "启动聊天记录":
                return bot.send(event, AIEngine.start_mem())
            if command[0] == "关闭聊天记录":
                return bot.send(event, AIEngine.end_mem())
            if command[0] == "帮助":
                return bot.send(event, AIEngine.help())
            if command[0] == "设置情绪":
                return bot.send(event)
            if command[0] == "清除聊天记录":
                return bot.send(event, AIEngine.del_history())
            else:
                return bot.send(event, AIEngine.gen_chat(prompt))


    @bot.on(GroupMessage)
    def on_group_message(event: GroupMessage):
        if At(bot.qq) in event.message_chain:
            raw_text = event.message_chain.__repr__();

            plain = str(event.message_chain[Plain])
            text = re.search(r"\[Plain\('(.*)'\)\]", plain)[1].strip()
            command = re.search(r"#(.*)#", text)
            prompt = re.search(r"(?:#.*?#)?(.*)", text)[1].strip()

            if command is None:
                return bot.send(event, AIEngine.gen_chat(prompt))
            else:
                command = command[1]
                command = command.split(',')

                if command[0] == "生成图片":
                    return bot.send(event, Image(url=AIEngine.gen_img(prompt)))
                if command[0] == "系统设置":
                    return bot.send(event, AIEngine.def_settings(prompt))
                if command[0] == '人格选择':
                    return bot.send(event, AIEngine.set_per(prompt))
                if command[0] == "启动语音聊天":
                    return bot.send(event, AIEngine.start_voi())
                if command[0] == "关闭语音聊天":
                    return bot.send(event, AIEngine.end_voi())
                if command[0] == "启动聊天记录":
                    return bot.send(event, AIEngine.start_mem())
                if command[0] == "关闭聊天记录":
                    return bot.send(event, AIEngine.end_mem())
                if command[0] == "帮助":
                    return bot.send(event, AIEngine.help())
                if command[0] == "设置情绪":
                    return bot.send(event, AIEngine.change_emo(prompt))
                if command[0] == "清除聊天记录":
                    return bot.send(event, AIEngine.ans_to_del())
                else:
                    return bot.send(event, AIEngine.gen_chat(prompt))


    bot.run()