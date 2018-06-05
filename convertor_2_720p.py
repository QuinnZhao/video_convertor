from os import system

command = 'c:/develop_program/ffmpeg-20180521/bin/ffmpeg.exe -i {} -c copy -c:v libx264 -vf scale=-2:720 {}'

for i in range(1,13):
    src = f'./mp4/{i:02d}.mp4'
    dst = f'./mp4/_{i:02d}.mp4'
    # print(src, dst)
    print('{} is converting......'.format(src))
    system(command.format(src, dst))
print('Done!')