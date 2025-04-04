# @Time    : 2023/4/30 15:36
# @Author  : MyNextWeekend
import argparse


def run(a, b):
    pass


if __name__ == "__main__":
    # run('robot', 1)
    parser = argparse.ArgumentParser(description="线程监控脚本参数说明：")
    parser.add_argument(
        "-path", dest="path", help="监控服务路径", type=str, required=True
    )
    parser.add_argument(
        "-time", dest="time", help="脚本执行时间，单位分钟", type=int, default=5
    )
    args = parser.parse_args()

    run(args.path, args.time)
