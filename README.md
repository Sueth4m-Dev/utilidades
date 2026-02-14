**PT-BR**

🛠️ Python Utilities Library
Uma biblioteca modular de funções utilitárias desenvolvida em Python para otimizar a criação de aplicações de terminal (CLI). Este projeto centraliza lógicas recorrentes de interface, manipulação de dados e validação de entradas, promovendo a reutilização de código e uma arquitetura limpa.

🚀 Funcionalidades
A biblioteca é organizada por núcleos de responsabilidade:

📑 Interface e UX (User Experience)
Menus Dinâmicos: Geração automática de listas numeradas e seleção de itens.

Feedback Visual: Uso de cores ANSI para destacar erros (vermelho), sucessos (verde) e informações (azul/amarelo).

Elementos Visuais: Barra de progresso, efeito de digitação (typewriter) e cabeçalhos formatados.

💾 Persistência de Dados
SQL Tools: Funções para simplificar operações em bancos SQLite (execute para comandos de escrita e query para leitura).

JSON Tools: Métodos para salvar e carregar dados em arquivos JSON com suporte a UTF-8.

🛡️ Validação de Entradas
Tratamento de Exceções: Funções para leitura de int e float que impedem o crash do programa por entradas inválidas.

Filtros de Texto: Validação de comprimento de strings e tipos de caracteres para nomes ou placas.

🎲 Utilitários Adicionais
Sistema de Logs: Registro de eventos em arquivo .log com carimbo de tempo (timestamp).

Lógica Aleatória: Funções para sorteios de listas, chances percentuais e simulação de dados.

💻 Exemplo de Uso
Python
import Utilities as ut

# Entrada de dados com validação de intervalo
idade = ut.read_int("Digite sua idade: ", min_val=0, max_val=100)

# Exibição de cabeçalho estilizado
ut.draw_header("SISTEMA DE GESTÃO", symbol="-", width=40)

# Barra de progresso visual
ut.progress_bar(75, 100, title="Processando")


**ENGLISH**

🛠️ Python Utilities Library
A modular library of utility functions developed in Python to streamline the creation of command-line interface (CLI) applications. This project centralizes recurring interface logic, data manipulation, and input validation, promoting code reuse and clean architecture.

🚀 Key Features
The library is organized by core responsibilities:

📑 Interface & UX
Dynamic Menus: Automatic generation of numbered lists and item selection.

Visual Feedback: ANSI colors to highlight errors (red), success (green), and info (blue/yellow).

UI Elements: Progress bars, typewriter effects, and formatted headers.

💾 Data Persistence
SQL Tools: Helper functions for SQLite operations (execute for write commands and query for data retrieval).

JSON Tools: Methods for saving and loading data in JSON files with full UTF-8 support.

🛡️ Input Validation
Exception Handling: Functions for reading int and float that prevent program crashes due to invalid user input.

Text Filters: String length and character type validation for names or identifiers.

🎲 Additional Utilities
Logging System: Event recording in a .log file with automatic timestamps.

Random Logic: Functions for list selection, percentage-based chances, and dice simulation.

💻 Usage Example
Python
import Utilities as ut

# Input with range validation
age = ut.read_int("Enter your age: ", min_val=0, max_val=100)

# Styled header display
ut.draw_header("MANAGEMENT SYSTEM", symbol="-", width=40)

# Visual progress bar
ut.progress_bar(75, 100, title="Processing")
