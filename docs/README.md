## Contextualização
* A Pesquisa Nacional de Saúde (PNS), realizada pelo IBGE em parceria com o Ministério da Saúde, é o mais completo inquérito domiciliar do Brasil, com edições em 2013 e 2019. Seu propósito é investigar as condições de vida e saúde da população, servindo de base para a formulação de políticas públicas.
* Dentro do ambito da saúde é questionado desde alimentação a exeriência de atendimentos do setor da saúde. O objetivo geral deste projeto é analisar e comparar padrões de vida, hábitos alimentares e experiências no sistema de saúde entre indivíduos diagnosticados com Asma e indivíduos sem doenças crônicas, utilizando a base de dados PNS 2019, a fim de identificar determinantes de saúde e propor pontos de melhoria no manejo da condição.
## Escolha dos Atributos
* V0001 - Unidade da Federação (primeiro digito equivale a Região)
* V0026 - Tipo de situação censitária (Morador urbano ou rural)
* C6. Gênero 
* C8. - Idade 
* M011071 - No(s) seu(s) trabalho(s), o(a) Sr(a) está exposto(a) a algum destes fatores que podem afetar a sua saúde Exposição à poeira mineral (pó de mármore, de areia, de brita, de vidro (sílica), de amianto (asbesto), de ferro ou aço)
* P00104 - Peso - Final (em kg)
* P00404 - Altura - Final (em cm)
* P10a. - Em geral, o(a) Sr(a) costuma comer esse tipo de verdura ou legume: 
* P9a. - Em quantos dias da semana, o(a) Sr(a) costuma comer pelo menos um tipo de verdura ou legume (sem contar batata, mandioca, cará ou inhame) como alface, tomate, couve, cenoura, chuchu, berinjela, abobrinha?
* P15. - Em quantos dias da semana, o(a) Sr(a) costuma comer peixe?
* P02001 - Em quantos dias da semana o(a) Sr(a) costuma tomar suco de caixinha/lata ou refresco em pó ? 
* P02101 - Que tipo de suco de caixinha/lata ou refresco em pó o(a) Sr(a) costuma tomar? (Ler as opções de resposta) 
* P01601 - Em quantos dias da semana o(a) Sr(a) costuma tomar suco de fruta natural (incluída a polpa de fruta congelada)? 
* P18. - Em quantos dias da semana o(a) Sr(a) costuma comer frutas?
* P19. - Em geral, quantas vezes por dia o(a) Sr(a) come frutas?
* P20b. Em quantos dia da semana o(a) Sr(a) costuma tomar refrigerante?
* P21b. Que tipo de refrigerante o(a) Sr(a) costuma tomar?
* P25a. - Em quantos dia da semana o(a) Sr(a) costuma comer alimentos doces como biscoito/bolacha recheado, chocolate, gelatina, balas e outros?
* P26b. - Em quantos dias da semana o(a) Sr(a) costuma substituir a refeição do almoço por lanches rápidos como sanduíches, salgados, pizzas, cachorro quente etc.?
* P027 - Com que frequência o(a) Sr(a) costuma consumir alguma bebida alcoólica?
* P02801 - Quantos dias por semana o(a) Sr(a) costuma consumir alguma bebida alcoólica? 
*  P029 - Em geral, no dia que o(a) Sr(a) bebe, quantas doses de bebida alcoólica o(a) Sr(a) consome? 
* P34. - Nos últimos doze meses, o(a) Sr(a) praticou algum tipo de exercício físico ou esporte?
* P35. - Quantos dias por semana o(a) Sr(a) costuma (costumava) praticar exercício físico ou esporte?
* P36. - Qual o exercício físico ou esporte que o(a) Sr(a) pratica(praticava) com mais frequência?
* P03702 - Em geral, no dia que o(a) Sr(a) pratica (praticava) exercício ou esporte, quanto tempo em minutos dura essa atividade?Minutos
* P50. - Atualmente, o(a) Sr(a) fuma algum produto do tabaco?
* P52. - E no passado, o(a) Sr(a) fumou algum produto do tabaco?
* P05401 - Em média, quanto fuma por dia ou por semana Cigarros industrializados
* P05404 - Em média, quanto fuma por dia ou por semana Cigarros de palha ou enrolados a mão? 
* P05407 - Em média, quanto fuma por dia ou por semana Cigarros de cravo ou de Bali? 
*  P05410 - Em média, quanto fuma por dia ou por semana Cachimbos (considere cachimbos cheios)? 
* P05413 - Em média, quanto fuma por dia ou por semana Charutos ou cigarrilhas?
* P05416 - Em média, quanto fuma por dia ou por semana Narguilé (sessões)? 
* P05419 - Em média, quanto fuma por dia ou por semana Outro
* P06701 - O(a) Sr(a) usa aparelhos eletrônicos com nicotina líquida ou folha de tabaco picado (cigarro eletrônico, narguilé eletrônico, cigarro aquecido ou outro dispositivo eletrônico para fumar ou vaporizar)? - (1, diaramente ; 2 menos que diaramente ; 3 Não, mas já usei)
* P68. - Com que frequência alguém fuma dentro do seu domicílio?
* Q74. - Algum médico já lhe deu o diagnóstico de asma (ou bronquite asmática)?
* W00201 - Altura - Primeira medida
* W00202- Altura – Segunda medida
* W00101 - Peso – Primeira medida
* W00102 - Peso – Segunda medida
* VDF004-  Faixa rendimento domiciliar per capita
* VDD004A - Nível de instrução mais elevado alcançado (pessoas de 5 anos ou mais de idade) padronizado para o Ensino Fundamental -  SISTEMA DE 9 ANOS


