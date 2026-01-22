# SIGE Automator 3.0

Projeto de **automação em Python** desenvolvido com o objetivo de auxiliar no **cadastro de alunos em um sistema de gestão escolar (SIGE)**, reduzindo tarefas repetitivas e minimizando erros manuais.

O projeto foi construído a partir de uma necessidade prática, com foco em organização, clareza de fluxo e separação de responsabilidades.

---

## 🎯 Objetivo do projeto
- Automatizar o processo de cadastro de alunos
- Reduzir trabalho manual e retrabalho
- Diminuir falhas humanas em tarefas repetitivas
- Aplicar conceitos de automação e organização de código em Python

---

## 🗂️ Estrutura do projeto

SIGE_Automator_3.0/
├── automator/
│ ├── base_automator.py # Classe base e comportamentos comuns da automação
│ ├── sige_automator.py # Implementação específica do fluxo SIGE
│ └── selectors.json # Mapeamento de seletores utilizados na automação
│
├── data/
│ ├── data_manager.py # Gerenciamento e leitura dos dados utilizados
│ ├── word_importer.py # Importação de dados a partir de arquivos Word
│ └── db/ # Estrutura para armazenamento de dados
│
├── interface/
│ └── app.py # Camada de interface para interação com o usuário
│
├── utils/
│ ├── validators.py # Validações de dados
│ ├── formatters.py # Padronização e formatação de informações
│ └── sustainability.py # Funções auxiliares para reaproveitamento de lógica
│
├── main.py # Ponto de entrada da aplicação
├── requirements.txt # Dependências do projeto
└── README.md


---

## 🛠️ Tecnologias utilizadas
- Python
- Automação de processos
- Estrutura modular
- Organização orientada à manutenção

---

## ⚙️ Funcionalidades
- Automação do fluxo de cadastro de alunos no sistema SIGE
- Importação e tratamento de dados externos
- Validação e formatação de informações antes da execução
- Separação clara entre lógica de automação, dados e interface

---

## ▶️ Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/caiowilker/SIGE_Automator_3.0.git
Acesse a pasta do projeto:

cd SIGE_Automator_3.0


Instale as dependências:

pip install -r requirements.txt


Execute a aplicação:

python main.py

📚 Aprendizados

Estruturação de projetos Python de forma modular

Automação aplicada a processos reais

Organização de código visando manutenção e clareza

Importância da separação de responsabilidades
