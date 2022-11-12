# -*- coding: utf-8 -*-
import execjs

# js_text = """
# function add(x, y) {
#    return x + y;
# }
# """

with open('./test.js', 'r') as fin:
    js_text = fin.read()

ctx = execjs.compile(js_text)
res = ctx.call('add', 1, 2)
print(res)


