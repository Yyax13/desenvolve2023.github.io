## @uthor André Luiz Barbosa | Andrehlb

Development in the Data Science codes.

ícone Python Collections parte 1: listas e tuplas Python Collections parte 1: listas e tuplas

Sumário

AULA
01

 Listas e operações

1. Listas e operações

Atividades

## 01. Introdução | 02min

## 02. Introdução as coleções e lista | 11min

## 03. Mais operações em listas e list comprehension | 13min

## 04. Problemas da mutabilidade da lista | 08min

PRÓXIMA ATIVIDADE

[00:00] Por fim, eu queria mostrar duas consequências importantes da mutabilidade da lista. Imagine que alguém define uma função que se chama def faz_processamento_de_visualizacao() e recebe uma lista. E então, vai fazer um print(len(lista)) ("print" e tamanho da lista), só isso, super simples o código.

[00:30] No caso das nossas idades, por exemplo, que são [16, 21, 29, 56, 43],chamamos a função faz_processamento_de_visualizacao(idades)] para imprimir o tamanho da lista, que, neste caso, é 5. Para conferir, imprimimos a lista de novo, idades, então, vai imprimir 5, que é o tamanho da lista e a lista de novo para conferirmos, [16, 21, 29, 56, 43].

[00:58] Só que alguém, no futuro, como esses dois trechos de código estão em pontos distintos, vem e fala lista.append(13).

def faz_processamento_de_visualizacao(lista):
  print(len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)

Ao rodar o código, ele continua imprimindo o "5", porque chamamos o faz_processamento, que recebeu uma lista com cinco elementos.

```
5
[16, 21, 29, 56, 43, 13]
```

