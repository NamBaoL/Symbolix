from functions import *
from parse import *

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
  main()