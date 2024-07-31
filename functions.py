from math import *
import numpy as np
import random
from termcolor import *

All = 'SIANF'
Any = 'SIAN'
Array = 'SAN'
List = 'AN'
Const = 'SI'
Brack = ('O', {1})
Parenthesis = ('O', {2})
FuncMark = ''
Functions = '[]+-*/^\'_{}|%`!?@#$~&\\=<>,:;() '

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
		[['I'], 'ceil(x)'],
		[[Array], 'x[-1]'],
	], '_': [
		[['I'], 'floor(x)'],
		[[Array], 'x[0]'],
	], '%': [
		[[Array, 'I'], 'y[x:] + y[:x]']
	], '\\': [
		[['I', 'I'], 'y or x']
	], '&': [
		[['I', 'I'], 'y and x'],
		[[Array, Array], '[i for i in y if i in x]']
	], '!': [
		[['I', 'not x']]
	], '`': [
		[['I'], '-x'],
		[[Array], 'x[::-1]']
	], '{': [
		[['I', 'I'], 'min([y, x])'],
		[[Array], 'gradeup(x)']
	], '}': [
		[['I', 'I'], 'max([y, x])'],
		[[Array], 'gradedown(x)']
	], '?': [
		[[Array], 'where(x)']
	], '#': [
		[['I'], 'list(range(1, x + 1))'],
		[[Array], 'len(x)']
	], '@': [
		[[Array, 'I'], 'y[x]']
	], '$': [
		[['I'], 'str(x)'],
		[['S'], 'int(x)'],
		[[List], 'list(np.shape(x))']
	], '[': [
		[[], '{1}']
	], ']': [
		[[], ['idx, arr = 0, 0; idx = rindex(stack, Brack); arr = [i[1] for i in stack[idx + 1:]]; del stack[idx:]', 'arr']]
	], '~': [

	], ':': [
		[[All, All], ['del stack[-2:]; stack += [typed(i) for i in [x, y]] + [None, None]', 'None']]
	], 
}

def runFunc(token, stack):
	classes = [i[0] for i in stack]
	# debug(classes)
	values = [i[1] for i in stack]
	
	# Find function
	functions = lambdas[token]
	for data in functions:
		funcTypes = list(zip(classes[max([len(classes) - len(data[0]), 0]):], data[0]))
		funcTypes = [(i[0] in i[1]) for i in funcTypes]
		matched = []
		if (not data[0]) or all(funcTypes):
			matched = data; pops = len(data[0]); break
		
	# Perform function
	assert matched, colored(f'Wrong types for function {token}, stack = [...{str(classes[max([len(classes) - 4, 0]):])[1:-1]}]', 'red', attrs=['bold'])
	if pops >= 1: x = values[-1]
	if pops >= 2: y = values[-2]
	if pops >= 3: z = values[-3]
	if pops >= 4: t = values[-4]
	function = matched[1]
	if type(function) == str: function = [function]
	try: exec('\n'.join(function[:-1]))
	except: pass
	value = eval(function[-1])
	print(value)
	if pops: del stack[-pops:]
	if value: stack += [typed(value)]
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

def typed(x):
	if type(x) == set: return ('O', x) 
	elif type(x) == list: return ('AN'[all([type(i) == int for i in x])], x)
	elif type(x) == tuple: return ('B', list(x))
	else: return ('SI'[type(x) == int], x)
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
isfunc = lambda x: type(x) == tuple and x[0] == 'F'

gradeup = lambda x: [x.index(i) for i in sorted(x)]
gradedown = lambda x: [x.index(i) for i in sorted(x, reverse = True)]

def parseBlock(block):
	pass

def runCode(code):
	stack = []
	for token in code:
		tokenType = token[0]
		token = token[1]
		if tokenType in 'CAB':
			stack += [typed(tuple(token) if tokenType == 'B' else token)]
			try: runFunc(token, stack)
			except: pass
			debug(stack, 'StackDebug#2', 'white', 'grey')
		else: stack = runFunc(token, stack) if Parenthesis not in stack or token == ')' else stack + [('F', token)]
	return stack
