import lexicalanalyzer 


while(True):
    print("----------------------")
    print("Menu for Lexical Analyzer")
    print("1- Press 1 to Call Lex()")
    print("2- Press 2 to Show Symbol Table")
    print("3- Press 3 to Exit")
    print("----------------------")
    userinput = int(input("Please choose a number from 1 to 3: "))

    if userinput == 1:
        
        lexical = lexicalanalyzer.Lexer()
        lexical.Lex()

      
        continue
    elif userinput == 2:
        lexical = lexicalanalyzer.Lexer()
        lexical.showingsymboltable()
        
        continue
    elif userinput == 3:
        break
    else:
        print("----------------------")
        print("This is not a valid number. Please select from 1 to 3!")
        print("----------------------")
        