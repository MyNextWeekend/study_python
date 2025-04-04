from DrissionPage import ChromiumPage

# 创建对象
page = ChromiumPage()
# 访问网页
page.get("https://www.bilibili.com/")

page.ele(
    'xpath://div/span[normalize-space(.) and normalize-space(text()) = "登录"]'
).click()
page.ele("@placeholder=请输入账号").input("123")
page.ele("@placeholder=请输入密码").input("456")
page.ele(
    'xpath://div/div[normalize-space(.) and normalize-space(text()) = "登录"]'
).click()
