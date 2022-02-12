import os
import sys
import shutil
import subprocess
import stat

present_dir = r"D:\projects\familyTed\presentation"


# os.system('rmdir /S /Q "{}"'.format(present_dir))q
# subprocess.run(r'manim -qh  main.py', shell=True)
subprocess.run("manim-presentation Main", shell=True)
