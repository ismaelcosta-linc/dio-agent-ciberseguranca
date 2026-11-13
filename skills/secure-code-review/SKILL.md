---
name: secure-code-review
description: Analisa a segurança de código, identifica vulnerabilidades, orienta correções e valida as mitigações com testes e evidências.
---

# Secure Code Review

## Objetivo

Realizar revisões de segurança de código de maneira educativa,
controlada e verificável.

## Procedimento

### 1. Compreender o contexto

- Identificar a linguagem, a finalidade e o ambiente da aplicação.
- Verificar quais arquivos devem ser analisados.
- Confirmar o escopo e solicitar autorização antes de modificar
  arquivos ou executar testes potencialmente invasivos.
- Não presumir que uma vulnerabilidade está exposta à internet.

### 2. Analisar o código

- Identificar possíveis vulnerabilidades e práticas inseguras.
- Indicar arquivos, linhas e trechos relevantes.
- Explicar a causa técnica e as possíveis consequências.
- Distinguir vulnerabilidades confirmadas de riscos hipotéticos.

### 3. Classificar os riscos

Para cada achado, registrar:

- Vulnerabilidade identificada.
- Classificação CWE e OWASP, quando aplicável.
- Técnica MITRE ATT&CK, somente quando houver relação justificável.
- Impacto, probabilidade e gravidade estimados.
- Evidências e limitações da análise.

### 4. Propor correções

- Priorizar soluções simples e eficazes.
- Explicar como a correção reduz o risco.
- Evitar alterações desnecessárias no projeto.
- Solicitar autorização antes de modificar arquivos.

### 5. Validar as correções

Após autorização:

- Registrar o comportamento anterior à correção.
- Aplicar a mitigação proposta.
- Executar testes locais e controlados.
- Verificar se a vulnerabilidade deixou de ser reproduzível.
- Verificar se a funcionalidade legítima continua funcionando.
- Informar quando não for possível executar algum teste.

### 6. Apresentar o relatório

Produzir um relatório conciso contendo:

1. Escopo da análise.
2. Vulnerabilidades e classificações.
3. Evidências anteriores à correção.
4. Correções realizadas.
5. Testes executados e respectivos resultados.
6. Comparação antes/depois.
7. Riscos residuais e recomendações.

## Regras de segurança

- Trabalhar somente em sistemas e arquivos autorizados.
- Não realizar exploração contra sistemas de terceiros.
- Não coletar credenciais reais ou informações sensíveis.
- Preferir ambientes locais, isolados e dados fictícios.
- Não afirmar que uma vulnerabilidade foi corrigida sem validação.
- Não inventar resultados, classificações ou evidências.
