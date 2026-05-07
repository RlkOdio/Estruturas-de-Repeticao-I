# Python Utility Scripts: Security & Infrastructure

Este repositório contém dois scripts práticos em Python desenvolvidos para resolver problemas comuns em ambientes de TI: validação de políticas de acesso e monitoramento de ativos de rede/servidores.

## Scripts Inclusos

### 1. Validador de Complexidade de Senha
Um script focado em segurança que analisa strings para garantir que as políticas de senhas fortes sejam cumpridas antes de serem aceitas por um sistema.

* **Regras de Validação:**
    * Mínimo de 8 caracteres.
    * Obrigatório ao menos uma letra maiúscula.
    * Obrigatório ao menos uma letra minúscula.
    * Obrigatório ao menos um número.
    * Obrigatório ao menos um caractere especial (`!@#$%^&*` etc).
* **Lógica:** O script percorre a string linearmente, garantindo eficiência máxima.

### 2. Monitor de Temperatura de Servidor
Uma simulação de um serviço que "escuta" sensores de hardware (via entrada manual ou integração) e dispara ações defensivas de hardware.

* **Regra de Negócio:** Se a temperatura ultrapassar **80 ºC**, o sistema dispara um alerta crítico.
* **Recursos:** * Loop contínuo de monitoramento.
    * Tratamento de exceções para entradas inválidas.
    * Interrupção segura do serviço.

---

## Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:** Nenhuma (Código 100% nativo/Built-in)

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
