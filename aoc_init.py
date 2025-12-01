import shutil
import os

for i in range(2, 13):
    src = 'day1'
    dst = f'day{i}'
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)