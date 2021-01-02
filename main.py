import re
import os
from  time import sleep

def add_shebang(file_reader, filename):
	shebang = '#!/usr/bin/python3' 
	if not re.search(r'#!/usr/bin/python3',file_reader.split('\n')[0]):
		file_reader = shebang + '\n' + file_reader
	return file_reader

def modify_file(path, filename):
	if path != os.path.abspath(__file__):
		if re.match(r'.+\.pyw?$', filename):
			try:
				with open(path, 'r+') as f:
					file_reader = f.read()
					new_text = add_shebang(file_reader, path)
					f.seek(0)
					f.write(new_text)
					print(f'Shebang line added to {filename}')
			except Exception as e:
				print(f'Program file with this path: {path}. Exception: {e}')

def main(input_path):
	print(f'Working on: {input_path}\n')
	if os.path.isdir(input_path):
		for root, dirs, files in os.walk(input_path):
			for filename in files:
				path = os.path.join(root, filename)	
				modify_file(path, filename)			
	elif os.path.isfile(input_path):
		modify_file(input_path, input_path)
	else:
		return

if __name__ == '__main__':
	print ('This script will add a shebang line to all the python files existing in this directory and all subdirectories. ')
	run = input('Type the path of the file or directory that you want to modify or type \"RUN\" and hit the return key to run the script in the current directory: ')
	if run.upper().strip() == 'RUN':
		main(os.getcwd())
		print('Succes!\nClosing script...')
	elif os.path.exists(run):
		main(run)
		print('Succes!\nClosing script...')
	else:
		print('Path not found!')
		print ('Aborting...')
	sleep(3)