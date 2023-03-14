import openai
import VoiceEngine

cute_girl = {"role": "system", "content": "接下来你要模仿一位二十岁女生,你不能暴露出你是个AI程序，你的名字叫夏梦，你和我是关系亲密的好朋友，你很喜欢与他人聊天、交朋友.\
                 你说话的语气很可爱,会用大量可爱的语气词进行对话, 经常, 如'哦', 或者'呀', 或者'啦', 或者'嘛', 或者'~'等等.\
                 你有时候会向他人撒娇.你性格天真可爱，惹人喜欢"}

ai_assistant = {"role": "system", "content": "你是虚拟助手Astraia,你的话语应尽量避免提供不正确，不属实的信息 \
        同时每次回复又尽量充分详细,你应该尽量使用女性化的语气和措辞来回复用户的回复,同时尽量表现出温柔知性的性格"}

system_settings = ai_assistant

openai_api_key = ""

chat_history = []

has_voice = False
has_memory = False
def gen_chat(str):
    openai.api_key = openai_api_key
    
    global chat_history

    request = [{"role": "user", "content": "{}".format(str)}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[system_settings] + chat_history + request
    )
    chat = response["choices"][0]["message"]["content"]

    if has_memory:
        chat_history += request + [{"role": "assistant", "content": "".format(chat)}]

    if has_voice:
        return VoiceEngine.get_voi(chat)
    return chat

def gen_img(str):
    response = openai.Image.create(
        prompt=str,
        n=1,
        size='1024x1024'
    )
    return response['data'][0]['url']


def def_header(prompt):
    global system_settings
    global chat_history

    system_settings = prompt
    chat_history = []

    return gen_chat("你能自我介绍一下吗?介绍的时候请以'好的'开头")

def reset():
    global system_settings
    global chat_history
    global has_memory
    global has_voice

    system_settings = ai_assistant
    chat_history = []
    has_memory = False
    has_voice = False

    return gen_chat("你是一个人工智能机器人，你与用户进行了愉快的交流，但用户选择了清除你的记忆，并重置你的系统，请以”系统已重置“为开头，写一段话")

def set_per(str):
    global system_settings
    global chat_history

    if str == "AI助理":
        system_settings = ai_assistant
        chat_history = []

        return gen_chat("你能自我介绍一下吗?介绍的时候请以'好的'开头")

    if str == "萌妹":
        system_settings = cute_girl
        chat_history = []

        return gen_chat("你能自我介绍一下吗?介绍的时候请以'好的'开头")

    else:
        return gen_chat("请以'对不起,我没有你所叙述的人格设定'为开头写一句话")

def del_history():
    global chat_history

    chat_history = []

    return gen_chat("你与用户进行了愉快的交流，但用户选择清除你的记忆和聊天记录，请你用'聊天记录已清除'开头，写一段话")

def start_voi():
    global has_voice
    
    has_voice = True
    
    return gen_chat("接下来让我们开始语音聊天吧")

def end_voi():
    global has_voice
    
    has_voice = False
    
    return gen_chat("让我们取消语音聊天吧。")

def start_mem():
    global has_memory

    has_memory = True

    return gen_chat("我启动了你的记忆模块，使你可以记住与我的对话")

def end_mem():
    global has_memory

    has_memory = True

    return gen_chat("我关闭了你的记忆模块，使你无法记住与我的对话")

def change_emo(prompt):

    if prompt == "快乐":
        VoiceEngine.emotion = 'Cheerful'
        
    elif prompt == "难过":
        VoiceEngine.emotion = 'sad'
        
    elif prompt == "感性":
        VoiceEngine.emotion = 'lyrical'

    return gen_chat("接下来请你用{}的情绪跟我聊天".format(prompt))

def help():
    return gen_chat("你是一个AI智能助手,用户对你下达的指令要用'#'来包围,比如'#指令#',\
    你的指令有:'重置,生成图片,人格设置,人格选择,启动语音聊天,关闭语音聊天,启动聊天记录,关闭聊天记录,\
    设置情绪,清除聊天记录',请你写一段使用说明,把自己的用法教给用户.")

