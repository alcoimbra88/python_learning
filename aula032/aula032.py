var = 'valor'

def func():
    print(var)

def func2():
    global var   # aponta para a variavel global , fora da função
    var = 'outro valor'
    print(var)

func()
func2()

# def func():
#     print(var)
#     var =  12345
#     print(var)
#
# func()