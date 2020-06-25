# Ache seu elemento!

Uma aplicação de console feita em python, com o objetivo de fazer pequenas consultas sobre elementos químicos.

![Amostra](https://i.imgur.com/TKHjwNK.png)

## Módulos utilizados
- Unicodedata
- Requests
- GoogleTrans

## Agradecimentos
Esse estudo foi possível graças a [API](https://github.com/neelpatel05/periodic-table-api) gratuita disponibilizada pelo usuário neelpatel05, que possui todos os elementos da tabela periódica, junto com suas respectivas propriedades, organizados no formarto json.

## Como funciona
Após o usuário digitar a opção desejada e fornecer a informação, o Requests pega na API o elemento em questão, transforma em um dicionário (para facilitar a manipulação do dado) e o programa retorna algumas das caracteríscas do elemento. 
Como a API está inteira em inglês, utilizei o GoogleTrans para sempre traduzir o nome do elemento para tal língua (e também para mostrar em português as propriedades do elemento).