## Agrupamentos e Transformações

### **IMC - 1° (2 atributos)**

- Verificar se há no **modulo W**, caso haja fazer a média das 2 medidas.
- Se não houver: Verificar o **modulo P**.
- juntar os atributos de peso e Altura e classificar os IMC.

$$IMC = \frac{Peso}{Altura \times Altura}$$

### **Fumantes- 2° (4 atributos)**

- Há 3 tipos Fumantes Ativos, Passivos e Ex-fumantes.
    - Fumantes Ativos: P50.
        - Se a resposta for 1 classificar como diario.
        - Se for 2 classificar como fumante Ocasional.
        - Se for 3 **NÃO** é classificado como fumante ativo.
    - Fumantes Passivos: M10a e P68.
        - Se na M10a for 1 classificar como fumante passivo.
        - Se no P68 for 1,2,3,4 classificar como fumante passivo.
    - Ex-fumantes: P52.
        - Se for 1,2 classificar como ex fumante.

### **Atividades fisica - 3° (3 atributos)**

- Se a pessoa entrevistada realiza exercícios e mantem uma rotina, evita a obesidade.
- P34.
    - Se 1 classifica como ativa - Ruim -  se não inativa - Pessimo.
    - Se a resposta for 1 verificar quantos dias e se os exercicios são os mais recomendados (aerobicos): P35 e P36.
        - Verificar a quantidade, valor int- Otimo- ou 0 (1 ou menos por semana). - Bom
        - Verificar se é 1,2,4,9,11. - Excelente

### **Alimentação - 4° (9atributos)**

- No ambito da alimentação será verificado se a ingestão de nutrientes recomendados para alguem com asma (alimentação correta) e a ingestão de nutrintes não recomendados para alguem com asma (alimentação errada).

- Alimentação Correta:
    - P9a.  e 910a. - Verificação de legumes e verduras( alimentos ricos em vitaminas) e sua frequencia.
    - P18a. e P19a - Verificação de frutas( alimentos ricos em vitaminas) e sua frequencia.
    - P15. - Verificação de peixes (alimento rico em Omega-3)
- Alimentação Errada:
    - P20b. - ingestão de refrigerantes e volume semanal.
    - P21b. - ingestão do tipo refrigerantes, 1  ruim, 2 pessimo , 3muito ruim.
    - P25a. -  ingestão alta de açucar adicionado e volume semanal.
    - P26b. -  ingestão de alimentos ricos em gorduras saturadas (inflamatorias) e volume.
    

### **Condição de trabalho - 5° ( 2 atributos)**

- O entrevistado é exposto a condições que possam criar gatilhos a asma.
- AA24:
    - a.  - Entrevistado esteve contato com substancias que podem adentrar facilmente no seu sistema respirátorio causando reações , 1 sim , 2 não
    - c. - Entrevistado esteve contato com substancias que podem adentrar facilmente no seu sistema respirátorio causando reações , 1 sim , 2 não

### **Fatores Socioeconomicos - 7° (2 atributos)**
* Fatores socioeconomicos tem uma relação direta com a insegurança alimentar, sendo uma relação proporcional, logo quanto pior a condição socioeconomica mais insegurança alimentar o mesmo para o contrário.
- VDF003 - Rendimento domiciliar per capita 
- D9a. Qual foi o curso mais elevado que ___frequentou?

### **Faixa Etária - 6° (1 atributo)**

- Selecionar apenas entrevistados entre 30-60

### **Genero - 7° (1 atributo)**

- Seguir o questionário

### **Asmático - 8° (1 atributo)**

- Seguir o questionário


2153