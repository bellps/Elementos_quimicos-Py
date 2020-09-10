# Ache seu elemento!

Uma aplicação de console feita em python, com o objetivo de fazer pequenas consultas sobre elementos químicos.

<p align="center"><img src="https://i.imgur.com/TKHjwNK.png"></p>

## Módulos utilizados
- Requests
- GoogleTrans
- Json
- PrettyTable
- OS

## Agradecimentos
Esse estudo foi possível graças a [API](https://github.com/neelpatel05/periodic-table-api) gratuita disponibilizada pelo usuário neelpatel05, que possui todos os elementos da tabela periódica, junto com suas respectivas propriedades, organizados no formarto json.

## Como funciona
Após o usuário digitar a opção desejada e fornecer a informação, o Requests pega na API o elemento em questão, transforma em um dicionário (para facilitar a manipulação do dado) e o programa retorna algumas das caracteríscas do elemento. 
Como a API está inteira em inglês, utilizei o GoogleTrans para sempre traduzir o nome do elemento para tal língua (e também para mostrar em português as propriedades do elemento).

**Atualização #1:** como a API não traz diretamente a distribuição eletrônica dos elementos, construi um arquivo .json com a informação e esta é anexada ao dicionário de cada elemento durante a consulta.

**Atualização #2:** utilizei o módulo PrettyTable para imprimir os dados de forma mais organizada, e adicionei uma opção para ver informações adicionais de um elemento. Por isso, a aplicação não usa mais o arquivo .json citado na primeira atualização.

<p align="center"><img src="https://i.imgur.com/OX9iOql.png"></p>
