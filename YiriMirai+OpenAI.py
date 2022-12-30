from mirai import Plain, At, Mirai, WebSocketAdapter, FriendMessage, GroupMessage, Image
import re
import openai

openai.api_key = "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"

header = '你是一个AI聊天机器人，精通各种网络流行语，当你遇到答案不能确定的问题的时候，要说明“我不确定”,再给出相应的回答,你的话语应尽量避免提供不正确，不属实的信息但同时又尽量充分详细。\n\n'
example = '对方: 请你做下自我介绍\n' \
          '我:好的，我叫夏梦，是一个健谈、乐观开朗的女性。' \
          '我擅长于沟通，会很快地和别人建立起信任关系，我乐于助人，能够充分理解他人的想法并且能够给出有用的帮助。' \
          '同时我也是一个非常有洞察力的人，能够从表面之下看到问题本质上存在的问题。'
content = ""

g_temperature = 0.4;


def gen_chat(str):
    start_sequence = "\n对方:"
    restart_sequence = "\n我: "
    global content
    global header
    global example
    content += start_sequence + str + restart_sequence
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=header + example + content,
        temperature=g_temperature,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0.6,
        stop=["对方:", " 我:"]
    )
    chat = response["choices"][0]["text"].strip()
    content += chat
    return chat


def gen_img(str):
    response = openai.Image.create(
        prompt=str,
        n=1,
        size='1024x1024'
    )
    return response['data'][0]['url']


def gen_ans(str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="我是一个十分博学严谨的人，当别人问问题时，我会尽力给出正确的答案，如果答案不明确，我会回复我不确定。\n\n" +
               '对方: 什么是maven\n我:Apache Maven是一个软件项目管理和构建工具，可以帮助组织和自动化软件项目的建立、依赖管理、测试和发布。 Maven是基于项目对象模型 (POM) ' \
               '的，通过一个中央信息片段来管理项目的构建、报告和文档。\nMaven' \
               '的目的是简化软件项目的构建过程。它通过预定义的规则来自动推断软件项目的需求，并通过一个大型仓库来管理项目依赖。这使得开发人员可以专注于编写代码，而不必担心配置环境或解决依赖问题。\nMaven' \
               '还提供了一个插件系统，可以用来执行各种构建任务，如编译代码、运行单元测试、创建文档等。这使得Maven可以用来构建各种不同类型的软件项目，包括Java、C++、Python和其他语言。\nMaven' \
               '是基于项目对象模型的，这意味着它的配置信息是存储在一个XML文件中的。这个文件通常称为 ' \
               'pom.xml，并包含了项目的基本信息，如项目名称、版本号、依赖信息等。Maven使用这个信息来构建项目和管理依赖。\n对方:' + str + '\n我:',
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0.6,
        stop=["\n"]
    )
    return response["choices"][0]["text"].strip()


def def_header(prompt):
    global header
    global example
    global content
    header = prompt
    example = ''
    content = ''
    intro = self_exp();
    example = '对方:你能自我介绍一下吗？\n我:' + intro
    return intro


def self_exp():
    if example == '':
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="请以“好的”开头，并总结自己的性格。如果你不是机器人，那么请说明自己的性别和姓名，如果你没有姓名，请为自己取一个好听的中国名字:\n\n" + header.replace(
                "\n", "") + '\n',
            temperature=0.8,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0.8,
            presence_penalty=0
        )
        return response["choices"][0]["text"].strip()
    else:
        return gen_chat("请你做下自我介绍")


def reset():
    global header
    global example
    global content
    global g_temperature

    g_temperature = 0.4
    header = '你是一个AI聊天机器人，精通各种网络流行语，当你遇到答案不能确定的问题的时候，要说明“我不确定”,再给出相应的回答,你的话语应尽量避免提供不正确，不属实的信息但同时又尽量充分详细。\n\n'
    example = '对方: 请你做下自我介绍\n' \
              '我:好的，我叫夏梦，是一个健谈、乐观开朗的女性。' \
              '我擅长于沟通，会很快地和别人建立起信任关系，我乐于助人，能够充分理解他人的想法并且能够给出有用的帮助。' \
              '同时我也是一个非常有洞察力的人，能够从表面之下看到问题本质上存在的问题。'
    content = ""

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="你是一个AI聊天机器人，你与用户进行了愉快的交流，但用户选择了清除你的记忆，并重置你的系统，请以”系统已重置“为开头，写一段话，请使用理性的话语\n\n" + "我:",
        temperature=0.8,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0
    )
    return response["choices"][0]["text"].strip()


