# App Preço de Ações

Este é um aplicativo desenvolvido com Streamlit para visualizar a evolução do preço das ações ao longo dos anos. O aplicativo permite que você selecione várias ações, ajustar o período de visualização e analisar o desempenho dos ativos e da carteira.

### Funcionalidades

<ul>
    <li>Visualização de Dados: Gráfico interativo com a evolução dos preços das ações.</li>
    <li>Filtros de Ações: Selecionar quais ações visualizar. </li>
    <li>Intervalos de Datas: Ajustar o período de consulta.</li>
    <li>Performance dos Ativos: Calcula e exibe a performance dos ativos no período selecionado.</li>
    <li>Desempenho da carteira: Avalia a partir do período definido o resultado das ações selecionadas. </li>
</ul>

### Tecnologias Utilizadas

<ul>
    <li><strong>Streamlit:</strong> Framework para criar aplicativos web interativos.</li>
    <li><strong>Pandas:</strong> Biblioteca para manipulação e análise de dados.</li>
    <li><strong>yfinance:</strong> Biblioteca para acessar dados financeiros de ações.</li>
</ul>

### Requisitos

Certifique-se de ter o Python e as bibliotecas necessárias instaladas. Você pode instalar as dependências usando o arquivo requirements.txt.

### Instalação

<ol>
    <li>Clone o repositório</li>
    <li>Crie um ambiente virtual</li>
    <li>Ative o ambiente virtual
    <ul>
        <li>No Windows</li>
        <li>No macOS/Linux</li>
    </ul>
    </li>
    <li>Instale as dependências</li>
    ``` pip install -r requirements.txt ```
    <li>Prepare o Arquivo CSV</li>
</ol>

### Uso

<ol>
    <li>Execute o Aplicativo</li>
    ```streamlit run main.py```
    <li>Acesse o Aplicativo</li>
</ol>

### Estrutura do Projeto

<ul>
    <li><strong>main.py:</strong> Código principal do aplicativo Streamlit.
    </li>
    <li><strong>IBOV.csv:</strong> Arquivo CSV contendo os dados das ações.</li>
    <li><strong>requirements.txt:</strong> Lista de dependências do projeto.</li>
</ul>

### Contribuição

Se você deseja contribuir para o projeto, siga estas etapas:

<ol>
    <li>Faça um Fork do repositório.</li>
    <li>Crie uma Branch para suas modificações</li>
    <li>Faça o Commit das suas alterações</li>
    <li>Faça o Push para sua branch</li>
    <li>Crie um Pull Request no GitHub.</li>
</ol>