Computação Embarcada
==================
* Insper - www.insper.edu.br 
* Curso     : Computação - quinto semestre 
* Professor : Rafael Corsi - rafael.corsi@insper.edu.br
* Aulas     : Segunda e Quarta Feira (15h45-17h45)

# Repositório 
O Repositório está estruturado da seguinte maneira :

- Códigos : Códigos utilizados como exemplo para o desenvolvimento das atividades;
- Leituras complementares : Materiais extra que acho interessante e compartilho com vocês;
- Estudo dirigido e Projetos : As atividades que devem ser realizadas durante as aulas e devem ser entregues;
- Material Aulas : Os slides utilizados em sala de aula, eles estão separados por conteúdo e não por aula, cada conteúdo é numerado como : 01, 02, 03. e.x: A primeira aula foi composta pelos conteúdos 1,2,3,4 ... ;
- Softwares Extras : Softwares a serem utilizados ao longo do curso ;

## Objetivos de Aprendizagem

Capacitar o aluno para projetar e desenvolver sistemas computacionais embarcados, com o enfoque na otimização do software para microcontroladores e suas interfaces. Um projeto será desenvolvido para a aplicação dos conceitos e técnicas em um sistema real.

1.  Criar softwares para microcontroladores utilizando suas especificidades (periféricos/ low power);

2.  Avaliar e melhorar soluções embarcadas integrando hardware/software levando em conta adequação a uma aplicação;

3.  Integrar em um protótipo hardware, software básico, sistema operacional de tempo real e módulos de interfaceamento com usuários, de comunicação e de alimentação;

4.  Compreender as limitações de microcontroladores e seus periféricos;

5.  Buscar e analisar documentação (datasheet) e extrair informações relevantes.

# Outline
![selecao_005](https://cloud.githubusercontent.com/assets/1039615/22657938/5fcb0cf6-ec7f-11e6-9f44-baccefb723ce.png)

## Objetivo

Visão Geral do curso:

O domínio da programação e especificação de sistemas embarcados é essencial para o projeto de praticamente qualquer dispositivo eletrônico. Conceitos atuais tais como: IoT, Smart Grid, sistemas autônomos, fazem uso extensivo de computação embarcada para viabilização de seus projetos.

Os projetos de sistemas embarcados estão normalmente atrelados a outras grandes áreas do conhecimento, e requerem a habilidade de interdisciplinaridade para compreensão do problema e proposição de soluções. Sistemas médicos, automobilísticos, entretenimento e militar são exemplos de grandes usuários dessa tecnologia. Devido ao seu baixo custo, baixo consumo energético e grande diversidade de escolhas os microcontrolados (uC) são os atores principais desses dispositivos1, sendo a primeira opção no desenvolvimento de projetos de computação embarcada 2.

A diversidade de microcontroladores encontrados no mercado difere em muito da dos processadores para computador em dois aspectos: a. existe dezenas de milhares de diferentes opções de famílias e modelos de microcontroladores a serem escolhidos pelos desenvolvedores; b. as inovações tecnológicas aparecem para o desenvolvedor de forma mais rápida. O desenvolvimento de aplicações microcontroladas não pode deve ser feita da mesma maneira com que se desenvolve aplicações típicas para computadores, os principais fatores que levam a isso são :

- Escassez de recursos : Memória, processamento e energia são recursos escassos no desenvolvimento de aplicações embarcadas;
- Interface hardware/software : A programação de uC envolve controlar sinais digitais e analógicos via software, o que implica na necessidade do maior conhecimento do hardware envolvido no projeto.
- Tempo real : A execução de tarefas em sistemas embarcados normalmente são consideradas críticas, pequenos atrasos na execução pode levar a um grande prejuízo (abs, marcapasso, …).

# Dinâmica:	
	O curso terá simultaneamente duas frentes. A primeira será o desenvolvimento de um projeto que envolva computação embarcada proposto pelos alunos em grupos. A segunda frente tratará de assuntos técnicos essenciais a disciplina abordando técnicas de programação e de designer de sistemas embarcados. As duas frentes serão executadas de forma concorrente com aulas alternadas entre elas.

## Projeto:

Os projetos serão realizados em grupos com o tópico selecionado a partir de uma dinâmica coletiva de seleção. Os projetos deverão conter necessariamente requisitos de computação embarcada (microprocessador), e deverão ser executados utilizando o kit de desenvolvimento proposto em sala (Atmel SAME-70).

No percurso do desenvolvimento do projeto, os grupos deverão criar um blog e realizar postagens técnicas referentes ao projeto contendo informações técnicas, especificação, material, cronograma. Os grupos deverão produzir um vídeo contendo a demonstração final do projeto. A fig. [fig:trabalho] contém o detalhamento das etapas de execução do projeto com os pontos de avaliações avaliação (A,B,…).

![dinamicaprojeto](https://cloud.githubusercontent.com/assets/1039615/22658000/a779b7dc-ec7f-11e6-9171-10d58d9f5fa8.png)

### Etapas de execução do projeto :
1. Ideia : etapa onde serão feitas as propostas de projeto de forma individual (mínimo 2)
2. Desenvolvimento da proposta : será escolhido uma das propostas para maior detalhamento
3. Peer review : com a proposta estruturada, uma analise em pares será realizada para sua melhoria
4. Seleção dos projetos : os alunos irão apresentar suas propostas e a sala coletivamente com base em votação selecionará os projetos vencedores, formam-se os grupos.
5.  Estruturação do projeto : os grupos deverão apresentar um documento técnico contendo informações detalhadas do desenvolvimento do projeto, tal como : material, diagrama de blocos, cronograma de execução, descritivo técnico.
6. Compra de material : caso necessário será disparado aqui a compra de materiais.
7. Prototipação : inicia-se a prototipação do projeto e sua validação.
8. Atualização da documentação : os alunos deverão constantemente atualizar o blog com novidades do projeto.
9. Apresentação final : os projetos serão apresentados para a sala e avaliados.

## Tópicos técnicos:
Ao longo do curso será apresentando tópicos de cunho técnico com o intuito de guiar e complementar o aprendizado obtido através do desenvolvimento do projeto. Os tópicos serão sempre relacionados a situações reais e contextualizado com o universo da computação embarcada e outras áreas da engenharia.

Os tópicos são acompanhados de um estudo dirigido que deve ser realizado previamente a aula, e entregue nesse dia. Esses estudos são uma guia para o desenvolvimento do aprender a aprender, bastante incentivado na disciplina. Cada tópico técnico terá também um atividade de programação que os alunos devem desenvolver em grupos.

![dinamicatecnica](https://cloud.githubusercontent.com/assets/1039615/22658003/ab1cf958-ec7f-11e6-9c9f-67a072d02949.png)


# Licença
Material liberado sob licença:
 * GNU General Public License v2.0


[1] Possui um mercado estimado em $15.8 bilhões de dólares (2014)

