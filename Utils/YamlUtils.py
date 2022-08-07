# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 11:04
# @Author  : hejinhu
import yaml


class YmalUtils:
    """YAML帮助类"""

    @classmethod
    def initUtilYaml(cls, file, key=None):
        """

        :param file:文件地址
        :param key:
        :return:
        """
        try:
            with open(file, encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
            return data
        except Exception as e:
            print(e)


if __name__ == '__main__':
    data = YmalUtils.initUtilYaml('../file.yaml')
    print(data.get('aaa'))
    # print(data['bbb'])
