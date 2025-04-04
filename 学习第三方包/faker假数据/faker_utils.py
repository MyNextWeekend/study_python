from faker import Faker

f = Faker(locale="zh-CN")
print(f.name())
print(f.ssn())
print(f.phone_number())
print(f.address())
print(f.company())
print(f.email())
print(f.job())
print(f.city())
print(f.credit_card_number())
print(f.text())
