class mathops:

    def add(a,b):
        return a + b
    
    def sub(a,b):
        return a - b
    
    def mult(a,b):
        return a * b
    
    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b 
        else:
            return "Error: Division by zero"
