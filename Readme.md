# Regua-Puzzle Trabalho de IA
![](https://img.shields.io/badge/Language-C++-green)
![](https://img.shields.io/badge/Platforms-Linux%20%7C%20Windows-lightgrey)
 
Repositório criado para o trabalho prático de DCC014-2022.1-A - Inteligência Artificial. O trabalho é para criar uma série de algoritmos informados e não informados para o problema do Regua Puzzle.

Feito por [Luan Reis Ciribelli](https://github.com/LuanCiribelli) e [João Pedro Lima](https://github.com/joaop-c-lima). 
 
 ## Para a execução do programa

 Primeiro deve se usar, no terminal, o MakeFile para compilar o executavel que terá o nome de "reguaPuzzle.exe". Com o comando:

 ```
$ make
```
 Em seguida, existem duas opções. Rodar o programa e criar a régua manualmente, sem arquivo de entrada ou saida. Que nesse caso deve se o usar o comando: 

  ```
./reguaPuzzle.exe
```
Ou o equivalente no windows.

E, a outra opção é passar um arquivo txt de entrada e de saida, com : 

```
./reguaPuzzle.exe entrada.txt saida.txt
```

 ## Formato arquivo de entrada:

 O arquivo de entrada deve ter _apenas_ os caracteres 'P', 'B' e '-'. Além disso deve-se ser finalizado com ';'. É importante notar que devido as regras do Regua Puzzle, é preciso ter a mesma quantidade de peças pretas e brancas.