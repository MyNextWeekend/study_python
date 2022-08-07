import yaml
import os


class ElementdataYamlUtils():

    def __init__(self, yaml_path):
        """初始化"""
        try:
            with open(yaml_path, encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
            return data
        except Exception as e:
            print(f'打开{yaml_path}文件异常===>{e}')

    def get_yaml_element_info(self, yaml_path):
        """获取yaml信息"""
        with open(yaml_path, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

yaml = ElementdataYamlUtils()

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    yaml_path = os.path.join(current_path, '../file.yaml')
    elements = ElementdataYamlUtils().get_yaml_element_info(yaml_path)

    print('单独取某一个变量：' + str(elements['aaa']))

    for key, val in elements['aaa'].items():
        print('*' * 5 + '循环取' + '*' * 5)
        print(f'key的值是：{key}')
        print(f'val的值是：{val}')
