import datetime
import re


def increment_numbers_by_four(input_string):
    def increment(match):
        number_str = match.group()

        # 改进日期处理的灵活性
        date_formats = ['%Y%m%d']  # 添加更多可能的日期格式

        for fmt in date_formats:
            try:
                a = datetime.datetime.strptime(number_str, fmt)
                a += datetime.timedelta(days=1)
                return a.strftime(fmt)
            except ValueError:  # 仅捕获值错误，提高异常处理
                pass

        # 对于非日期数字的处理
        try:
            # 尝试将字符串转换为整数加1，解决性能问题
            return str(int(number_str) + 1)
        except ValueError:
            # 如果无法转换为整数，返回原字符串
            return number_str

    # 改进正则表达式，这里保留原表达式以满足不改变函数输出的要求
    pattern = r'\d+'
    return re.sub(pattern, increment, input_string)


# 示例输入字符串
input_string = "The price is 123.45 and the year is 20221231."

# 使用函数处理字符串
output_string = increment_numbers_by_four(input_string)

print(output_string)
