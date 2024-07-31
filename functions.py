from math import *
import numpy as np
import random
from termcolor import *

Any = 'SIAN'
Array = 'SAN'
List = 'AN'
Const = 'SI'
Brack = ('O', {})

lambdas = {
	'+': [
		[['I', 'I'], 'y + x'],
		[['S', Const], 'y + str(x)'],
		[[Const, 'S'], 'str(y) + x'],
		[[List, Any], 'y + [x] if type(x) != list else x'],
		[[Any, List], '([y] if type(y) != list else y) + x']
	], '-': [
		[['I', 'I'], 'y - x']
	], '*': [
		[['I', 'I'], 'y * x'],
		[[List, List], '[y] + [x]']
  ], '/': [
		[['I', 'I'], 'y / x'],
		[['S', 'S'], 'y.split(x)']
	], '^': [
		[['I', 'I'], 'y ** x'],
		[[Array], '[j for i, j in enumerate(x) if j not in x[:i]]']
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
		[[], '{}']
  ], ']': [
	  [[], ['id = rindex(stack, Brack)', 'del stack[id]', 'arr = [i[1] for i in stack[id:]]', 'del stack[id:]', 'arr']]
  ]
}

def runFunc(token, stack):
	classes = ['SI'[type(i[1]) == int] if i[0] == 'C' else ('AN'[all([type(j) == int for j in i[1]])] if i[0] == 'A' else i[0]) for i in stack]
	types = [type(i[1]) for i in stack]
	values = [i[1] for i in stack]
	
	# Find function
	functions = lambdas[token]
	for data in functions:
		funcTypes = list(zip(classes[-max([len(classes) - len(data[0]), 0]):], data[0]))
		funcTypes = [(i[0] in i[1]) for i in funcTypes]
		matched = []
		if (not data[0]) or all(funcTypes):
			matched = data; pops = len(data[0]); break
		
	# Perform function
	assert matched, colored('Wrong types for function ' + token, 'red', attrs=['bold'])
	args = len(matched[0])
	if args >= 1: x = values[-1]
	if args >= 2: y = values[-2]
	if args >= 3: z = values[-3]
	if args >= 4: t = values[-4]
	idx = 0
	function = matched[1]
	if type(function) == str: function = [function]
	try: exec('\n'.join(function[:-1]))
	except: pass
	value = eval(function[-1])
	if pops: del stack[-pops:]
	stack += [typed(value)]
	debug(stack, 'StackDebug', 'cyan', 'green')
	return stack

def find(array, elem):
	result = []
	lenElem = len(elem) if type(elem) != int else 1
	for i in range(len(array) - lenElem + 1):
		if type(elem) == int: elem = [elem]
		result.append(int(array[i:i + lenElem] == elem))
	result += [0] * (lenElem - 1)
	return result

typed = lambda x: ('O' if x == {} else 'AN'[all([type(i) == int for i in x])] if type(x) == list else 'SI'[type(x) == int], x)
islist = lambda x: type(x) in [list, str]
where = lambda x: [i for i, j in enumerate(x) if j] if np.ndim(x) == 1 else [encodeRadix(list(np.shape(x)), i) for i, j in enumerate(np.ravel(x)) if j]

def encodeRadix(alpha, omega):
	alpha.reverse()
	result = []
	for a in alpha:
		omega, rem = divmod(omega, a); result += [rem]
	return list(reversed(result))

debug = lambda text, title = 'Debug', colortext = 'cyan', colortitle = 'red': print(colored(title + ': ', colortitle) + colored(str(text), colortext))
rindex = lambda a, b: len(a) - a[::-1].index(b) - 1