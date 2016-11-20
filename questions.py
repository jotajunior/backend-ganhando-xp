# -*- coding: utf-8 -*-
questions = [
        {
            'id': 1, 
            'question': 'A disciplina de testes é mais eficaz que as revisões para remoção de defeitos.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'F', 
            'explanation': 'A disciplina de testes é menos eficaz que as revisões para remoção de defeitos. Ela detecta defeitos que escapam das revisões. ', 
        },
        { 
            'id': 2, 
            'question': 'Testes são indicadores de qualidade mais do que meios de detecção e correção de erros.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'V', 
            'explanation': 'Quanto maior o número de defeitos encontrados durante a realização dos testes, provavelmente maior o número de defeitos não-detectados. Um número anormal de defeitos em testes sugere um redesenho. ', 
        },

        {
            'id': 3, 
            'question': ' A remoção de defeitos é a parte que consome mais tempo do ciclo de vida',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'V', 
            'explanation': ' É quase impossível uma boa remoção de erros sem ferramentas. Em geral utiliza-se depuradores. ', 
        },
        {
            'id': 4, 
            'question': 'Implementadores são indicados para testar seu próprio código.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'F', 
            'explanation': 'Implementadores não são indicados para testar seu próprio código, dado que autores têm mais dificuldade em enxergar problemas.', 
        },

        {
            'id': 5, 
            'question': ' Os casos de teste têm por objetivo demonstrar que o programa funciona. ',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'F', 
            'explanation': 'Os casos de teste têm por objetivo detectar defeitos e não demonstrar que o programa funciona.', 
        },

        {
            'id': 6, 
            'question': 'Casos de teste têm ordem especificada de execução.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'V', 
            'explanation': 'A execução correta pode depender do estado da base de dados, produzido pela execução bem-sucedida do caso anterior.', 
        },

        {
            'id': 7, 
            'question': ' Os testes alfa são executados no ambiente do cliente.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'F', 
            'explanation': 'Os testes alfa são executados no ambiente do fornecedor. São os testes beta que são executados no ambiente do cliente.', 
        },

        {
            'id': 8, 
            'question': 'Os testes de desenvolvimento são executados pelos próprios desenvolvedores.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'V', 
            'explanation': 'Os testes de desenvolvimento fazem parte da implementação e são executados pelos própios desenvolvedores.', 
        },

        {
            'id': 9, 
            'question': 'Uma partição de equivalência divide o domínio de entrada em categorias de dados.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'V', 
            'explanation': 'Neste caso, cada categoria revela uma classe de erros e permite que casos de teste na mesma categoria sejam eliminados sem que se prejudique a cobertura de testes.', 
        },

        {
            'id': 10, 
            'question': 'A análise do valor limite analisa erros nas fronteiras do domínio de saída.',
            'F': 'Falso', 
            'V': 'Verdadeiro', 
            'correct': 'F', 
            'explanation': 'A análise de valores limites analisa erros nas fronteiras do domínio de entrada, mais frequentes do que nas regiões centrais.', 
        },
        { 
            'id': 11, 
            'question': '  Do ponto de vista de Engenharia de Software, o que é um defeito?', 
            'A': 'É o programa apresentar falhas durante a execução', 
            'B': ' É o programa ser lento', 
            'C': 'É o não atendimento dos requisitos', 
            'correct': 'C', 
            'explanation': 'Segundo o PMBOK, um deifeito é “uma imperfeição ou deficiência em um componente do projeto na qual esse componente não atende aos seus requisitos ou especificações e precisa ser reparado ou substituído” ', 
        },

        { 
            'id': 12, 
            'question': ' O que é um procedimento de teste?', 
            'A': ' É uma ação de se testar partes do programa e depois o todo ', 
            'B': ' É um conjunto roteiros e procedimentos para execução de um teste', 
            'C': ' É a descrição detalhada de apenas um tipo de teste ', 
            'correct': 'B', 
            'explanation': ' Um procedimento de teste é um conjunto detalhado de instruções para execução de testes.', 
        },

        { 
            'id': 13, 
            'question': ' Os testes que cumprem papel dentro de um processo são:', 
            'A': ' Qualificação, Operacionais, Sistema, Alfa, Beta, Regressão, Desenvolvimento ', 
            'B': 'Teste de caixa branca, cinza e preta' ,
            'C': ' Desenho de teste e teste unitário', 
            'correct': 'A', 
            'explanation': 'Tais testes se enquadram no aspecto do papel dentro dos processos ', 
        },

        { 
            'id': 14, 
            'question': ' Qual a diferença entre teste de caixa branca e teste de caixa preta?', 
            'A': ' Um é feito no ambiente do desenvolvedor e o outro no ambiente do usuário ', 
            'B': 'A diferença entre está no fato de um testar os módulos individualmente e o outro o todo' ,
            'C': 'No teste de caixa branca, conhece-se os mecanismos internos o que não ocorre no segundo ', 
            'correct': 'C', 
            'explanation': 'Os testes de caixa preta ignoram os mecanismos internos, focalizando apenas nas saídas geradas por entradas e condições de execução selecionadas. Já os testes de caixa-branca levam em conta os mecanismos internos do sistema ou componente. ', 
        },

        { 
            'id': 15, 
            'question': ' Um jovem guerreiro do software gostaria de testar um software novo desenvolvido. Ao adquirir esse software, ele vai para o campo de batalha, mas um defeito em uma parte do software faz com que ele perca a batalha. Quais o teste resolveria esse problema?', 
            'A': '  Teste de partição de equivalência ', 
            'B': ' Teste Operacional' ,
            'C': ' Teste unitário e teste de integração', 
            'correct': 'C', 
            'explanation': ' Os testes de unidade testam unidades individuais ou grupos de unidades. Já os testes de integração testam componentes combinados, de modo a avaliar sua interação. ', 
        },

        { 
            'id': 16, 
            'question': ' O que é um teste destrutivo?', 
            'A': ' É um procedimento que pretende fazer com que o hardware pare de funcionar ', 
            'B': ' É um teste que tenta provocar alguma falha no software, aplicando, por exemplo, uma entrada inválida nele' ,
            'C': 'É um teste feito por clientes a fim detectar falhas de segurança', 
            'correct': 'B', 
            'explanation': ' Um teste destrutivo é um teste que tentar provocar uma falha no software.  ', 
        },

        { 
            'id': 17, 
            'question': ' A realização de testes é limitada por:', 
            'A': ' Pessoal e software especializado', 
            'B': 'Cronograma e orçamento' ,
            'C': ' Mão de obra qualificada', 
            'correct': 'B', 
            'explanation': ' Em geral a realização de testes é limitado por cronograma e orçamento. Por isto, os testes devem ser planejados e desenhados. ', 
        },

        { 
            'id': 18, 
            'question': ' Sobre o objetivo de teste, é INCORRETO afirmar que:', 
            'A': 'É um conjunto identificado de características de software.', 
            'B': 'Compara-se o comportamento real com o requerido.' ,
            'C': 'Podem haver testes sem objetivo.', 
            'D': ' Deve ser medido sob condições específicas. ', 
            'correct': ' C', 
            'explanation': ' Cada teste tem pelo menos um objetivo.', 
        },

        { 
            'id': 19, 
            'question': ' Um caso de teste NÃO espicifica, para um dado item a testar: ', 
            'A': 'Resultados de testes anteriores.', 
            'B': ' Entradas' ,
            'C': 'Resultados previstos ', 
            'D': ' Condições de execução', 
            'correct': 'A', 
            'explanation': ' Um caso de teste especifica, para um dado item a testar, as entradas, os resultados previstos e as condições de execução. Eles tem por objetivo detectar defeitos.', 
        },

        { 
            'id': 20, 
            'question': ' É ERRADO afirmar, com relação aos testes de sistema:', 
            'A': 'Responsáveis por verificar a conformidade com requisitos', 
            'B': 'São divididos em testes funcionais e não-funcionais.' ,
            'C': 'Os testes funcionais avaliam, por exemplo, o desempenho, a usabilidade e a segurança do sistema.', 
            'D': 'São especificados e executados por equipes de testes.' , 
            'correct': 'C', 
            'explanation': 'Os testes funcionais avaliam a conformidade com os requisitos funcionais. São os testes não-funcionais que avaliam coisas como o desempenho, a usabilidade e a segurança do sistema, que são requisitos não-funcionais.', 
        },
        ]
