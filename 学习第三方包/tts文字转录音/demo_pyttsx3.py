import pyttsx3


def create_voice(text, filename):
    engine = pyttsx3.init(debug=True)  # 初始化语音
    engine.setProperty("rate", 150)  # 设置语速，200正常 100慢
    engine.setProperty("volume", 0.9)  # 设置音量
    # voices = engine.getProperty("voices")  # 获取当前系统所有的发声
    # for i in voices:
    #     engine.setProperty("voice", i.id)
    #     engine.say("我是一个兵，来自老百姓")
    #     print(i)
    #     engine.runAndWait()  # 阻塞把语句说完
    engine.say(text)  # 将结果念出来
    engine.save_to_file(text, filename)  # 保存音频文件
    engine.runAndWait()  # 结束
    engine.stop()  # 结束


if __name__ == "__main__":
    create_voice("hello i an great", "./a.mp4")
