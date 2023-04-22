class Lexer:
    
        

    def Lex(self):
        usr = input("Enter the something to analyze it: ")
        self.type_of_Token(usr)
        
        
    def showingsymboltable(self):
        file = open("str.txt", "r")
        data = file.read().split()
        for i in data:
            self.type_of_Token(i)

        file.close()    
   
    
    
    index = 3

    identifiers = []

    def type_of_Token(self, userinput):
        reserved_words = ["for","while" , "if", "else"]
       
        
       
        if userinput in reserved_words:
            print(f'<token={userinput.upper()}>')
        
        
        elif userinput.isnumeric():
            print(f'<token=INTEGER, integer_value={userinput}>')
            
        
        elif "-" in userinput and "." in userinput:
            print(f'<token=FLOAT, float_value={userinput}>')
               
        elif '.' in userinput:
            print(f'<token=FLOAT, float_value={userinput}>')
            
            
        elif "-" in userinput:
            print(f'<token=INTEGER, integer_value={userinput}>')
        
            
        elif "&&" == userinput:
            print("f'<token=LOGICAL_AND>'")
            

        elif "&" == userinput:
            print("f'<token=BITWISE_AND>'")
        
  
        elif "||" == userinput:
            print("f'<token=LOGICAL_OR>'")
            
   
        elif "|" == userinput:
            print("f'<token=BITWISE_OR>'")
            
  
        elif userinput[0].isdigit():
            print(f'<token=ERROR, unrecognized_string="{userinput}">')
        
        else:
            
            if userinput in self.identifiers:
                    print(f'<token=ID, index={self.identifiers.index(userinput) + 4}>')
                
                
              
            else:
               
            
                self.identifiers.append(userinput)
                self.index += 1
              
                print(f'<token=ID, index={self.index}>')
                