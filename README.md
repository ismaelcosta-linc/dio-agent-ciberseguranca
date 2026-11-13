# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Revisão de segurança de código](skills/secure-code-review/SKILL.md) | Identifica vulnerabilidades, orienta correções e valida mitigações | "Analise a segurança deste código Python e valide as correções." |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                Este guia
├── AGENTS.md                Definição do agente (lida pelo harness)
├── CLAUDE.md                Atalho para o Claude Code
├── agent/
│   ├── persona.md           A personalidade e o tom do agente
│   └── knowledge/           Contexto da DIO e laboratório educacional
│       ├── app.py           Laboratório intencionalmente vulnerável
│       ├── app_corrigido.py Laboratório com correções de segurança
│       └── ...              Demais arquivos de conhecimento
├── skills/                  Uma pasta por skill, cada uma com o seu SKILL.md
│   ├── secure-code-review/
│   │   └── SKILL.md         Guia de revisão de segurança de código
│   └── ...                  Demais skills
└── docs/
    ├── glossary.md          Glossário de termos
    ├── youcom-mcp.md        Como conectar a busca do You.com
    └── evidencias/
        └── relatorio-testes.md  Análise comparativa e testes relatados
```

---

## Personalização — Cibersegurança defensiva

Esta personalização foi desenvolvida como atividade do curso Santander/DIO, em ambiente **Debian GNU/Linux 13**, com uso do **Codex CLI**. O desenvolvimento e a documentação contaram com o auxílio do Codex CLI e do chatbot ChatGPT.

Agradeço à professora Isadora Ferrão pelas orientações e pelos conhecimentos compartilhados durante as aulas de cibersegurança do programa Santander/DIO.

Os arquivos [agent/persona.md](agent/persona.md) e [AGENTS.md](AGENTS.md) foram personalizados para orientar a atuação do agente em cibersegurança defensiva. Foi criada a skill [skills/secure-code-review/SKILL.md](skills/secure-code-review/SKILL.md), que orienta a identificação de vulnerabilidades, a avaliação de riscos, a proposição de correções e sua validação com evidências.

O laboratório usa Python e SQLite em memória, com duas versões:

- [agent/knowledge/app.py](agent/knowledge/app.py): versão original, intencionalmente vulnerável, preservada para comparação.
- [agent/knowledge/app_corrigido.py](agent/knowledge/app_corrigido.py): versão com consultas parametrizadas, hash de senha com salt, credenciais informadas durante a execução e fechamento garantido da conexão no fluxo principal.

A inspeção estática identificou quatro problemas no original: **SQL Injection**, **armazenamento de senha em texto claro**, **credencial fixa no código** e **gerenciamento inadequado da conexão**. A versão corrigida implementa medidas para tratar essas quatro causas.

O usuário informou os seguintes testes manuais na versão corrigida. Em cada teste, cadastrou `usuario_teste` com a senha fictícia `senha_laboratorio_2026`:

| Teste | Entradas de autenticação | Resultado informado pelo usuário |
| --- | --- | --- |
| Autenticação válida | Usuário `usuario_teste` e senha `senha_laboratorio_2026` | `Autenticado.` |
| Rejeição de senha incorreta | Usuário `usuario_teste` e senha `senha_errada` | `Credenciais inválidas.` |
| Rejeição de tentativa de SQL Injection | Usuário `usuario_teste' OR '1'='1` e senha `senha_errada` | `Credenciais inválidas.` |

Esses resultados foram relatados pelo usuário e não executados pelo agente. Não há arquivos de log ou capturas anexados ao relatório. A análise comparativa, os limites das evidências e os riscos residuais estão em [docs/evidencias/relatorio-testes.md](docs/evidencias/relatorio-testes.md).

A finalidade desta personalização e de seu laboratório é exclusivamente **educacional e defensiva**, com dados fictícios e em ambientes autorizados. Os resultados disponíveis não comprovam adequação para produção.

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
