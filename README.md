# Códigos Livro Guia Definitivo de listas em Python

Este é o diretório GitHub com os exemploes e exercicios do Livro Guia Definitivo de listas em Python.

## Estrutura do Diretório

.
├── chapter01
│   ├── __init__.py
│   ├── linked_lists.py
│   └── list_basics.py
├── chapter02
│   ├── __init__.py
│   └── consult_modify_functions_lists.py
├── chapter03
│   ├── __init__.py
│   └── deep_shallow_copy.py
├── exercises
│   ├── __init__.py
│   ├── exercises_list.py
│   └── test_exercise.py
├── .gitignore
├── README.md
└── requirements.txt

- `chapter01/`: Contém os arquivos do primeiro capítulo.
  - `__init__.py`: Arquivo de inicialização do pacote.
  - `linked_lists.py`: Código de linked listas.
  - `list_basics.py`: Código de exemplo do primeiro capitulo.

- `chapter02/`: Contém os arquivos do segundo capítulo.
  - `__init__.py`: Arquivo de inicialização do pacote.
  - `consult_modify_functions_lists.py`: Código de exemplo do segundo capitulo.

- `chapter03/`: Contém os arquivos do terceiro capítulo.
  - `__init__.py`: Arquivo de inicialização do pacote.
  - `deep_shallow_copy.py`: Código de exemplo do terceiro capitulo.

- `exercises/`: Contém exercícios e testes.
  - `__init__.py`: Arquivo de inicialização do pacote de exercícios.
  - `exercises_list.py`: Arquivo com exercícios sobre listas.
  - `test_exercise.py`: Arquivo com testes para os exercícios.

- `README.md`: Este arquivo.
- `requirements.txt`: Lista de dependências do projeto.

## Configuração do Ambiente Virtual

Antes de configurar seu ambiente virtual clone este projeto, no diretorio do projeto siga o passoa passo abaixo
1. **Crie um ambiente virtual:**

   No terminal, navegue até o diretório do projeto e execute:

   ```bash
   python -m venv venv

## Configuração do Ambiente Virtual

1. **Crie um ambiente virtual:**

   Para criar um ambiente virtual, você pode usar o `venv` do Python. No terminal, navegue até o diretório do projeto e execute:

   ```bash
   python -m venv venv
   ```

   Isso criará uma nova pasta chamada `venv` que conterá o ambiente virtual.

2. **Ative o ambiente virtual:**

   - **No Windows:**
     ```cmd
     venv\Scripts\activate
     ```

   - **No macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

   Após a ativação, você verá o nome do ambiente virtual (`venv`) no prompt.

3. **Instale as dependências:**

   Com o ambiente virtual ativado, instale as dependências listadas em `requirements.txt` usando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

4**Execute os testes:**

   Acesse a pasta exercises
   ```bash
   cd exercises 
   ```
   Para executar os testes, use o comando `pytest` no terminal:

   ```bash
   pytest
   ```

   O `pytest` irá buscar todos os arquivos e funções de teste e executá-los, mostrando um relatório dos resultados.

## Exemplos de Comandos Úteis

- **Listar o conteúdo do diretório:** `ls` (Linux/macOS) ou `dir` (Windows)
- **Criar um ambiente virtual:** `python -m venv venv`
- **Ativar ambiente virtual:** `source venv/bin/activate` (macOS/Linux) ou `venv\Scripts\activate` (Windows)
- **Instalar dependências:** `pip install -r requirements.txt`
- **Executar testes:** `pytest`

Sinta-se à vontade para ajustar este `README.md` conforme as necessidades específicas do seu projeto!
