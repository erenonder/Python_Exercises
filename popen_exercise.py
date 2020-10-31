import os

output_python_version = os.popen('python --version', "r")

python_version = output_python_version.readline()
print(python_version, end='')
