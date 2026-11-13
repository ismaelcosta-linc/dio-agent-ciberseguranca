# Relatório de evidências — laboratório de cibersegurança DIO Agent

## Escopo e origem das evidências

Referências analisadas:

- [app.py](../../agent/knowledge/app.py): laboratório original, intencionalmente vulnerável.
- [app_corrigido.py](../../agent/knowledge/app_corrigido.py): versão com medidas de correção.

A análise segue a skill `secure-code-review` e considera somente esses arquivos. Ambos utilizam SQLite em memória. Não há evidência de exposição à internet, integração com sistemas externos ou uso de dados reais.

Este relatório distingue duas fontes:

- **Inspeção estática:** leitura do código, sem executar a aplicação. Permite identificar construções inseguras e medidas implementadas, mas não comprova seu comportamento em execução.
- **Resultados informados pelo usuário:** três testes manuais na versão corrigida, com entradas exatas e resultados registrados abaixo. Não foram reproduzidos pelo agente. Não existem arquivos de log ou capturas anexados ao relatório, e não foram fornecidos detalhes do ambiente.

Nenhum teste adicional foi executado para produzir este documento. Os arquivos de código não foram modificados.

## Análise comparativa

| Vulnerabilidade e causa no original | Risco associado | Correção observada | Evidência e limite |
| --- | --- | --- | --- |
| **SQL Injection (CWE-89):** `autenticar` concatena `usuario` e `senha` diretamente na consulta SQL. | Uma entrada pode alterar a condição da consulta e contornar a autenticação. Gravidade potencial alta se entradas não confiáveis alcançarem a função. | Cadastro e busca usam parâmetros `?`. A senha é verificada separadamente do SQL. | A causa foi removida por inspeção estática. O usuário informou rejeição de uma tentativa de injeção; isso não representa teste de todas as entradas possíveis. |
| **Senha em texto claro (CWE-256):** a tabela recebe e compara a senha literal. | Acesso ao conteúdo do banco revela a senha. Impacto limitado no laboratório com dados fictícios; relevante se o padrão for reutilizado com credenciais reais. | PBKDF2-HMAC-SHA256 com 600 mil iterações e salt aleatório de 16 bytes por cadastro. Armazenamento de hash, salt e iterações; comparação com `hmac.compare_digest`. | A substituição do armazenamento em texto claro é visível no código. Não houve inspeção do banco em execução nem teste específico da derivação. |
| **Credencial fixa (CWE-798):** uma conta com senha conhecida é inserida a cada chamada. | Quem conhece o código conhece uma credencial válida. Gravidade baixa no laboratório; potencialmente alta em uso real. O nome da conta não comprova privilégios administrativos. | Usuário e senha são fornecidos interativamente; `getpass` oculta a digitação da senha em terminal compatível. | Não há credencial fixa na versão corrigida analisada. A conclusão decorre da leitura do arquivo. |
| **Fechamento inadequado da conexão (CWE-404):** uma exceção antes de `close()` impede o fechamento explícito. | Interrupção do fluxo e possível retenção de recursos. Gravidade baixa no laboratório; esgotamento dependeria de repetição e do ambiente. | `contextlib.closing` envolve o uso da conexão no fluxo principal. O cadastro usa uma transação com confirmação ou reversão. | O fechamento está previsto inclusive na saída por exceção. Não foi executado teste de falha. Funções reutilizadas com outra conexão dependem do gerenciamento feito pelo chamador. |

As quatro causas estão presentes no original e suas medidas de correção estão presentes na versão corrigida por inspeção estática. As classificações são qualitativas e condicionadas ao contexto, sem exploração do original ou comprovação de impacto externo.

## Testes manuais informados pelo usuário

Em cada teste, o usuário informou ter cadastrado `usuario_teste` com a senha fictícia `senha_laboratorio_2026`.

| Cenário | Entradas de autenticação informadas | Resultado informado | Interpretação e limite |
| --- | --- | --- | --- |
| Autenticação válida | Usuário: `usuario_teste`; senha: `senha_laboratorio_2026`. | `Autenticado.` | Sustenta o funcionamento do fluxo legítimo no cenário utilizado. |
| Senha incorreta | Usuário: `usuario_teste`; senha: `senha_errada`. | `Credenciais inválidas.` | Sustenta a distinção entre senha correta e incorreta no cenário utilizado. |
| Tentativa de SQL Injection | Usuário: `usuario_teste' OR '1'='1`; senha: `senha_errada`. | `Credenciais inválidas.` | A tentativa utilizada não contornou a autenticação. |

Esses resultados são relatos do usuário, não execuções ou observações diretas do agente. Não existem arquivos de log ou capturas anexados ao relatório. Não há resultados de testes do original disponíveis para uma comparação experimental antes/depois. A comparação entre versões é estática, complementada pelos três relatos sobre a versão corrigida.

## Riscos residuais

| Observação | Avaliação conforme as evidências | Medida recomendada |
| --- | --- | --- |
| O cadastro aceita qualquer senha não vazia. | Limitação confirmada. Risco baixo no laboratório; senhas fracas continuam suscetíveis a adivinhação, inclusive em ataque offline se hashes forem obtidos. | Em uso real, definir critérios de senha adequados ao contexto. |
| Não há limitação de tentativas. | Não caracteriza ataque demonstrado no fluxo local, que realiza uma tentativa por execução. Tentativas repetidas e consumo de CPU pelo PBKDF2 são riscos hipotéticos se a função virar um serviço acessível. | Implementar controle de frequência se houver essa integração. |
| Senhas existem temporariamente na memória; `del` não garante apagamento seguro. | Limitação confirmada, com risco baixo no laboratório. Exploração dependeria de acesso à memória do processo. Isso não equivale a armazenar senha em texto claro no banco. | Usar dados fictícios, evitar logs de senha e não tratar `del` como limpeza segura. |
| Erros esperados, como cadastro vazio, podem encerrar o programa com exceção. | Limitação de robustez confirmada por leitura. Divulgação remota de erros não está demonstrada. | Tratar erros esperados na interface sem expor dados sensíveis. |
| O trabalho de derivação também ocorre para usuário inexistente. | Medida observada para reduzir diferenças de tempo evidentes. Não comprova tempo total constante nem ausência de canais laterais. | Avaliar esse comportamento caso o laboratório seja adaptado para um serviço real. |

Não há evidência suficiente para afirmar comprometimento remoto, vazamento de credenciais reais ou execução de comandos do sistema.

## Conclusão educativa

A versão corrigida separa dados de comandos SQL, substitui senhas armazenadas por hashes com salt, remove a credencial fixa e garante o fechamento da conexão no fluxo principal. Essas mudanças tratam as quatro causas identificadas no laboratório original.

Os três testes relatados apoiam o funcionamento básico e a rejeição da tentativa de injeção utilizada. Eles não demonstram ausência de todas as vulnerabilidades nem validam especificamente o armazenamento ou o fechamento em situações de erro. Nenhuma validação adicional foi realizada.

O aprendizado central é combinar prevenção no código com evidências de validação: cada conclusão deve indicar o que foi observado, de onde veio a evidência e quais limites permanecem. O exemplo continua sendo um laboratório educativo, sem comprovação de adequação para produção.
