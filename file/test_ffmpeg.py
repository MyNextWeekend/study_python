import subprocess

audio1 = './file/abc.mp3'
audio2 = './file/abc2.mp3'


def action_ffmpeg(args: list):
    list_args = ['ffmpeg'] + args
    res = subprocess.run(list_args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0:
        print(f'success:{res.stdout}')
    else:
        print(f'error:{res.stderr}')


if __name__ == '__main__':
    l = []
    # 单声道转双声道
    # l.append('-i')
    # l.append('abc.mp3')
    # l.append('-ac')
    # l.append('1')
    # l.append('out2.mp3')
    # 组装录音
    # l.append('-i')
    # l.append('out2.mp3')
    # l.append('-i')
    # l.append('out1.mp3')
    # l.append('-filter_complex')
    # l.append('[0:a][1:a]amerge=inputs=2[aout]')
    # l.append('-map')
    # l.append('[aout]')
    # l.append('output.mp3')
    action_ffmpeg(l)
# ffmpeg -i left.aac -i right.aac -filter_complex "[0:a][1:a]amerge=inputs=2[aout]" -map "[aout]" output.mka
# mka为acc编码格式
