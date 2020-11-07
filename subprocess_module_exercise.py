
import subprocess


# subprocess.run('pwd')

# subprocess.run('ls -alrt', shell=True)

process = subprocess.run(['ls', '-al'], capture_output=True, text=True)


# print(f'arguments: {process.args} return: {process.returncode}')
# print(f'output: {process.stdout}')

if process.returncode == 0:
    # print(f'output: {process.stdout}')
    pass
else:
    print(f'Error occured in your command\n {process.stderr}')


first_process = subprocess.run(
    ['cat', 'onder.txt'], capture_output=True, text=True)

print(f'output: {first_process.stdout}')

second_process = subprocess.run(
    ['grep', '-n', 'writing'], input=first_process.stdout, capture_output=True, text=True)

print(f'found at {second_process.stdout}')

# We could do the above code in one line as follows:
# shell is used when you enter the whole command without
# providing as list elements.

process = subprocess.run("cat onder.txt | grep -n writing",
                         capture_output=True, text=True, shell=True)

print(f'second option: {process.stdout}')
