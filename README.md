# Sumário
- # [Apresentação](#análise-de-uma-série-de-tv)
  - ## [Resumo das funcionalidades](#resumo_funcionalidades)
- # [Top 250 TV Shows (IMDb)](top-250-tv-shows-imdb)
  - ## [Análise de alguns gráficos peculiares](análise-de-alguns-gráficos-peculiares)
    - ## [The Simpsons (1989 - )]()
    - ## [Top Gear (2002 - 2020)]()
    - ## [Doctor Who (2005 - 2012)]()
    - ## [Dexter (2006 - 2013), House of Cards (2013 - 2018) & Game of Thrones (2011 - 2019)]()
    - ## [Breaking Bad (2008 - 2013)]()
- # [Guia de instalação e de uso](#guia)
  - ## [Pré-requesitos e informações](#pre_requisitos)
    - ### [1. Python](#instalar_python)
    - ### [2. ID da série](#codigo_da_serie)
  - ## [Passo a passo para baixar e utilizar o programa](#como-baixar-e-utilizar-o-programa)
    - ### [1. Baixe a pasta scripts.zip](#baixar_pasta_script)
    - ### [2. Extraia os arquivos](#extrair_pasta_script)
    - ### [3. Execute o script interface.py](#executar_interface)
    - ### [4. Clique no botão Verificar bibliotecas](#clicar_botao_verificar_bibliotecas)
    - ### [5. Clique no botão Baixar dados trimestrais](#clicar_botao_baixar_dados_trimestrais)
    - ### [6. Clique no botão Baixar DFPs](#clicar_botao_baixar_dfps)
    - ### [7. Digite o código CVM da empresa e o ano da DFP](#inputs)
    - ### [8. Clique no botão Gerar Excel](#clicar_botao_gerar_excel)
   
------------------------

# Análise de uma série de TV

## Plote um gráfico de dispersão das avaliações dos epísodios de uma série

