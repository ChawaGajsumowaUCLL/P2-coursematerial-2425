def repeat(function, n):
    i= 0
    while i < n:
        function()
        i += 1
    
def say_hello():
    print("hello!")

repeat(say_hello, 5)