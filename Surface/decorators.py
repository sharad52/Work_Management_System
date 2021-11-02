def Wrapper(func):
    def inner1(*args,**kwargs):
        # code here
        #more code here 
        # print something
        # print("hello ")
        return "inner"
    return inner1