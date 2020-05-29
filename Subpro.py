import subprocess

p1=subprocess.run('dir', shell=True, capture_output=True, text=True)

print(p1.stdout)
