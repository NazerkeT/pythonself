import subprocess
res=subprocess.check_output(["gnome-screensaver-command", "-l"])
res=subprocess.check_output(["sleep","5"])
res=subprocess.check_output(["gnome-screensaver-command", "-dp"])


