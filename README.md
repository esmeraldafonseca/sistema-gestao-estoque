# Sistema de Gestão de Estoque (SGE)

Aplicação desktop desenvolvida em Python, com interface gráfica em Flet e base de dados SQLite, para gestão de produtos, fornecedores e controlo de stock. Inclui um dashboard com gráficos gerados em matplotlib.

## Funcionalidades

- **Cadastro de produtos** — nome, preço, quantidade e fornecedor associado
- **Controlo de stock** — entrada e saída de produtos
- **Gestão de fornecedores**
- **Dashboard** com visualização de dados:
  - Produtos com menor stock (gráfico de barras)
  - Distribuição de produtos por fornecedor (gráfico circular)

## Tecnologias

- **Python 3.12+**
- **Flet** — framework de interface gráfica
- **SQLite** — base de dados (via `sqlite3`, biblioteca nativa do Python)
- **Matplotlib** — geração de gráficos no dashboard

## Estrutura do projeto

```
SGE_/
├── src/
│   ├── app/
│   │   ├── models/
│   │   │   └── database.py        # conexão e criação das tabelas
│   │   └── views/
│   │       ├── home_views.py
│   │       ├── stock_views.py
│   │       ├── product_views.py
│   │       └── dashboard_views.py
│   └── main.py
├── pyproject.toml
└── README.md
```

## Base de dados

Ao correr a aplicação pela primeira vez, as tabelas `usuarios`, `produtos` e `fornecedores` são criadas automaticamente pela função `create_table()`, incluindo a relação entre produtos e fornecedores (`fornecedor_id`). Não é necessário nenhum passo manual de configuração da base de dados.

## Como correr o projeto

Este projeto usa [`uv`](https://docs.astral.sh/uv/) para gerir o ambiente e as dependências, definidas no `pyproject.toml`.

1. **Clonar o repositório**
```bash
git clone https://github.com/esmeraldafonseca/inventory-management-system.git
cd inventory-management-system
```

2. **Instalar o `uv`** (se ainda não o tiveres)
```bash
pip install uv
```

3. **Instalar as dependências**
```bash
uv sync
```

4. **Correr a aplicação**
```bash
uv run flet run
```

> Nota: requer Python 3.10 ou superior.


## Autora

Esmeralda Fonseca
