import pyttsx3

text = """
张孝祥·《浣溪沙》
行尽潇湘到洞庭，
楚天阔处数峰青，
旗梢不动晚波平。
红蓼一湾纹缬乱，
白鱼双尾玉刀明，
夜凉船影浸疏星。
空灵澄澈，直可入梦。
"""
text2 = """
哈哈哈哈哈
哈哈哈哈哈
哈哈哈哈哈
哈哈哈哈哈
哈哈哈哈哈
哈哈哈哈哈
"""

engine = pyttsx3.init(debug=True)
# engine.say(text)
engine.save_to_file(text2, './file/abc2.mp3')
engine.runAndWait()
