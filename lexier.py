class Token:
	TYPE = None
	VALUE = None

class Lexier:
	listType = ['+','-','*','/','(',')', '=']
	INT_LIT = 10
	IDENT = 11
	ASSIGN_OP = 20
	ADD_OP = 21
	SUB_OP = 22
	MULT_OP = 23
	DIV_OP = 24
	LEFT_PAREN = 25
	RIGHT_PAREN = 26

	token = Token()
	lexemeList = list()

	#def __init__(self):

	def analyzer(self,inputString):
		def getIdent(self, input, index):
			count = index
			while(count < len(input) and input[count] != ' '):
				if(input[count] in self.listType):
					return input[index:count]
				count+=1
			return input[index:count]

		def switch(x):
			default = lambda x: x
			return {
				'+' : (self.ADD_OP, '+'),
				'-' : (self.SUB_OP, '-'),
				'*' : (self.MULT_OP, '*'),
				'/' : (self.DIV_OP, '/'),
				'(' : (self.LEFT_PAREN, '('),
				')' : (self.RIGHT_PAREN, ')'),
				'=' : (self.ASSIGN_OP,'='),
			}.get(x,-1)

		i = 0

		while(i < len(inputString)):
			newToken = Token()		
			if(switch(inputString[i]) == -1):
				ident = getIdent(self,inputString, i)				
				if(self.isNum(ident)):
					newToken.TYPE = self.INT_LIT
					newToken.VALUE = ident
					self.lexemeList.append(newToken)
					i += (len(ident)-1)
				else:
					if(ident and ident.strip()):					
						newToken.TYPE = self.IDENT
						newToken.VALUE = ident
						self.lexemeList.append(newToken)
						i += (len(ident))		
			else:
				newToken.TYPE = switch(inputString[i])[0]
				newToken.VALUE = switch(inputString[i])[1]
				self.lexemeList.append(newToken)
			i+=1


	#the simple function to check if string is number
	def isNum(self,n):
		try:
			int(n)
			return True
		except ValueError:
			return False

	#the super simple function to get the next el in list
	def getNext(self):
		if(len(self.lexemeList) > 0):
			output = self.lexemeList.pop(0)
			print("Next token is: %s Next lexeme is %s" % (output.TYPE,output.VALUE))
			return output
		else:
			tmpToken = Token()
			tmpToken.TYPE = -100
			tmpToken.VALUE = "Fail"
			return tmpToken