[01:32] A lista é uma referência para um único objeto na memória, esse objeto na memória tem cinco posições (16, 21, 29, 56 e 43), então o que está acontecendo na memória é o que foi criado na linha 1 idades = [16, 21, 29, 56, 43. Portanto, foi criado um espaço na memória com esses valores. Ainda na linha 1, o que fizemos foi criar uma variável chamada idades que aponta para esses valores na memória.

./Python

```
idades =====v
     [16, 21, 29, 56, 43]
```

[02:10] Agora chamamos o faz_processamento, que passa uma referência para esse valor [16, 21, 29, 56, 43], e para essa função faz_processamento_de_visualizacao(). Dentro dela teremos uma nova variável chamada lista, que referencia o objeto de cima, então os dois estão referenciando o mesmo objeto na memória.

./Python

```Python
idades =====v

     [16, 21, 29, 56, 43]

lista==========T
```

[02:50] E o que acontece é que quando chamamos o lista.append? Estamos appendando aqui o valor 13, [16, 21, 29, 56, 43]. Então estamos mudando o valor da lista, que era mutável. Mas na hora que saímos dessa função,q variável idades continua apontando para aquele objeto que agora possui um valor a mais.

[03:17] Então, é super delicado quando trabalhamos com objetos mutáveis sejam eles quais forem. Algumas pessoas no mercado defendem usar objetos imutáveis a maior parte do tempo, sempre que possível. Objetos, referências, seja lá o que for, alguns defendem' a imutabilidade, quanto mais melhor, porque se evita esse tipo de situação inesperada, por exemplo, eu não estava esperando que o faz_processamento fosse alterar a minha lista.

[03:47] Mas no momento em que eu passei a lista como parâmetro, você perdeu o controle dessa lista, ela pode voltar vazia, ou completamente diferente. Sempre que você passa um objeto mutável como parâmetro para alguém, você não sabe o que vai sobrar desse objeto depois, porque ele é mutável, pode ter alterado os valores durante essa chamada.

[04:10] Então isso é algo para sempre nos atentarmos. Uma consequência disso que todo mundo passa na vida do Python é: imagine que você tem essa função faz_processamento_de_visualizacao, só que você quer deixar um valor padrão para ela. O meu valor padrão vai ser uma lista vazia.

./Python

```Python
def faz_processamento_de_visualizacao(lista = []):  
    print(len(lista))  
    lista.append(13)  
    faz_processamento_de_visualizacao()  
```

[04:30] Vou chamar faz_processamento_de_visualizacao, e não vou passar nada como parâmetro. Uma lista vazia será criada, vai imprimir "0", e adicionar 13. Em outras palavras, vai adicionar um elemento, mas imprimir 0, vamos ver?

./Python

```
def faz_processamento_de_visualizacao(lista = []):
print(len(lista)
lista.append(13)

faz_processamento_de_visualizacao()
```

```
0
```

Imprimiu "0".
Ao chamar de novo, perceberemos que a lista está aumentando de tamanho. Repare que quando você coloca um valor padrão para um parâmetro de uma função no Python, esse padrão vai ser armazenado em algum lugar.

[05:20] Então esse objeto, que é uma lista vazia, está armazenado na memória. Nós imprimimos o 0, e, nesse objeto, adicionamos o valor 13. Quando chamamos de novo o método sem parâmetro, a variável, por padrão, referencia o objeto que continua existindo. Então, o objeto padrão continuou existindo e sendo referenciado como objeto padrão - o valor a ser referenciado por padrão - por esse parâmetro.

./Python

```
faz_processamento_de_visualizacao()

0

faz_processamento_de_visualizacao()

1

faz_processamento_de_visualizacao()

2

faz_processamento_de_visualizacao()

3
```

[05:57] Então começamos a adicionar cada vez mais, a lista fica cada vez maior. Se imprimirmos a lista em si, vamos ver que na primeira vez ela realmente está vazia, [], na segunda, ela tem o valor [13], depois o valor [13, 13], e depois [13, 13, 13]. Então, o valor está sendo alterado. Se quisermos colocar um valor padrão para um parâmetro que é mutável, por exemplo, sem manter o estado - que é o que estamos fazendo no caso de uma lista - o que precisamos fazer?.

[06:27] Então, eu queria que toda vez tivéssemos uma lista nova, só o colchete não está criando, toda vez, uma lista nova, porque ele executa o código uma única vez, cacheia e referencia todas as vezes. Se eu colocar o tipo list() e referenciar o construtor dele, toda vez el vai executar esse código? Não, porque esse código é executado uma única vez, só é aplicado esse valor uma vez, então, se eu rodar duas vezes, vai continuar imprimindo 0 e 1, vazio e 13.

./Python

```Python
def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
    print(lista)
    lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
```

```
0
[]
1
[13]
```

[07:00] Então, a boa prática nessa situação é não colocarmos valor nenhum. Se quero deixar o lista = list() como opcional, então farei isso o deixando como nada, lista = None Se a lista for nada, if lista == None:, então a lista é uma nova lista, e será executada uma única vez, mas é o None que é nada, não tem problema.

./Python

```
lista = [16, 21, 29, 56, 43]
def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
     lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)
```

```
6
[16, 21, 29, 56, 43, 13]
```

[07:27] E toda vez que chamamos essa nossa função vamos verificar, se é o valor padrão que é o None - se é nada - uma nova lista é criada. O código é executado todas as vezes, claro, mas só é analisado e executado uma única vez, mas não tem mais problema, porque se for None, vai criar uma lista nova, se for None de novo, vai criar uma lista nova de novo, e corrigimos o nosso erro.

[07:58] É muito comum isso acontecer com listas. Então, não é recomendável colocar uma lista como parâmetro default, e, sim,None e verificar se é None, mas isso também se estende para outros objetos que você pode usar como parâmetro de valor opcional, que é mutável. Portanto, é sempre bom ter esse cuidado, listas e objetos que são mutáveis.

## 05. Removendo dados duplicados

Gabriel é programador e trabalha em uma escola dando aula de matemática. No fim do semestre, Gabriel passa as notas dos alunos para uma lista feita em Python que o ajuda no controle das notas. Um dia, acidentalmente, Gabriel duplicou as notas e precisava remover as duplicadas.

```
notas = [2, 2, 3, 5]
```

Como essa duplicidade pode ser removida?

Selecione uma alternativa

A)

 Utilizando a função append para remover as notas duplicadas, o Python remove os elementos que estão por último no lista.

```
O append() adiciona um elemento ao final da lista, não remove.
```

<p> B) </p> Utilizando a função`remove()´ e passando como parâmetro a nota duplicada para ser excluída. Essa função vai retirar a primeira aparição da nota, resolvendo a duplicidade.

```
Quando usamos a função `remove()´ ela vai percorrer nosso array e remover a primeira aparição do elemento que passamos como parâmetro.
```

C)

Refazendo a lista e removendo os elementos manualmente, pois o Python não permite que sejam removidos elementos de uma lista.

```
Isto não precisa ser feito manualmente, o Python nos permite remover elementos com funções específicas.
```

## 06.Faça como...

## 07. O que aprendemos?

O que aprendemos nesta aula:

* O que é coleção;
* Criar lista;
* Verificar o tipo da lista e o tamanho da lista;
* Mostrar na tela o valor conforme sua posição na lista;
* Alterar valores que estão dentro da lista;
* Adicionar valores no final da lista;
* Percorrer a lista;
* Remover elemento da lista;
* Remover **todos** elementos da lista;
* Verificar se o elemento está dentro da lista;
* Inserir um elemento na posição que desejamos;
* Utilizar um list comprehension;
* Fazer filtragens;
* Criar uma função e deixar um valor padrão;
* Quais são os problemas da mutabilidade.
