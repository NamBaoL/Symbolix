from math import *
import numpy as np
import random
from termcolor import *

Any = 'SIAN'
Array = 'SAN'
List = 'AN'
Const = 'SI'

lambdas = {
	'+': [
		[[List, Any], "y + [x] if type(x) != list else x"]
	], '-': [
		[[List, Any], "y + [x] if type(x) != list else x"]
	], '*': [
		
  ], '/': [
		
	], '^': [
		
	], '\'': [
		
	], '_': [
		
	], '%': [
		
	], '&': [
		
	], '!': [
		
	], '{': [
		
	], '}': [
		
	], '?': [
		
	], '#': [
		 
	], '@': [
		
	], '$': [
		 
	], '[': [
		[[], "{}"]
  ], ']': [
	  [[], "idx = rindex(stack, {}); del stack[idx]\n[i[1] for i in stack[idx + 1:]]", lambda x: len(x) - rindex(x, ('C', {}))]
  ]
}

def runFunc(token, stack):
	classes = ['SI'[type(i[1]) == int] if i[0] == 'C' else ('AN'[all([type(j) == int for j in i[1]])] if i[0] == 'A' else i[0]) for i in stack]
	types = [type(i[1]) for i in stack]
	values = [i[1] for i in stack]
	#debug(f"{values} {types} {classes}")
	
	# Find function
	functions = lambdas[token]
	for data in functions:
		funcTypes = list(zip(classes[-max([len(classes) - len(data[0]), 0]):], data[0]))
		funcTypes = [(i[0] in i[1]) for i in funcTypes]
		matched = []
		if (not data[0]) or all(funcTypes):
			matched = data; pops = len(data[0]) if len(data) == 2 else data[2](stack); break
		
	# Perform function
	assert matched, colored('Wrong types for function ' + token, 'red', attrs=['bold'])
	args = len(matched[0])
	if args >= 1: x = values[-1]
	if args >= 2: y = values[-2]
	if args >= 3: z = values[-3]
	if args >= 4: t = values[-4]
	idx = 0
	function = matched[1]
	split = function.split('\n')
	try: exec(split[:-2])
	except: pass
	value = eval(split[-1])
	del stack[-pops:]
	stack += [typed(value)]
	debug(stack)
	return stack

def find(array, elem):
	result = []
	lenElem = len(elem) if type(elem) != int else 1
	for i in range(len(array) - lenElem + 1):
		if type(elem) == int: elem = [elem]
		result.append(int(array[i:i + lenElem] == elem))
	result += [0] * (lenElem - 1)
	return result

typed = lambda x: ('CA'[type(x) == list], x)
islist = lambda x: type(x) in [list, str]
where = lambda x: [i for i, j in enumerate(x) if j] if np.ndim(x) == 1 else [encodeRadix(list(np.shape(x)), i) for i, j in enumerate(np.ravel(x)) if j]

def encodeRadix(alpha, omega):
	alpha.reverse()
	result = []
	for a in alpha:
		omega, rem = divmod(omega, a); result += [rem]
	return list(reversed(result))

debug = lambda x: print(colored("Debug: ", 'red') + colored(str(x), 'cyan'))
rindex = lambda a, b: len(a) - a[-1::-1].index(b) - 1