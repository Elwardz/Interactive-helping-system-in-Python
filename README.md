# PyHELP - Sistema de Ajuda Interativo em Python

PyHELP é um sistema interativo de ajuda que permite aos usuários consultar a documentação de funções ou bibliotecas do Python diretamente no terminal. Ele utiliza a função embutida `help()` do Python e oferece uma interface visual amigável, destacada por mensagens coloridas, para facilitar a navegação e o aprendizado.

---

## 🎯 **Funcionalidades**

1. **Consulta de Documentação**:
   - Exibe o manual de qualquer função ou biblioteca válida do Python.
   - Oferece uma mensagem de erro amigável caso o comando informado não seja válido.

2. **Interface Visual com Cores**:
   - Utiliza sequências ANSI para formatar mensagens no terminal com cores:
     - **Vermelho**: Mensagens de erro.
     - **Verde**: Títulos principais.
     - **Azul**: Mensagens intermediárias.
     - **Branco**: Conteúdo do manual.

3. **Mensagens de Título**:
   - Formata os títulos com bordas e cores para organizar as informações exibidas.

4. **Interatividade**:
   - Permite consultas sucessivas até que o usuário digite `FIM` para encerrar o programa.

5. **Validação de Entrada**:
   - Trata entradas inválidas, como strings vazias, e informa o usuário.

---

## 🛠️ **Como Funciona**

### Estrutura do Código

1. **Paleta de Cores**:
   A tupla `c` define as cores para a formatação das mensagens no terminal.

2. **Funções**:
   - `ajuda(com)`: Recebe o nome de uma função ou biblioteca, exibe sua documentação e trata erros.
   - `titulo(msg, cor=0)`: Formata e exibe mensagens com bordas e cores.

3. **Programa Principal**:
   - O loop principal solicita ao usuário um comando ou biblioteca para consulta.
   - Digitar `FIM` encerra o programa.

---

## 🚀 **Como Usar**

1. Execute o programa em um terminal compatível com ANSI.
2. Ao iniciar, o programa exibirá o título:

SISTEMA DE AJUDA PyHELP

3. Digite o nome de uma função ou biblioteca do Python para consultar, por exemplo:
Função ou Biblioteca > print

O programa exibirá a documentação correspondente.

4. Para encerrar, digite:
FIM


## 📋 **Exemplo de Execução**

~~~~~~~~~~~~~~~~~~~~~~~~~~~
SISTEMA DE AJUDA PyHELP
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Função ou Biblioteca > print
Acessando o manual do comando 'print'

Help on built-in function print in module builtins:
<conteúdo do manual>

Função ou Biblioteca > FIM
~~~~~~~~~~~~~
ATÉ LOGO!
~~~~~~~~~~~~~

## 📌 Requisitos
Python 3.6 ou superior.
Terminal compatível com sequências ANSI para exibição de cores.

## 🖋️ Licença
Este projeto é open-source e pode ser usado, modificado e distribuído livremente.

## 🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no PyHELP.
