import subprocess

#下面三个等价
subprocess.run(["ls", "-l"])
subprocess.run("ls -l ", shell = True)
subprocess.call(["ls", "-l"])

#
a = subprocess.run("ls -l ", shell = True, stdout = subprocess.PIPE)
print(a)
b = subprocess.call("ls -l ", shell = True, stdout = subprocess.PIPE)
print(b)
c = subprocess.Popen("ls -l ", shell = True, stdout = subprocess.PIPE)
print(c)


