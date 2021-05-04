# Test-Driven-Development

**Test Driven Development** solution on roman number translation problem.  

(portuguese)
O TDD parte do princípio de que, compreendido um determinado problema, é possível pensar nos testes que irão garantir a qualidade da solução que irá resolver o problema, antes mesmo de se ter a solução.  
  
A qualidade da solução a ser desenvolvida passa a ser diretamente relacionada à qualidade do conjunto de teste utilizado como base para o TDD. Desse modo, projetar o conjunto de teste inicial com base em critérios de teste é de grande importância para o sucesso da aplicação do TDD.  
  
Considere a descrição a seguir para aplicar os conceitos do TDD.  

“Numerais romanos foram criados na Roma Antiga e eles foram utilizados em todo o seu império. Os números eram representados por sete diferentes símbolos, listados na tabela a seguir.

I, unus, 1, (um)

V, quinque, 5 (cinco)

X, decem, 10 (dez)

L, quinquaginta, 50 (cinquenta)

C, centum, 100 (cem)

D, quingenti, 500 (quinhentos)

M, mille, 1.000 (mil)

Para representar outros números, os romanos combinavam estes símbolos, começando do algarismo de maior valor e seguindo a regra:

Algarismos de menor ou igual valor à direita são somados ao algarismo de maior valor;

Algarismos de menor valor à esquerda são subtraídos do algarismo de maior valor.

Por exemplo, XV representa 15 (10 + 5) e o número XXVIII representa 28 (10 + 10 + 5 + 1 + 1 + 1). 

Há ainda uma outra regra: nenhum símbolo pode ser repetido lado a lado por mais de 3 vezes. Por exemplo, o número 4 é representado pelo número IV (5 - 1) e não pelo número IIII. 

