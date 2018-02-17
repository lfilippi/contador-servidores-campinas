<b><h1>Monitor do Funcionalismo de Campinas</h1></b>

A partir da folha de pagamento disponibilizada mensalmente pela Prefeitura de Campinas, o programa, escrito em Python, possui duas funções nesta primeira versão. Monitorar o número de funcionários por secretaria ou cargo.

Inicialmente, estão disponíveis os dados de janeiro a dezembro de 2017. Porém, em próximas atualizações serão fornecidos períodos mais estendidos de dados para análise. 

As planilhas CSV utilizadas para obtenção das informações estão disponíveis no Portal da Trasparência da Prefeitura de Campinas. Todas passaram por um processo de limpeza para melhor interpretação dos códigos Python.

<b><h3>1. Monitor do número de servidores por secretaria</h3></b>

Contabiliza mês a mês o número de funcionários contratados por secretaria. Basta digitar a secretaria desejada com as primeiras letras em caixa alta ("Educação", "Direitos da Pessoa com Deficiência e Cidadania" etc) e o programa retorna os dados. 

<b><h3>2. Monitor do número de servidores por cargo</h3></b>

Contabiliza mês a mês o número de servidores contratados por cargo. Basta digitar o cargo a ser buscado todo em caixa alta ("GUARDA MUNICIPAL", "ASSISTENTE SOCIAL" etc) e o programa retorna os dados. 

<b><h3>3. Monitor do número de servidores por cargo</h3></b>

Contabiliza os valores pagos pela prefeitura aos funcionários. É possível fazer os cálculos para os tipos específicos de pagamentos. Para isso, a lista de todas as opções está abaixo. O número ao lado representa a posição da coluna na planilha, ou seja, para somar o Total Bruto, por exemplo, é preciso alterar o código para registro[16].

Verbas Fixas [5]
Cargo Comissão / Função Gratificada [6]
Produtividade [7]
Hora Extra [8]
Sucumbência [9]
Eventual [10]
Adic.Crg./ Local/Jorn. [11]
Salário Atraso [12]
Prêmio Férias [13]
Licença Prêmio [14]
13º Salário [15]
Total Bruto [16]
Deduções [17]
Bruto c/ Deduções [18].
