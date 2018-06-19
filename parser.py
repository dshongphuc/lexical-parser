from lexier import Lexier
from lexier import Token
class Parser:
	lexier = Lexier()
	token = Token()
	nextToken = None

	#def __init__(self, lexemeList):

	#Compile function
	def compile(self, inputString):	
		self.lexier.analyzer(inputString)
		self.getNextToken()
		self.expr()
		# for i in range(0,len(self.lexier.lexemeList)):
		# 	self.getNextToken()
		 	#token = self.lexier.getNext()
		 	#print("Next token is %s Next lexeme is %s" % (token.TYPE, token.VALUE))


	# Expr function
	def expr(self):
		print("Enter <expr>")
		self.term()
		while(self.nextToken.TYPE == self.lexier.ADD_OP or self.nextToken.TYPE == self.lexier.SUB_OP):
			self.getNextToken()
			self.term()
		print("Exit <expr>")


	# Term function
	def term(self):
		print("Enter <term>")
		self.factor()
		while(self.nextToken.TYPE == self.lexier.MULT_OP or self.nextToken.TYPE == self.lexier.DIV_OP):
			self.getNextToken()
			self.factor()
		print("Exit <term>")


	# Factor function
	def factor(self):
		print("Enter <factor>")
		if(self.nextToken.TYPE == self.lexier.IDENT or self.nextToken.TYPE == self.lexier.INT_LIT):
			self.getNextToken()
		else:
			if(self.nextToken.TYPE == self.lexier.LEFT_PAREN):
				self.getNextToken()
				self.expr()
				if(self.nextToken.TYPE == self.lexier.RIGHT_PAREN):
					self.getNextToken()
				else:
					self.error()
		print("Exit <factor>")


	# Get next token
	def getNextToken(self):
		self.nextToken = self.lexier.getNext()


	# Function to print error
	def error(self):
		print("Syntax error")



# We can test here :
parser = Parser()
parser.compile("(sum + 47) / total")