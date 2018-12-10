
# Task - DevOps Engineer 

<img src="app/img/semantix.png" alt="drawing" style="width:100px;"/> </img>

### Table of Contents

1. [Descrição e melhorias aplicadas](#desc)
    - 1.1 [Solução anterior](#sol_ant)
    - 1.2 [Otimização da API](#otim)
    - 1.3 [Análise do desempenho obtido](#result)
    - 1.4 [Possíveis modificações futuras](#future)
    
2. [Instruções de uso ](#instruct)
    - 2.1 [Pré-requisitos](#pre_requisits)
    - 2.2 [Tarefa 1](#task_1)
    - 2.3 [Tarefa 2](#task_2)


<a name="desc"></a>
## 1.0 Descrição e melhorias aplicadas

<a name="sol_ant"></a>
### 1.1 Solução anterior

A API anterior contava com o recebimento de solicitações **GET** por meio de um single-thread e de 
forma síncrona, ou seja, cada solicitação é recebida, processada e por fim atendida. 

O processamento de cada solicitação inclui uma tarefa de busca em um dicionário em memória.
Dado um texto, é necessário identificar todos os registros que possuem as palavras contidas no 
texto buscado. 
Em todos os casos, essa busca possui complexidade **O(XN)**, no qual: 

    X: Quantidade de palavras existentes no texto de busca.
    N: Quantidade de registros do dicionário.

<a name="otim"></a>
### 1.2 Otimização da API
As primeiras modificações realizadas em relação ao codigo original foram: 

* Reescrita do código, adotando conceitos de programação funcional.

* Paralelismo no recebimento de requisições através de sub-processos.

* Alteração do algoritmo de busca, 
com o objetivo de tornar o algoritmo menos complexo no quando analisado o custo computacional
    * A cada iteração, o algoritmo diminui o espaço de busca utilizado, conforme restrições impostas em iterações anteriores.

* Adoção de arquivos de configuração .yml para facilitar a mudança de variáveis posteriormente.
 
<a name="future"></a>
### 1.3 Possíveis modificações futuras 

* Construção de um dicionário que é populado conforme a chegada de novas requisições:
a adoção desta solução tem finalidade de atuar como um cache, 
afim de reduzir a complexidade computacional da busca à O(1) no melhor caso (se o mesmo texto já foi buscado anteriormente).
               
    > Ponto positivo: A complexidade computacional de 
    requisições com valores frequentes é O(1)
   
    > Ponto negativo: Ocupa mais memória.*

### 1.3 Análise do desempenho obtido

![Benchmark](app/img/output.png)

 

## 2.0 Instruções de uso 

### 2.1 Pré-requisitos

    Docker previamente configurado.

### Tarefa 1 

Dentro do diretório criado, execute o comando:

    > docker-compose up

Este comando carregará todas as configurações contidas no Dockerfile, além disso, empregará configurações adicionais
que estão sinalizadas no *docker-compose.yml*

Após esta etapa, o container criado estará pronto para uso. 

Para testar se o serviço contido no docker funciona, execute uma chamada simples via curl: 

    > curl http://localhost:4000/s/fun%20city
    
**obs.: O serviço estára escutando chamadas na porta 4000.**



    

