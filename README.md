### Jogo da Velha

<hr>

#### Módulos

Os códigos abaixo fazem a importação de duas bibliotecas.
<details><summary>Choice</summary>
Esse módulo é reponsável por realizar uma escolha random, ou seja, uma escolha aleatória. Esse trecho será utilizado na lista "possibilidades".

</details>

``` python
from random import choice
```

<details><summary>Sleep</summary>
Responsável por fazer o trecho de código esperar o tempo que for indicado pelo dev.
</details>

``` python
from time import sleep
```

<hr>

#### Listas

<details><summary>Possibilidades</summary>
 São todos os caminhos que podemos fazer em um Jogo da Velha.
</details>

``` python
possibilidades = ["0,0","0,1","0,2","1,0","1,1","1,2","2,0","2,1","2,2"]
```
<details><summary>Tabuleiro</summary>
 Nada mais é que o layout do tabuleiro de Jogo da Velha. Ele será impresso como uma matriz.<table style="width:100%">
  <tr>
    <th> </th>
    <th>0</th>
    <th>1</th>
	<th>2</th>
  </tr>
  <tr>
    <td><b>0</b></td>
    <td></td>
	<td></td>
    <td></td>
  </tr>
  <tr>
    <td><b>1</b></td>
    <td></td>
	<td></td>
    <td></td>
  </tr>
    <tr>
    <td><b>2</b></td>
    <td></td>
	<td></td>
    <td></td>
  </tr>
</table>


 Para representar o tabuleiro iremos chamar a linha desejada, e em seguida a coluna desejada.
 Exemplo:
<table>
  <tr>
    <th> </th>
    <th>0</th>
    <th>1</th>
	<th>2</th>
  </tr>
  <tr>
    <td><b>0</b></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><b>1</b></td>
    <td> </td>
    <td><b>Y</b></td>
    <td></td>
  </tr>
    <tr>
    <td><b>2</b></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  </table>

 Para substituirmos o **Y** por um **X** devemos indicar sua Linha, que seria a segunda linha, ou seja, o número **1** na matriz, já que a mesma começa com **0**.
Agora iremos chamar a coluna desejada, que seria a terceira coluna, ou seja, o número **2**.

Vamos supor que a matriz se chame **Teste_Matriz**, então iremos escrever o códgio como _Teste_Matriz[1][2]_, respeitando sempre a ordem, Linha x Coluna.

</details>

``` python
tabuleiro = [["_","_","_"],["_","_","_"],["_","_","_"]]
```
<hr>

#### Funções
<details><summary>Remove possibilidades</summary>

 A função é responsável por eliminar as possibilidades digitadas pelo jogador. Assim nenhuma jogada poderá se repetir.
 O código procura o index (posição) do número digitado na lista **possibilidades** , retirando esse número em seguida para que o mesmo não se repita.
 O argumento passado é o número digitado pelo usuario. O valor será enviado como tipo **String**(tipo da variável = texto).
</details>

``` python
def remove_possibilidades(numero):
    try:
        index = possibilidades.index(numero)
        possibilidades.pop(index)
    except:
        pass
```
<hr>
<details><summary>Verifica se há possibilidades</summary>

Essa função é responsável por verificar se a lista possibilidades está vazia, pois caso a função **remove_possibilidades(numero)**, ja foi executada todas as vezes possiveis, o programa chama a **função fim_de_jogo()**.

Caso não esteja vazio, o codigo verifica se o número digitado pelo usuario existe na lista **possibilidades**, caso não exista quer dizer que o número foge do padrão, ou ele já foi digitado antes, evitando repetições de movimento.
Caso o número exista, o código chama a função **remove_possibilidades(numero)**.
Caso o número não exista, a função retorna **False**.

</details>

``` python
def verifica_possibilidades(n):
    if possibilidades == []:
        fim_de_jogo()
    else:
        if n in possibilidades:
            remove_possibilidades(n)
            return True
        else:
            return False
```

<hr>
<details><summary>Verifica o ganhador</summary>
Primeiramente é criado uma lista com várias listas, onde cada uma tem três elementos.
Cada lista dentro de **ganhar** é uma posição de vitória no Jogo da Velha.

```python
from time import sleep
```

