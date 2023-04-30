class Color(str):
    
    def __new__(self, color):
        self.color = color
        return  str.__new__(Color, color)
    

if __name__ == "__main__":
    print(Color("WHITE"))