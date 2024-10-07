import subprocess

audio1 = './common/abc.mp3'
audio2 = './common/abc2.mp3'


def action_ffmpeg(cmd):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0:
        print(f'success:{res.stdout}')
    else:
        print(f'error:{res.stderr}')


if __name__ == '__main__':
    # 单声道转双声道
    # cmd = 'ffmpeg -i abc.mp3 -ac 2 out2.mp3'
    # 组装录音
    cmd = 'ffmpeg -i out1.mp3 -i out2.mp3 -filter_complex "[0:a][1:a]amerge=inputs=2[aout]" -map "[aout]" output.mp3'
    action_ffmpeg(cmd)
