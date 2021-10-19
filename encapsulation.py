class Hello:
    def __init__(self):
        self.a = ''
        self._b = ''
        self.__c = ''



if __name__ == "__main__":
    hi = Hello()

    hi.a = 'This is info'
    hi._b = 'This is protected info'
    hi.__c = 'This is private info'

    
    print(hi.a)
    print(hi._b)
    print(hi.__c)
