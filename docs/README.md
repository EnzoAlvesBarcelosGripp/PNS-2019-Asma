## Contextualização
* A Pesquisa Nacional de Saúde (PNS), realizada pelo IBGE em parceria com o Ministério da Saúde, é o mais completo inquérito domiciliar do Brasil, com edições em 2013 e 2019. Seu propósito é investigar as condições de vida e saúde da população, servindo de base para a formulação de políticas públicas.
* Dentro do ambito da saúde é questionado desde alimentação a exeriência de atendimentos do setor da saúde. O objetivo geral deste projeto é analisar e comparar padrões de vida, hábitos alimentares e experiências no sistema de saúde entre indivíduos diagnosticados com Asma e indivíduos sem doenças crônicas, utilizando a base de dados PNS 2019, a fim de identificar determinantes de saúde e propor pontos de melhoria no manejo da condição.
## Escolha dos Atributos
* A seguir estão os atributos escolhidos e suas motivações:
    * C6. Gênero - Escolhido devido a importância de distinguir o entrevistado entre Homen ou Mulher.
    * C8. - Idade - Filtro para a faixa etária do projeto (30-59).
    * D9a. Qual foi o curso mais elevado que ___frequentou? - escolaridade, importante fator socioeconomico.
    * P10a. - Em geral, o(a) Sr(a) costuma comer esse tipo de verdura ou legume: - Verificar hábito alimentícios, as verduras e legumes geralmente comtém as vitaminas C,D,E importantes para o controle da asma.
    * P9a. - Em quantos dias da semana, o(a) Sr(a) costuma comer pelo menos um tipo de verdura ou legume (sem contar batata, mandioca, cará ou inhame) como alface, tomate, couve, cenoura, chuchu, berinjela, abobrinha? - Verificar a consistência do hábito.
    * P15. - Em quantos dias da semana, o(a) Sr(a) costuma comer peixe? - Verificar consistência de hábito alimentício, peixes são ricos em Omêga-3, que é um nutriente anti-flamatório
    * P18. - Em quantos dias da semana o(a) Sr(a) costuma comer frutas? - Verificar consistência de hábito alimentícios, as frutas geralmente comtém as vitaminas C,D,E importantes para o controle da asma.
    * P19. - Em geral, quantas vezes por dia o(a) Sr(a) come frutas? - Verificar consistência de hábito alimentícios
    * P20b. Em quantos dia da semana o(a) Sr(a) costuma tomar refrigerante? - Verificar consistência de hábito alimentício, o alto teor de açúcar, frutose e conservantes promovem inflamações em vias aéreas.
    * P21b. Que tipo de refrigerante o(a0 Sr(a) costuma tomar? - Verificação de possível agravante, refrigerantes Diet/ligth/zero são considerados ruins para a saúde de alguém asmático, mas não tanto qunato refrigerantes normais.
    * P25a. - Em quantos dia da semana o(a) Sr(a) costuma comer alimentos doces como biscoito/bolacha recheado, chocolate, gelatina, balas e outros? - Verificar consistência de hábito alimentício, o alto teor de açúcar promove inflamações em vias aéreas.
    * P26b. - Em quantos dias da semana o(a) Sr(a) costuma substituir a refeição do almoço por lanches rápidos como sanduíches, salgados, pizzas, cachorro quente etc.? - Verificar consistência de hábito alimentício, alimentos ultraprocessados contém gorduras saturadas,trans e alto teor de sódio promovendo processos inflamatórios direto dos brônquios e nos pulmões.
    * P34. - Nos últimos doze meses, o(a) Sr(a) praticou algum tipo de exercício físico ou esporte? - Verificação de rotina de saúde, a rotina de exercícios fisícos evitam a obesidade, que é um agravante da asma.
    * P35. - Quantos dias por semana o(a) Sr(a) costuma (costumava) praticar exercício físico ou esporte? - Verificação de consistência de rotina de saúde
    * P36. - Qual o exercício físico ou esporte que o(a) Sr(a) pratica(praticava) com mais frequência? - Verificação de exercícios aeróbicos altamente recomendados para asmáticos (Caminhada,Caminhada em esteira, Corrida em esteira,Natação,Hidroginástica  Bicicleta ou bicicleta ergométrica).
    * P50. - Atualmente, o(a) Sr(a) fuma algum produto do tabaco? - Verificação de tabagismo ativo, a inalação de tabaco é extremamente perigoso para um asmático, já que fácilmente pode gerar irritações ou piorar a eficiência pulmonar.
    * P52. - E no passado, o(a) Sr(a) fumou algum produto do tabaco? - P050 (Ex fumante) - Verificação de ex-fumantes.
    * P68. - Com que frequência alguém fuma dentro do seu domicílio? - Verificação de tabagismo passivo.
    * Q74. - Algum médico já lhe deu o diagnóstico de asma (ou bronquite asmática)? - Necessária para distinguir pessoas asmáticas de não asmáticas.
    * Altura - Primeira medida  e Altura – Segunda medida --> Caso haja usadas no lugar das medidas do modulo P.
    * Peso – Primeira medida e Peso – Segunda medida --> Caso haja usadas no lugar das medidas do modulo P.
    * VDF003 - Rendimento domiciliar per capita - importante fator socioeconomico.
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