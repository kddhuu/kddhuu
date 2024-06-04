import os, random

def main():
# generate random string of characters
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # type: ignore
char_string = ''.join(random.choices(char_list))

# create a file with the virus code in it
filename = random.choice(char_string) + '.exe'
file_path = os.path.abspath('./') + '/' + filename

# if the file already exists, overwrite it
if os.path.isfile(file_path):
os.remove(file_path) # type: ignore
else # type: ignore

# copy the virus code to the newly created file
open(file_path, 'w').write(''.join([random.choice(char_list) for _ in range(random.randint(100, 150))]))
os.chmod(file_path, 0777)

# create a new process to run the virus file
command = 'python -m SimpleHTTPServer ' + random.choice(char_string) + '.exe'
os.system(command)

main()
