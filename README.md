# What is this?
A simple Lexical Analyzer &amp; Syntax Analyzer written in Python.

# Hmm, but why?
One time, when I still in my university, my professor ask me if I can write for him a simple Lexical analyzer & a Parser (I was in Programming Language class).
So I start research what is it & how to build one. And here we are, just a very simple Lexier & Parser for my study. But who know you'll need it sometime?

# Okay, but How it works?
Put it all in the same folder and run file parser.py in your python console, you can open and edit the input.
<br>
Input (just a simple code) :
````
(sum + 47) / total
````

<br>
Output :
````
Next token is: 25 Next lexeme is (
Enter <expr>
Enter <term>
Enter <factor>
Next token is: 11 Next lexeme is sum
Enter <expr>
Enter <term>
Enter <factor>
Next token is: 21 Next lexeme is +
Exit <factor>
Exit <term>
Next token is: 10 Next lexeme is 47
Enter <term>
Enter <factor>
Next token is: 26 Next lexeme is )
Exit <factor>
Exit <term>
Exit <expr>
Next token is: 24 Next lexeme is /
Exit <factor>
Next token is: 11 Next lexeme is total
Enter <factor>
Exit <factor>
Exit <term>
Exit <expr>
````
