def metodo_bissecao(a,b,erro,funcao,max_iteracoes=1000):
    #VERIFICAÇÃO SE OS ARGUMENTOS SÃO NÚMEROS
    for argumento in [a, b, erro, max_iteracoes]:
        if not eh_numero(argumento):      
            raise TypeError(f'O valor de {argumento} nao e um numero!') 

    #VERIFICAR SE B E MAIOR DO QUE A
    if a > b:
        aux = b
        b = a
        a = aux
    elif a==b:
        pass #adicionar excessão

    #VERFICAR SE DO ERRO E MAIOR DO ZERO
    if erro < 0:
        erro = (-1)*erro
    elif erro == 0:
        pass #adicionar excessão

    #VERIFICAR SE É UMA FUNÇÃO    
    if type(funcao) is not function:
        pass #adicionar excessão

    #VERIFICAR SE O MAX_ITERAÇÕES É POSITIVO
    if max_iteracoes < 0:
        max_iteracoes = (-1)*max_iteracoes
    elif max_iteracoes == 0:
        pass #adicionar excessão

    #IMPLEMENTAÇÃO DO MÉTODO
    #verificação do teorema de Bolzano
    if funcao(a)*funcao(b) > 0:
        pass #adicionar excessão

    x_medio = (a+b)/2.00

    iteracao = 0 
    while (iteracao < max_iteracoes) and (abs(funcao(x_medio)) < erro):
        print(f'iteração = {iteracao}, a = {a} , b = {b} , x = {x_medio} , f(a) = {funcao(a)}, f(b) = {funcao(b)} , f(x) = {funcao(x_medio)}, erro atual = {abs(funcao(x_medio))},erro = {erro}')

        if funcao(a)*funcao(x_medio) < 0:
            b = x_medio
        else:
            a = x_medio

        x_medio = (a+b)/2.00
    
        iteracao += 1  

    return  x_medio        
        


# ======= FUNCOES AUXILIARES ========
#
def eh_numero(valor):
    return (type(valor) is int or type(valor) is float)