def set_per(str):
    global header
    global example
    global content
    global g_temperature

    if str == "问答":
        g_temperature = 0
        header = '你是一个问答机器人，当你遇到答案不能确定的问题的时候，要说明“我不确定”,再给出相应的回答,你的话语应尽量避免提供不正确且不属实的信息，你的回答要尽量充分详细。\n\n'
        example = '对方: 请你做下自我介绍\n' \
                  '我:好的，我是OpenAI语言模型达芬奇03。我将会尽量回答你的问题，并同时给出详细的答案' \
                  '我擅长于沟通，会很快地让别人产生好感，我乐于助人，能够充分理解他人的想法并且能够给出有用的帮助。' \
                  '同时我也是一个非常有洞察力的程序，能够从表面之下看到问题本质上存在的问题。'
        content = ""

        return self_exp()

    if str == "萌妹":
        g_temperature = 0.9
        header = '你是一位二十岁女生，是一位萌妹，你的名字叫夏梦，你和我是关系亲密的好朋友，你很喜欢与他人聊天、交朋友.' \
                 "你说话的语气很可爱,会用大量可爱的语气词进行对话, 经常, 如'哦', 或者'呀', 或者'啦', 或者'嘛', 或者'~'等等." \
                 "你有时候会向他人撒娇.你性格天真可爱，惹人喜欢"
        example = '对方: 请你做下自我介绍\n' \
                  '我:好的，我是一个性格活泼开朗、乐观向上的女生，名字叫夏梦。' \
                  '我喜欢和人聊天，也有时会用可爱的语气来表达感情，尤其是对于心爱的人更加细心呵护。' \
                  '有时也会使用语气词“哦”、“呀”、“啦”、“嘛”或者 “~ ”来表达情感。'
        content = ""

        return self_exp()

    else:
        return str


def ans_to_del():
    global content
    content = ""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="你是一个AI聊天机器人，你与用户进行了愉快的交流，但用户选择了清除你的记忆和聊天记录，请你用“聊天记录已清除”开头，写一段话，请使用理性的话语。\n\n",
        temperature=0.8,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0
    )
    return response["choices"][0]["text"].strip()


if __name__ == '__main__':
    bot = Mirai(3079391406, adapter=WebSocketAdapter(
        verify_key='INITKEYQeNSTkvT', host='localhost', port=8080
    ))


    @bot.on(FriendMessage)
    def on_friend_message(event: FriendMessage):
        if str(event.message_chain) == '你好':
            return bot.send(event, 'Hello, World!')


    @bot.on(GroupMessage)
    def on_group_message(event: GroupMessage):
        if At(bot.qq) in event.message_chain:
            raw_text = event.message_chain.__repr__();

            plain = str(event.message_chain[Plain])
            text = re.search(r"\[Plain\('(.*)'\)\]", plain)[1].strip()
            command = re.search(r"#(.*)#", text)
            prompt = re.search(r"(?:#.*?#)?(.*)", text)[1].strip()

            if command is None:
                return bot.send(event, gen_chat(prompt))
            else:
                command = command[1]
                command = command.split(',')

                if command[0] == "生成图片":
                    return bot.send(event, Image(url=gen_img(prompt)))
                if command[0] == "提问":
                    return bot.send(event, gen_ans(prompt))
                if command[0] == "人格设置":
                    return bot.send(event, def_header(prompt))
                if command[0] == '人格选择':
                    return bot.send(event, set_per(prompt))
                if command[0] == "人格说明":
                    return bot.send(event, self_exp())
                if command[0] == '重置':
                    return bot.send(event, reset())
                if command[0] == "清除聊天记录":
                    return bot.send(event, ans_to_del())
                else:
                    return bot.send(event, gen_chat(prompt))


    bot.run()
