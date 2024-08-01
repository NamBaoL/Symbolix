def getTypes(lines):
	global predef

	# Tokenize
	for line in lines:
		for char in line:
			if char in (predef['symbols'] + predef['functions']): # Check if symbol
				if predef['token']: predef['tokens'] += [('CONST', predef['token'])]
				predef['tokens'] += [('SMB' if char in predef['symbols'] else 'FUNC', char)]
				predef['token'] = ''
			else:
				predef['token'] += char
		if predef['token']: predef['tokens'] += [('CONST', predef['token'])]
		predef['token'] = ''

	# Group
	groups = group(predef['tokens'])
	parser = parse(groups)
	# print(parser)

	# Typed parsed tokens
	return parsedToTypes(parser)

def parsedToTypes(parser):
	types = typeCode(parser)
	types = [deepBool(i) for i in types]
	types = ['CFAB'[2*(type(i) == list) + (not i if type(i) != list else not i[0])] for i in types]
	types = list(zip(types, parser))
	types = [(i[0], trueType(i[1])) if i[0] in 'CA' else i for i in types]
	return types

def trueType(array):
	if type(array) == str:
		return array[1:-1] if array[0] == '"' else array
	elif type(array) not in [str, list]:
		return array
	return [trueType(i) for i in array]

def typeCode(parsedCode):
	global predef
	if type(parsedCode) == tuple: return False
	elif type(parsedCode) in [float, int]: return True
	elif type(parsedCode) == str: return parsedCode not in predef['functions']
	elif type(parsedCode) == tuple: return [False]
	else: return [typeCode(token) for token in parsedCode]

deepBool = lambda x: [False not in x] if type(x) == list else x

def group(tokens):
	opened = ''
	resGroup = []
	if len(tokens) < 1 or not max([i[0] == 'SMB' for i in tokens]) or tokens[0] == '$STR':
		return tokens
	for token in tokens:
		tokenType = token[0]
		tokenChar = token[1]
		if tokenType == 'SMB': # Check for open-close symbols
			if len(opened) == 0: resGroup += [[]]
			if tokenChar == ')': 
				opened = opened[:-1]
				if len(opened) >= 1: resGroup[-1] += [token]
			elif tokenChar == '(': 
				if len(opened) >= 1: resGroup[-1] += [token]
				else: resGroup[-1] += ['$PRN']
				opened += tokenChar
			elif tokenChar == '"':
				if opened and opened[-1] == '"': 
					opened = opened[:-1]
					if len(opened) >= 1: resGroup[-1] += [token]
				else: 
					if len(opened) >= 1: resGroup[-1] += [token]
					else: resGroup[-1] += ['$STR']
					opened += tokenChar
		elif tokenType in ['CONST', 'FUNC', '$']: # Keep lists, constants, and functions
			if not opened: resGroup += [token]
			else: resGroup[-1] += [token]
	resGroup = [group(i) for i in resGroup]
	return resGroup

def parse(groups):
	resGroup = []
	for idx, group in enumerate(groups):
		if group[0] == 'CONST' or (group[0] == 'FUNC' and group[1] != ' '):
			try: resGroup += [eval(group[1])]
			except: resGroup += [group[1]]
		elif group[0] in ['$LIST', '$PRN']:
			if group[0] == '$PRN': resGroup += [(parse(groups[idx][1:]))]
			else: resGroup += [parse(groups[idx][1:])]
		elif group[0] == '$STR':
			resGroup += [f"\"{''.join([i[1] for i in groups[idx][1:]])}\""]
	return resGroup

Functions = '[]+-*/^\'_{}|%`!?@#$~&\\=<>,:;() '
predef = {
	'symbols': '"()',
	'functions': Functions,
	'parsed': '',
	'array': [],
	'tokens': [],
	'token': ''
}