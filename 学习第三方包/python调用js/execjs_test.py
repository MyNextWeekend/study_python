import execjs

with open("密码加密.js", "r", encoding="utf-8") as f:
    js_content = f.read()

context = execjs.compile(js_content)

result = context.call("Encrypt", "1q2w3e4r@")
print(result)
