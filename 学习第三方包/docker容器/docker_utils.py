import os
from uuid import uuid4
import docker
from docker.errors import ContainerError

# 初始化 Docker 客户端
docker_client = docker.from_env()


def run_repo_in_docker(repo_dir, entry_file):
    """
    使用用户提供的 Dockerfile 来构建 Docker 镜像并运行指定入口文件
    """
    container_name = f"container_{uuid4()}"
    image_name = "jfxs/rye"

    try:
        # 准备运行命令，执行用户指定的入口文件
        command = f"python /repo/{entry_file}"

        # 创建并启动容器，将整个仓库挂载到容器中
        container = docker_client.containers.create(
            image=image_name,  # 使用官方 Python 3.10 Docker 镜像
            command=command,  # 执行安装依赖并运行入口文件
            name=container_name,
            volumes={
                os.path.abspath(repo_dir): {
                    'bind': '/repo',  # 将整个仓库挂载到容器的 /repo 目录
                    'mode': 'ro'  # 只读模式
                }
            },
            detach=True  # 后台运行容器
        )

        # 启动容器
        container.start()

        # 等待容器执行完成
        container.wait()

        # 获取容器的日志
        logs = container.logs(stdout=True, stderr=True).decode('utf-8')

        # 获取容器的退出代码
        exit_code = container.attrs['State']['ExitCode']
        print(f"{container.attrs}")
        # 根据退出码生成返回结果
        if exit_code == 0:
            result = f"Script executed successfully. Exit code: {exit_code}"
        else:
            result = f"Script failed with exit code: {exit_code}"

        # 返回日志和执行结果
        return result, logs
    except ContainerError as e:
        return f"Error running script: {e}", ""
    finally:
        pass
        # 清理容器和镜像
        container.remove(force=True)
        # docker_client.images.remove(image=image_name, force=True)


if __name__ == '__main__':
    root_path = "/Users/weekend/workSpaces/pycharmProjects/study_python/学习第三方包/docker容器"
    result, logs = run_repo_in_docker(root_path, "hello.py")
    print(f"{result:} {logs:}")
