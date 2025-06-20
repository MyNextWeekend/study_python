from passlib.context import CryptContext

# 创建一个 CryptContext 对象
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
    哈希密码
    :param password: 密码
    :return:
    """
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    """
    验证密码
    :param password: 密码
    :param hashed_password: hash密码
    :return:
    """
    return pwd_context.verify(password, hashed_password)


if __name__ == "__main__":
    input_password = "my_secret_password"
    hash_pwd = get_password_hash(input_password)
    print(f"获取hash之后的密码是：{hash_pwd}")
    print(f"校验之后的bool值是：{verify_password(input_password, hash_pwd)}")
