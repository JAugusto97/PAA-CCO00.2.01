# PAA-CCO00.2.01
## Processo Seletivo
Ramón Hackerman é o gerente de RH da empresa QS (Qualidade Seguros).
Ese ano, a QS está fazendo um processo seletivo muito concorrido. Para reduzir o
número de pessoas a serem entrevistadas, Ramón propôs a realização de uma prova
eliminatória como a primeira fase do processo. Após coletar as notas obtidas nessa
prova, Ramón seleciona um número máximo de pessoas para serem entrevistada. No
entanto, antes de divulgar o resultado, Ramón quer saber a menor nota tirada dentre
um determinado número de pessoas. Ou seja, se Ramón pretende selecionar dez
pessoas, ele quer consultar qual foi a décima maior nota alcançada nesse período.
Porém, o volume de dados é muito grande e Ramón precisa de ajuda. A primeira
fase foi realizada com candidatos para diferentes vagas. Para cada cada uma delas,
Ramón quer fazer uma ou mais consultas como a descrita acima. Escreva um
programa que auxilie Ramón nessa tarefa.

## Entrada
A entrada contém um único caso de teste. A primeira linha indica o número
inteiro N (2 ≤ N ≤ 100) de vagas oferecidas. As próximas N linhas contêm as notas dos
candidatos e a consulta que deve ser realizada, no seguinte formato. A linha é iniciada
por um inteiro K (1 ≤ K ≤ 100), indicando quantas pessoas serão, potencialmente,
chamadas para a segunda fase daquela vaga. A seguir, é apresentado um número
inteiro C (10 ≤ C ≤ 106
), indicando o número de candidatos que concorreram à vaga.
Por fim, são apresentados C números reais R (0.0 ≤ R ≤ 100.0) indicando a nota obtida
por cada um dos candidatos. Neste problema, é garantido que K ≤ C em todos os
casos de teste.
Saída
Ao final da execução, seu programa deve imprimir um único valor real para cada vaga,
indicando qual é K-ésima maior nota obtida. A saída deve ser um número real com
duas casas de precisão.

## Exemplo de entrada
```
3
3 10 75.2 45.3 23.4 35.9 77.7 52.7 66.6 98.3 88.9 12.3
5 8 11.1 22.2 33.3 44.4 55.5 66.6 77.7 88.8
1 5 25.8 97.3 99.9 95.4 89.7
```

## Saída esperada para o exemplo
```
77.70
44.40
99.90
```

## Autores
Caio Ueno  
João Augusto Leite