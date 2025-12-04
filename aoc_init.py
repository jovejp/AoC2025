import shutil
import os

for i in range(6, 13):
    src = 'day5'
    dst = f'day{i}'
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)