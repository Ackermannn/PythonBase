print("您好,我是智能聊天机器人\n输入文字后再按下回车我就可以看到你的消息了。 " )
while True:
    words = input("您:")
    print("AI:" + words[:-1])
