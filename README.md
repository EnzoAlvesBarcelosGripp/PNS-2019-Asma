# PNS 2019 - Análise de padrões de qualidade de vida em adultos (30-59 anos) com asma

1. Introdução
* Este projeto tem como objetivo realizar um estudo da base de dados da Pesquisa **Nacional de Saúde** (PNS) publicada em 2019, o tema é **Análise de padrões de qualidade de vida em adultos (30-59 anos) com asma**, com **enfoque** maior na **alimentação**.
---
2. Publico-alvo 
* O publico-alvo do projeto são as pessoas no intervalo de 30-59 anos. Este grupo se difere em 2:
    * Com diagnóstico médico de asma.
    * Sem diagnóstico médico de asma.
---
3. Objetivo
* O objetivo é conseguir distinguir padrões de qualidade de vida saudáveis e não saudáveis, seguindo as recomendações médicas para pessoas diagnósticadas com asma.
    1. Objetivos Especifícos
    *  
---
4. Base de Dados
* A base de dados escolhida é a PNS 2019, disponibilizada pelo Instituto Brasileiro de Geografia e Estatística (IBGE) e pela Fundação Oswaldo Cruz (Fiocruz).
---
5. Metodologia
* Os processos realizados no projeto segue abaixo:
    * Escolha criteriosa dos atributos.
    * Particionamento do dataset, seguindo a escolha dos atributos.
    * Agrupamento dos atributos.
    * Construção dos dicionário de dados.
    * 
* Obs: Variáveis que representam consequências diretas do diagnóstico de diabetes (por exemplo, orientações médicas recebidas após o diagnóstico) não são utilizadas na construção de modelos preditivos, de modo a evitar o vazamento de informação (target leakage). São priorizadas variáveis que representam exposição alimentar, comportamento e condições físicas dos indivíduos.
