# Gerador de Senha Forte

Este sistema gera senhas fortes e seguras, combinando letras maiúsculas, minúsculas, números e símbolos. A senha gerada terá um tamanho fixo de 10 caracteres e será embaralhada para garantir mais segurança.

### Como Funciona

O código segue os seguintes passos:

1. **Importação das Bibliotecas:**
   - `random`: Utilizada para sortear caracteres aleatórios.
   - `string`: Fornece categorias de caracteres (letras maiúsculas, minúsculas, números e símbolos).

2. **Solicitação de Entrada do Usuário:**
   - O código começa perguntando ao usuário se ele deseja gerar uma senha.
   - Se o usuário responder **"Y" (Sim)**, a senha será gerada.
   - Se o usuário responder **"N" (Não)**, o código será finalizado.

3. **Processo de Geração da Senha:**
   - **Tamanho da Senha**: O tamanho da senha será 10 caracteres.
   - **Seleção de Caracteres**: A senha será composta por uma mistura de:
     - **Letras Maiúsculas**: A-Z
     - **Letras Minúsculas**: a-z
     - **Números**: 0-9
     - **Símbolos**: !@#$%^&*()-_=+
   - O código começa escolhendo aleatoriamente um caractere de cada tipo e, em seguida, preenche o restante da senha com caracteres aleatórios de todas as categorias.

4. **Embaralhamento da Senha:**
   - Após gerar os caracteres, a lista de caracteres da senha é **embaralhada** para garantir que não haja um padrão previsível.

5. **Exibição da Senha Gerada:**
   - A senha final é exibida na tela.

---