Este projeto em Python apresenta uma maneira simples e rápida de analisar uma série listada no site [IMDb](https://www.imdb.com/). 
- O IMDb (Internet Movie Database) é uma base de dados online com informações sobre cinema, TV, música e games.
  
Com apenas alguns inputs, o usuário pode obter um gráfico de dispersão que detalha a relação entre episódios e avaliações.

###### Interface do programa
<img align="center" width='33%' src="https://i.postimg.cc/jqHYTSRK/image.png">

<a name="resumo_funcionalidades"></a>
## Resumo das funcionalidades
- **Interface intuitiva**: A interface do programa é simples e acessível.
   - O programa apenas necessita do nome ou do ID da série para gerar um gráfico.

- **Análise gráfica**: Será plotado um gráfico de dispersão que oferece detalhes suficientes para uma primeira análise.

# Top 250 TV Shows IMDb
Foram gerados gráficos para os [*Top 250 TV Shows*](https://m.imdb.com/chart/toptv/?ref_=nv_tvv_250) do site.
###### Alguns *plots* do Top 250 TV Shows, sem ordem específica
<p align="center" width="100%">
    <img width="25%" src="https://i.postimg.cc/8cX0452f/R1-Breaking-Bad.png"> 
    <img width="25%" src="https://i.postimg.cc/brw51bBj/R2-Planet-Earth-II.png"> 
    <img width="25%" src="https://i.postimg.cc/43GBzVYF/R18-The-World-at-War.png">
    <img width="25%" src="https://i.postimg.cc/cLymSwB4/R23-The-Twilight-Zone.png">
    <img width="25%" src="https://i.postimg.cc/Xqr8VgPX/R20-Attack-on-Titan.png">
    <img width="25%" src="https://i.postimg.cc/tTM3mxgb/R28-TVF-Pitchers.png">
    <img width="25%" src="https://i.postimg.cc/Kc0wxq1c/R3-Band-of-Brothers.png">
    <img width="25%" src="https://i.postimg.cc/mgCmz8gH/R15-The-Sopranos.png">
    <img width="25%" src="https://i.postimg.cc/BZjkZ5Hx/R33-Better-Call-Saul.png">
    <img width="25%" src="https://i.postimg.cc/7ZnQtKry/R32-The-Office-USA.png">
    <img width="25%" src="https://i.postimg.cc/s2PH8wFr/R7_-_The_Wire.png">
    <img width="25%" src="https://i.postimg.cc/HWvZfrNV/R14-Game-of-Thrones.png">
    <img width="25%" src="https://i.postimg.cc/rFtJ3QWP/R24-Fullmetal-Alchemist-Brotherhood.png">
    <img width="25%" src="https://i.postimg.cc/kMHsTkVS/R22-Rick-and-Morty.png">
    <img width="25%" src="https://i.postimg.cc/MGYttHRZ/R17-Critical-Role.png">
</p>

Você pode acessar toda a lista de gráficos clicando [neste link](https://drive.google.com/drive/folders/1Kz9c25IGAVdHTS8WLWV7Xjy7M59EencQ).

## A seguir estão algumas representações gráficas interessantes que foram geradas:

### The Simpsons (1989 - ) 
<img width="80%" src="https://i.postimg.cc/hGRL7dCZ/R104-The-Simpsons.png">

[The Simpsons](https://www.imdb.com/title/tt0096697/) é uma dos desenhos mais antigos da televisão, além de ser uma das séries com maior número de episódios e temporadas. O gráfico revela a decadência da qualidade do programa. Entretanto, ao levar em consideração que já se passaram 35 anos desde o lançamento do primeiro episódio, podemos dizer que a animação como um todo teve um ótimo desempenho geral.

### Top Gear (2002 - 2020)
<img width="80%" src="https://i.postimg.cc/mgMGLv1f/R133-Top-Gear.png">

Pelo gráfico, é possível notar que [Top Gear](https://www.imdb.com/title/tt1628033/) esteve em ascendência contínua por surpreendentes 22 temporadas. Já a partir da 23ª Season, houve uma queda brutal na qualidade da série, o que foi parcialmente recuperado nas temporadas seguintes.

### Doctor Who (2005 - 2012)
<img width="80%" src="https://i.postimg.cc/GpqgdKKn/R156-Doctor-Who.png">

[Doctor Who](https://www.imdb.com/title/tt0436992/) apresenta uma peculiaridade intrigante: por mais que as avaliações dos seus episódios sejam um tanto quanto inconsistentes, o rating médio, tanto da maioria das temporadas como o geral (8,6) é muito bom.

### Dexter (2006 - 2013), House of Cards (2013 - 2018) & Game of Thrones (2011 - 2019)
<img width="80%" src="https://i.postimg.cc/sx9wHJvL/R155-Dexter.png">
<img width="80%" src="https://i.postimg.cc/BnwNzbnJ/R169-House-of-Cards.png">
<img width="80%" src="https://i.postimg.cc/HWvZfrNV/R14-Game-of-Thrones.png">

[Dexter](https://www.imdb.com/title/tt0773262/), [House of Cards](https://www.imdb.com/title/tt1856010/) e [Game of Thrones](https://www.imdb.com/title/tt0944947/) são exemplos de séries que, de acordo com seus telespectadores, poderiam ter tido finais muito mais satisfatórios e congruentes.

### Breaking Bad (2008 - 2013) 
<img width="80%" src="https://i.postimg.cc/8cX0452f/R1-Breaking-Bad.png">

Em contrapartida, [Breaking Bad](https://www.imdb.com/title/tt0903747/) apresenta um desempenho fenomenal, sendo a série com melhor avaliação do site. Além de manter uma média ascendente incrível, teve um final extremamente satisfatório, com direito a episódios com avaliações de 9.9 ([S5 E16](https://www.imdb.com/title/tt2301455/?ref_=ttep_ep16)) e 10 ([S5 E14](https://www.imdb.com/title/tt2301451/?ref_=ttep_ep14)) na temporada 5, a última temporada do programa. 

------------------------

<a name="guia"></a>
# Guia de instalação e de uso

<a name="pre_requisitos"></a>
## Pré-requisitos e informações


<a name="instalar_python"></a>
### 1. Instale o Python em seu computador

- É **necessário** que o usuário tenha Python instalado em sua máquina

- Acesse [python.org](https://www.python.org/downloads/) e baixe Python para seu sistema operacional

> [!WARNING]
> ***Certifique-se de marcar a opção Add python.exe to PATH!***
  
###### Instalador do Python
<img align="center" width='65%' src="https://i.postimg.cc/wxkf5Tp4/python-installer.png">

<a name="codigo_da_serie"></a>
### 2. ID da série
> [!IMPORTANT]
> Caso exista séries com mesmo nome, digite o ID ao invés do título
- O ID pode ser encontrado na URL da página da série no site, como mostra o exemplo abaixo:

###### O ID da série sempre será os números que sucedem o 'tt'; no caso de Breaking Bad, o ID da série é 0903747
<img align="center" width='65%' src="https://i.postimg.cc/BQGhPppD/id.png">

###### URL: https://www.imdb.com/title/tt0903747/

------------------------

## Como baixar e utilizar o programa

<a name="baixar_pasta_script"></a>
### 1. Baixe a pasta [filtro_cvm.zip](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm.zip)
------------------------

<a name="extrair_pasta_script"></a>
### 2. Extraia os arquivos

> [!IMPORTANT]
> Para garantir o funcionamento do programa, mantenha todos os arquivos extraídos em um único diretório.

###### Extração de arquivos zip
<img align="center" width='50%' src="https://i.postimg.cc/zG6jjFMv/extract-image.png">

------------------------

<a name="executar_interface"></a>
### 3. Execute o script [interface.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/interface.py)

> [!TIP]
> Segurando a tecla ALT, você pode arrastar o arquivo interface.py para outro diretório para criar um atalho.

###### Interface do programa
<img align="center" width='80%' src="https://i.postimg.cc/4xk3sNB8/user-interface.png">

------------------------

<a name="clicar_botao_verificar_bibliotecas"></a>
### 4. Clique no botão <img align="center" width="33%" src="https://i.postimg.cc/YSy0cNVF/verificar-bibliotecas.png"> 

- Este botão irá executar o script [setup.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/setup.py)
- Será feito o download de todos os módulos necessários para o funcionamento do programa
------------------------

<a name="clicar_botao_baixar_dados_trimestrais"></a>
### 5. Clique no botão <img align="center" width='33%' src="https://i.postimg.cc/7PJGkcqZ/baixar-dados-trimestrais.png">

- Este botão irá executar o script [donwload_dados_itr.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/download_dados_itr.py)
- Será realizado o download das [ITRs (Informações Trimestrais) (2011 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm_itr**
------------------------

<a name="clicar_botao_baixar_dfps"></a>
### 6. Clique no botão <img align='center' width='33%' src="https://i.postimg.cc/7Z9b9rnm/baixar-dfps.png">

- Este botão irá executar o script [donwload_dados_dfp.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/download_dados_dfp.py)
- Será realizado o download dos [DFPs (Demonstrativo Financeiro Padronizado) (2010 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm_dfp**
------------------------

<a name="inputs"></a>
### 7. Digite o código CVM da empresa e o ano da DFP
> [!IMPORTANT]
> Acesse o site para encontrar os códigos CVM das empresas
- Os códigos CVM das empresas podem ser encontrados [aqui](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

###### Empresa: ALPARGATAS S.A. | Ano: 2023
<img align="center" width='80%' src="https://i.postimg.cc/j2WhCnFn/user-interface-inputs.png">

------------------------

<a name="clicar_botao_gerar_excel"></a>
### 8. Clique no botão <img align='center' width='20%' src='https://i.postimg.cc/W44zfY9j/generate-excel.png'>
- Este botão irá executar o script [filtro.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/filtro.py)
- Um [arquivo Excel](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/ALPARGATAS%20S.A._2023.xlsx) será gerado com as especificações dadas
  
  - Link para acessar a planilha: [https://docs.google.com](https://docs.google.com/spreadsheets/d/18aJ9YykdlPfqjOoxF577g4grvyuqFuht/edit?usp=sharing&ouid=103571908927816967898&rtpof=true&sd=true)
