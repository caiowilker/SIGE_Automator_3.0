# SIGE Automator 3.0

Projeto de automação em Python desenvolvido para auxiliar no cadastro de alunos em um sistema de gestão escolar (SIGE), reduzindo tarefas repetitivas e erros manuais.


## Objetivo do projeto

- Automatizar o processo de cadastro de alunos
- Reduzir trabalho manual e retrabalho
- Diminuir falhas humanas em tarefas repetitivas
- Aplicar Python em um cenário real de automação

```

## Estrutura do projeto

SIGE_Automator_3.0/
├── automator/
│ ├── base_automator.py
│ ├── sige_automator.py
│ └── selectors.json
├── data/
│ ├── data_manager.py
│ ├── word_importer.py
│ └── db/
├── interface/
│ └── app.py
├── utils/
│ ├── validators.py
│ ├── formatters.py
│ └── sustainability.py
├── main.py
├── requirements.txt
└── README.md
```

## Tecnologias utilizadas

- Python
- Automação de processos
- Estrutura modular

### Organização dos módulos

- **automator**: contém a lógica principal da automação e a implementação específica do fluxo do SIGE.
- **data**: responsável pelo gerenciamento e importação dos dados utilizados durante o processo.
- **interface**: camada simples de interação com o usuário para iniciar a automação.
- **utils**: funções auxiliares para validação, formatação e reaproveitamento de código.


## Funcionalidades

- Automação do cadastro de alunos no sistema SIGE
- Leitura e tratamento de dados externos
- Validação de informações antes da execução
- Organização do fluxo para reduzir falhas manuais


## Como executar

1. Clonar o repositório
2. Instalar as dependências listadas em requirements.txt
3. Executar o arquivo main.py


