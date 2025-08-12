# **Desenvolvimento de Sistemas 2** 

## **Professor Roberto Itai**

## Aula 001 - 05/08/2025

Introdução a Python com alguns testes de *print* e *type*

*print* imprime alguma mensagem na tela

    print('Hello World')

*type* verifica o tipo de dado da variável

    x = 3
    print(type(x))
Vai imprimir o tipo de dado da variável *x*, neste caso, um *int* (número inteiro)

## Aula 002 - 12/08/2025

Testes com input e operações

O comando *input* abre uma caixa de resposta para o usuário inserir uma informação

 - O tipo de dado do resultado SEMPRE será uma string
 - O comando pode ser inserido dentro de uma variável e "puxada" por ela depois
 
    print(input('Digite seu nome: '))

O *print* adicionado antes serve pra exibir a informação respondida pelo usuário
Pode-se transformar o tipo de dado da resposta do usuário com:

    idade = int(input('Digite a sua idade'))
    print(idade)

Aqui a operação de input foi colocada dentro da variável "idade", transformada em *int* e em seguida *printada* na tela

Operações seguem o padrão de outras linguagens, veja o exemplo:

    a = 12
    b = 20
    soma = a + b
    print(soma)

No exemplo foram atribuídos valores *int* nas variáveis *a* e *b* e em seguida **somados** com o uso do símbolo de '+'

Se o tipo de dado de *a* e *b* forem alteradas, como por exemplo:

    a = "12"
    b = "24"

O + passa a servir como uma **concatenação**, assim como a vírgula
		 *Concatenação = Intervalo entre variáveis, separa as duas e te permite imprimir mais de uma com o *print*, exemplo:
		 

    nome = igor
    sobreonome = gianeri
    print(nome + gianeri)
    print(nome, gianeri)

Ordem de prioridade das operações ( 0 > 1 >  2 > 3)
( ) = 0
^ = 1 
'*' / \ % = 2
"+" "-" = 3
