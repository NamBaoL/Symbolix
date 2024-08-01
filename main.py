from functions import *
from parse import *
import os

def run(lines):
	global stack
	stack = runCode(getTypes(lines))
	print()
	# print(stack)
	debug(f'{'\n{\n' + ''.join(['  ' + valFormat(i[1]) +',\n' for i in stack]) + '}\n'}', 'Stack', 'white', 'yellow')

def main():
	global stack, file
	stack = []
	file = open("run.sbx")
	run(file.read().split("\n"))

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	main()