```python
ganhar = [
[tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]],
[tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]],
[tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]],
[tabuleiro[0][0],tabuleiro[1][1],tabuleiro[2][2]],
[tabuleiro[0][2],tabuleiro[1][1],tabuleiro[2][0]],
[tabuleiro[0][0],tabuleiro[1][0],tabuleiro[2][0]],
[tabuleiro[0][1],tabuleiro[1][1],tabuleiro[2][1]],
[tabuleiro[0][2],tabuleiro[1][2],tabuleiro[2][2]],
]
```
<table>
	<tr>
		<th>Código</th>
		<th>Layout</th>
	</tr>
	<tr>
		<td>tabuleiro[0][0] tabuleiro[0][1] tabuleiro[0][2]</td>
		<td>
		|X|X|X|
		|_|_|_|
		|_|_|_|
		</td>
	</tr>
	<tr>
		<td>tabuleiro[1][0] tabuleiro[1][1] tabuleiro[1][2]</td>
		<td>
		|_|_|_|
		|X|X|X|
		|_|_|_|
		</td>
	</tr>
	<tr>
		<td>tabuleiro[2][0] tabuleiro[2][1] tabuleiro[2][2]</td>
		<td>
		|_|_|_|
		|_|_|_|
		|X|X|X|
		</td>
	</tr>
	<tr>
		<td>tabuleiro[0][0] tabuleiro[1][1] tabuleiro[2][2]</td>
		<td>
		|X|_|_|
		|_|X|_|
		|_|_|X|
		</td>
	</tr>
	<tr>
		<td>tabuleiro[0][2] tabuleiro[1][1] tabuleiro[2][0]</td>
		<td>
		|_|_|X|
		|_|X|_|
		|X|_|_|
		</td>
	</tr>
	<tr>
		<td>[tabuleiro[0][0] tabuleiro[1][0] tabuleiro[2][0]</td>
		<td>
		|X|_|_|
		|X|_|_|
		|X|_|_|
		</td>
	</tr>
	<tr>
		<td>[tabuleiro[0][1] tabuleiro[1][1] tabuleiro[2][1]</td>
		<td>
		|_|X|_|
		|_|X|_|
		|_|X|_|
		</td>
	</tr>
	<tr>
		<td>[tabuleiro[0][2] tabuleiro[1][2] tabuleiro[2][2]</td>
		<td>
		|_|_|X|
		|_|_|X|
		|_|_|X|
		</td>
	</tr>
</table>

Em seguida ele irá comparar se em alguma posição há uma sequencia de **X** ou uma sequencia de **O**.
Caso na lista **ganhar** haja essa sequencia, ele dará a vitoria a um dos jogadores.
O programa faz a verificação, apresenta uma mensagem(dependendo da posição, a mensagem tem uma cor diferente. Vermelho para "YOU LOSE!!!", e verde para "Player 1 WIN!!!"). O código irá chamar a função **exibe()**, e em seguida a função **fim_de_jogo()**, encerrando o programa.

``` python
    if ["X","X","X"] in ganhar:
        print("\033[042m Player 1 WIN!!!!\033[0m")
        exibe()
        fim_de_jogo()
```
Se a sequencia que estiver na lista for de **O**, então o usuario perde o jogo. Exibindo a mensagem **YOU LOSE!!!**
Exibindo a matriz e encerrando o programa.
``` python
if ["O","O","O"] in ganhar:
        print("\033[041m YOU LOSE!!!!\033[0m")
        exibe()
        fim_de_jogo()
```
</details>

``` python
def verifica_ganhador():
    ganhar = [
    [tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]],
    [tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]],
    [tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]],
    [tabuleiro[0][0],tabuleiro[1][1],tabuleiro[2][2]],
    [tabuleiro[0][2],tabuleiro[1][1],tabuleiro[2][0]],
    [tabuleiro[0][0],tabuleiro[1][0],tabuleiro[2][0]],
    [tabuleiro[0][1],tabuleiro[1][1],tabuleiro[2][1]],
    [tabuleiro[0][2],tabuleiro[1][2],tabuleiro[2][2]],
    ]

    if ["X","X","X"] in ganhar:
        print("\033[042m Player 1 WIN!!!!\033[0m")
        exibe()
        fim_de_jogo()
    if ["O","O","O"] in ganhar:
        print("\033[041m YOU LOSE!!!!\033[0m")
        exibe()
        fim_de_jogo()
```

<hr>
<details><summary>Primeiro Jogador (Usuário)</summary>
A função **jogar** tem o objetivo de pegar o valor digitado pelo usuario e colocar esse valor na variavel **n**.

Em seguida ele faz a verificação das possibilidades do jogo, visualizando se **verifica_possibilidades(n)** é verdadeiro(True). Caso seja **True** quer dizer que o valor digitado pelo usuário está presente na lista **possibilidades** eliminando o fato desse valor nunca ter sido digitado no código. Em seguida esse valor será eliminado da lista **possibilidades** e será incorporado a matriz, na posição digitada, o codigo insere um simbolo, **X** para o usuário, e **O** para a máquina.
 A forma que foi encontrada para o codigo saber qual dos dois jogadores fez essa requisição, foi inserido uma variavel chamada **jogador**. Essa variavel irá receber **1**, caso a requisição seja do usuário, e **2** para a máquina.
O codigo chama a função **jogo**, passando os paramentros de número digitado pelo usuario **n**, e o código identificado para jogador **jogador**, que será igual a **1**.
Caso haja algum erro referente ao valor digitado, a função irá se chamar, fazendo com que o usuário seja obrigado a digitar um valor correto para o código poder rodar.
</details>

``` python
def jogar():
    n = str(input("Digite um valor: "))
    if verifica_possibilidades(n) == True:
        jogador = 1
        jogo(n,jogador)
    else:
        jogar()
```

<hr>
<details><summary>Segundo Jogador (NPC)</summary>

Essa função é utilizada para representar a "máquina", ou seja, o computador que irá jogar contra o usuário.

Caso ainda haja valores na lista **possibilidades**, o código irá utilizar o **random choice**, ou seja, uma escolha aleatória entre os valores ainda disponiveis na lista ja mencionada. Caso não exista valor algum na lista, o código chama o **fim_de_jogo()**, encerrando o programa. Isso ocorrerá quando o jogo não tiver ganhador, ou seja, **DEU VELHA**.

A segunda parte do código, está presente também em **jogar()**.

</details>

``` python
def jogar2():
    try:
        n = choice(possibilidades)
    except:
    	print("DEU VELHA!!!")
        fim_de_jogo()
    if verifica_possibilidades(n) == True:
        jogador = 2
        jogo(n,jogador)
    else:
        jogar2()

```

<hr>
<details><summary>Jogo</summary>

A função **jogo(n,jogador)** fará o tratamento dos dados enviados, e fará a verificação com base no jogador, ele insere **X** ou **O**, na posição informada.
Exemplo:

**jogo(n,jogador)**
O código recebe **n**. Vamos supor que **n** seja igual a "2,1" e jogador seja igual a "1".
Ele separa **n** por virgula, transformando **n** em uma lista com dois elementos.

<table>
<tr>
<td>n[0]</td>
<td>2</td>
</tr>
<tr>
<td>n[1]</td>
<td>1</td>
</tr>
</table>

Em seguida pegamos o valor de n[0] e n[1] e transformamos eles em tipo inteiro(*int*)

Em seguida verificamos qual é o valor de jogador, se jogador for igual a 1, o codigo insere o simbolo **X**, caso seja igual a 2 o codigo insere o simbolo **Y**, ele realiza a troca do valor anterior inserido em _tabuleiro[n[0]][n[1]]_ que seguindo a exemplo acima, seria a posição do tabuleiro na linha de numero 2 (terceira linha) e na coluna de número 1 (segunda coluna).

Em seguida o codigo chama a função **verifica_ganhador()** e chama a função **exibe()**
</details>

``` python
def jogo(n,jogador):
    n = n.split(",")
    n[0] = int(n[0])
    n[1] = int(n[1])
    if jogador == 1:
        tabuleiro[n[0]][n[1]] = "X"
    elif jogador == 2:
        tabuleiro[n[0]][n[1]] = "O"
    verifica_ganhador()
    exibe()
```

<hr>
<details><summary>Exibir Matriz (Layout do Jogo)</summary>

A função **exibe()** é responsável por exibir a matriz. Sempre que chamada ela apresenta na tela os valores que estão na lista **tabuleiro**.
</details>

``` python
def exibe():
    print(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2])
    print(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2])
    print(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2])
    print(10*"-")

```

<hr>
<details><summary>Fim de Jogo (encerrar o programa)</summary>

Essa função é reponsavel por encerrar o programa.
</details>

```python
def fim_de_jogo():
	exit()
```
<hr>
<details><summary>Rodar o código</summary>
Esse trecho do código imprime na tela a frase ***"Para jogar digite uma das possibilidades apresentadas"***.
Em seguida um looping é criado.

Enquanto o tamanho total da lista **possibilidades** for maior que zero faça:

``` python
while len(possibilidades) > 0:
```

Neste trecho do código ele irá apresentar uma mensagem com todas as possibilidades possiveis de jogo.
Chama o **jogar()** onde o usuário irá digitar a possição desejada.
Em seguida iremos chamar a função **jogar2()**, que representa a jogada do computador.

``` python
    print("As possiblidades são: {}\n".format(possibilidades))    
    jogar()
    jogar2()
```
</details>

``` python
print("Para jogar digite uma das possibilidades apresentadas")
while len(possibilidades) > 0:
    print("As possiblidades são: {}\n".format(possibilidades))    
    jogar()
    jogar2()
    print("\nA quantidade de possibilidades possiveis é {}".format(len(possibilidades)))
```



