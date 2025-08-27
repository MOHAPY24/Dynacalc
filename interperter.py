

class Token:
    def __init__(self, value=any, stype=str):
        self.value = value
        self.stype = stype

    def __str__(self):
        return f"[{self.value}:{self.stype}]"
    
    def __repr__(self):
        self.__str__()

class Interperter(object):
    def __init__(self, text):
        self.text = text
        self.ptr = 0
        self.current_token = Token(None, "NONE")
    
    def error(self):
        raise Exception("Error while parsing")

    def get_next_token(self):
        text = self.text

        if self.ptr > len(text) -1:
            return Token(None, "EOF")
        
        current_char = text[self.ptr]

        if current_char.isdigit():
            token = Token(int(current_char), "INT")
            self.ptr += 1
            return token

        elif current_char == "+":
            token = Token("+", "ADD_OPERAND")
            self.ptr += 1
            return token
        
        elif current_char == "-":
            token = Token("-", "MINUS_OPERAND")
            self.ptr += 1
            return token
        
        elif current_char == "*":
            token = Token("*", "MULTIPLY_OPERAND")
            self.ptr += 1
            return token

        elif current_char == "/":
            token = Token("/", "DIVIDE_OPERAND")
            self.ptr += 1
            return token
        
        else:
            self.error()


    def eat(self, token_type):
        if self.current_token.stype == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    
    def expr(self):
        o1 = None
        o2 = None
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat("INT")

        op = self.current_token
        if op.value == "+":
            self.eat("ADD_OPERAND")
            o1 = True
        elif op.value == "-":
            self.eat("MINUS_OPERAND")
            o2 = True
        


        right = self.current_token
        self.eat("INT")

        if o1:
            result = left.value + right.value
        elif o2:
            result = left.value - right.value
        return result

    def term(self):
        o1 = None
        o2 = None
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat("INT")

        op = self.current_token
        if op.value == "*":
            self.eat("MULTIPLY_OPERAND")
            o1 = True
        elif op.value == "/":
            self.eat("DIVIDE_OPERAND")
            o2 = True
        


        right = self.current_token
        self.eat("INT")

        if o1:
            result = left.value * right.value
        elif o2:
            result = left.value / right.value
        return result

    
if __name__ == "__main__":
    while True:
        try:
            code = input("DynaCalc >> ")
        except EOFError:
            break
        if not code:
            continue
        else:
            inte = Interperter(code)
            if "+" in code or "-" in code:
                result = inte.expr()
            elif "*" in code or "/" in code:
                result = inte.term()
            print(result)


