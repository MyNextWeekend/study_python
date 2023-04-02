import configparser
import yaml

from utils.path_utils import get_path


def get_by_yaml(file_path: str):
    with open(file_path, encoding='utf-8') as fin:
        data = yaml.load(fin, Loader=yaml.FullLoader)
    return data


def get_by_ini(file_path: str):
    cfg = configparser.RawConfigParser()
    cfg.read(file_path, encoding='utf-8')
    return cfg


if __name__ == '__main__':
    # file = get_path("/config/mysql.ini")
    # print(file)
    # obj = get_by_ini(file)
    # print(obj.get("mysql", "host"))
    # print(obj.getint("mysql", "port"))

    file = get_path("/config/mysql.yaml")
    obj = get_by_yaml(file)
    print(obj.get("mysql"))


