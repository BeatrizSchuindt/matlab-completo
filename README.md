# Compilador MATLAB - Projeto de Compiladores

Este repositório contém o projeto de um **compilador para uma linguagem baseada em MATLAB**, desenvolvido ao longo da disciplina de Compiladores.  
Cada arquivo `main` representa uma **fase específica do compilador**, e o **último `main` (da geração de código)** integra todas as análises anteriores (léxica, sintática e semântica) antes de produzir o código de saída.

---

## Sumário

- [Visão geral do projeto](#visão-geral-do-projeto)
- [Estrutura das fases (`main`)](#estrutura-das-fases-main)
  - [Análise Léxica](#1-análise-léxica---main_lexicopy)
  - [Análise Sintática](#2-análise-sintática---main_sintaticopy)
  - [Análise Semântica](#3-análise-semântica---main_semanticopy)
  - [Geração de Código (pipeline completo)](#4-geração-de-código---main_codigopy)
- [Instalação e ambiente virtual](#instalação-e-ambiente-virtual)
  - [Criando e ativando a *venv*](#criando-e-ativando-a-venv)
  - [Por que a *venv* é importante](#por-que-a-venv-é-importante)
- [Dependências do projeto](#dependências-do-projeto)
- [Instalação do Graphviz](#instalação-do-graphviz)
  - [Windows](#windows)
  - [Linux--ubuntu-debian)](#linux-ubuntu-debian)
- [Exemplos de uso com o arquivo `triangulos.m`](#exemplos-de-uso-com-o-arquivo-triangulosm)

---

## Visão geral do projeto

O projeto implementa um compilador em múltiplas fases para uma linguagem inspirada em MATLAB:

1. **Análise léxica** – quebra o código-fonte em *tokens*.
2. **Análise sintática** – verifica se a sequência de tokens respeita a gramática.
3. **Análise semântica** – checa tipos, declarações de variáveis, uso correto de identificadores, etc.
4. **Geração de código** – gera código intermediário ou código alvo (por exemplo, Python) a partir da árvore sintática/AST já validada.

Cada uma dessas etapas foi implementada e testada em um `main` separado ao longo do desenvolvimento.  
Ao final, o `main` da **geração de código** integra todas essas fases em um pipeline completo.

---

## Estrutura das fases (`main`)

Os nomes abaixo são **sugestões**. Substitua pelos nomes reais dos seus arquivos.

### 1. Análise Léxica - `main.py`

- **Objetivo:**  
  Executar apenas a análise léxica do código-fonte, listando os tokens e identificando possíveis erros léxicos.

- **Uso sugerido:**
  ```bash
  python main.py exemplos/triangulos.m
  ```

- **Entrada:**  
  Arquivo-fonte em linguagem MATLAB (ex.: `triangulos.m`).

- **Saída típica:**
  - Lista de tokens (identificadores, palavras reservadas, números, operadores, etc.).
  - Mensagens de erro léxico, se houver.

---

### 2. Análise Sintática - `main.py`

- **Objetivo:**  
  Realizar a análise sintática a partir dos tokens gerados, verificando se o programa está conforme a gramática definida.

- **Uso sugerido:**
  ```bash
  python main.py exemplos/triangulos.m
  ```

- **Entrada:**  
  Arquivo-fonte (ex.: `triangulos.m`).

- **Saída típica:**
  - Mensagem indicando se a análise sintática foi bem-sucedida.
  - Arquivo `.dot` com a árvore sintática, se configurado para isso (ver seção de Graphviz).

---

### 3. Análise Semântica - `main_semantic.py`

- **Objetivo:**  
  Verificar regras semânticas do programa, como:
  - Variáveis usadas sem declaração.
  - Tipos incompatíveis em operações.
  - Atribuições inválidas.

- **Uso sugerido:**
  ```bash
  python main_semantic.py exemplos/triangulos.m
  ```

- **Saída típica:**
  - Mensagens de erro semântico (se houver).
  - Confirmação de que o programa é semanticamente válido.

---

### 4. Geração de Código - `main_codegen.py`

Este é o **main final** do projeto.

- **Objetivo:**  
  Integrar:
  1. Análise léxica  
  2. Análise sintática  
  3. Análise semântica  
  4. Geração de código

  em um único fluxo completo.

- **Uso sugerido:**
  ```bash
  python main_codegen.py exemplos/triangulos.m
  ```

- **Comportamento esperado:**
  - Em caso de erro léxico, sintático ou semântico, o processo é interrompido com mensagem clara.
  - Em caso de sucesso, o código alvo é gerado (por exemplo, `triangulos_out.py`).

---

## Instalação e ambiente virtual

Recomenda-se fortemente o uso de um **ambiente virtual (venv)** para isolar as dependências do projeto.

### Criando e ativando a `venv`

No diretório raiz do projeto:

#### Windows (PowerShell ou CMD)

```bash
python -m venv .venv
.\.venv\Scripts/activate
```

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### Por que a `venv` é importante?

- Isola as bibliotecas usadas neste projeto das demais instaladas na máquina.
- Evita conflitos de versões entre diferentes projetos Python.

---

## Dependências do projeto

Com a `venv` ativada, instale as dependências:

```bash
pip install antlr4-python3-runtime graphviz
```

---

## Instalação do Graphviz

O Graphviz é usado para gerar imagens das árvores sintáticas (a partir de arquivos `.dot`).

### Windows

1. Acesse o site oficial do Graphviz.
2. Baixe o instalador adequado para sua versão do Windows.
3. Instale o Graphviz e **marque a opção para adicionar ao PATH** (ou faça isso manualmente depois).
4. Após a instalação, teste no terminal:

   ```bash
   dot -V
   ```

   Se aparecer a versão do Graphviz, está tudo certo.

### Linux (Ubuntu / Debian)

```bash
sudo apt-get update
sudo apt-get install graphviz
dot -V
```


## Exemplos de uso com o arquivo `triangulos.m`

Supondo que você esteja na raiz do projeto, com a `venv` ativada e todas as dependências instaladas:

```bash
# Análise léxica & sintática + AST em png/svg
python main.py exemplos/triangulos.m

# Análise semântica
python main_semantic.py exemplos/triangulos.m

# Pipeline completo + geração de código
python main_codegen.py exemplos/triangulos.m
```

Se tudo estiver correto, será gerado um arquivo de saída (por exemplo `triangulos_out.py`) que poderá ser executado normalmente:

```bash
python exemplos/triangulos_out.py
```
