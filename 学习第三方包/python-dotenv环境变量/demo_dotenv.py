import os

from dotenv import load_dotenv

from utils.path_utils import BASE_PATH


def load_env_variables():
    """
    根据变量加载不同的环境变量
    :return:
    """
    # 获取当前环境，默认为开发环境
    environment = os.getenv("ENVIRONMENT", "dev")
    # 加载对应环境的 .env 文件
    env_file = os.path.join(BASE_PATH, f".env.{environment}")
    print(f"正在加载环境变量:{env_file}")
    load_dotenv(env_file)  # 如果不传入参数，默认找根目录下.env文件


load_env_variables()

if __name__ == "__main__":
    print(os.getenv("MY_USERNAME"))
    print(os.getenv("MY_PASSWORD"))
