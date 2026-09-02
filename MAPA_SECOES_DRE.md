# Mapa de seção do DRE e do Fluxo de Caixa — Painel Financeiro QUORUM

Este documento existe para consulta rápida, sem precisar abrir `index.html`
(onde o mapa vive de fato, na constante `SECAO_POR_CODIGO_GRUPO`). Qualquer
mudança de verdade acontece **no código**; este arquivo é só a leitura
legível dela, e precisa ser atualizado junto sempre que o mapa mudar.

## O que é fato e o que é decisão

- **Quais grupos e categorias existem, e como se chamam**: isso vem da Omie,
  ao vivo, a cada carga do painel. É fato, não mora aqui.
- **Em qual linha do resultado cada grupo entra**: isso é decisão gerencial
  da QUORUM, não um dado que a Omie fornece. É essa decisão que este
  documento registra.
- O vínculo no código é sempre pelo **código do grupo** (ex.: `1.01`), nunca
  pelo nome — código é estável, nome muda quando alguém renomeia na Omie.
- Grupo que não estiver no mapa não desaparece: cai em **"Não classificado"**,
  visível no Fluxo de Caixa, como alerta de que falta decidir onde ele entra.

## Tabela completa (30 grupos, conferida contra o catálogo real em 02/09/2026)

| Código | Nome do grupo na Omie | Seção | Rótulo na tela | Sinal |
|---|---|---|---|---|
| 1.01 | Receita de Patrocínio | `receita` | Receita Bruta | + |
| 1.02 | Receita de Eventos Abertos | `receita` | Receita Bruta | + |
| 1.03 | Receita de Evento Fechado | `receita` | Receita Bruta | + |
| 1.04 | Receita de Quorum House | `receita` | Receita Bruta | + |
| 1.05 | Receita de Assinaturas | `receita` | Receita Bruta | + |
| 1.06 | Receita de Advisory | `receita` | Receita Bruta | + |
| 1.07 | Receita de Comissões | `receita` | Receita Bruta | + |
| 1.08 | Receitas Financeiras | `finRec` | Receitas Financeiras | + |
| 1.09 | Outras Receitas Operacionais | `outrasRec` | Outras Receitas e Não Operacional | + |
| 1.10 | Resultado Não Operacional (Receitas) | `outrasRec` | Outras Receitas e Não Operacional | + |
| 2.01 | Custo de Patrocínio | `custo` | Custo dos Serviços Prestados | − |
| 2.02 | Custo de Eventos Abertos | `custo` | Custo dos Serviços Prestados | − |
| 2.03 | Custo de Evento Fechado | `custo` | Custo dos Serviços Prestados | − |
| 2.04 | Custo de Quorum House | `custo` | Custo dos Serviços Prestados | − |
| 2.05 | Custo de Assinaturas | `custo` | Custo dos Serviços Prestados | − |
| 2.06 | Custo de Advisory | `custo` | Custo dos Serviços Prestados | − |
| 2.07 | Outros Custos dos Serviços | `custo` | Custo dos Serviços Prestados | − |
| 2.08 | Despesas com Pessoal | `despesas` | Despesas Fixas | − |
| 2.09 | Despesas Administrativas | `despesas` | Despesas Fixas | − |
| 2.10 | Despesas de Vendas e Marketing | `despesas` | Despesas Fixas | − |
| 2.11 | Despesas com Tecnologia | `despesas` | Despesas Fixas | − |
| 2.12 | Despesas Comerciais e de Representação | `despesas` | Despesas Fixas | − |
| 2.13 | Despesas Financeiras | `finDesp` | Despesas Financeiras | − |
| 2.14 | Impostos e Taxas | `impostos` | Impostos e Deduções | − |
| 2.15 | Impostos sobre o Lucro (regime futuro) | `impLucro` | Impostos sobre o Lucro | − |
| 2.20 | Resultado Não Operacional (Despesas) | `outrasDesp` | Resultado Não Operacional (Despesas) | − |
| 1.11 | Movimentações do Passivo - Entradas | `entradas` | Entradas Não Operacionais | + |
| 2.16 | Lucros/Dividendos a Distribuir a Sócios | `saidas` | Saídas Não Operacionais | − |
| 2.17 | Movimentações do Passivo - Saídas | `saidas` | Saídas Não Operacionais | − |
| 2.18 | Movimentação do Ativo | `ativo` | Movimentação do Ativo | − |
| 2.19 | Investimentos em Imobilizado e Intangível | `capex` | Investimentos | − |
| 0.01 | Transferência | `transf` | Transferências entre Contas | + |

## Onde cada seção aparece

**DRE** (`SECOES_DRE`, nesta ordem): Receita Bruta → Impostos e Deduções →
Custo dos Serviços Prestados → Despesas Fixas → Receitas Financeiras →
Despesas Financeiras → Outras Receitas e Não Operacional → Resultado Não
Operacional (Despesas) → Impostos sobre o Lucro.

**Fluxo de Caixa** (`SECOES_FLUXO`, nesta ordem): Entradas Não Operacionais →
Saídas Não Operacionais → Movimentação do Ativo → Investimentos →
Transferências entre Contas → **Não classificado** (rede de segurança, nunca
some um lançamento calado).

## Por que 1.11 e 2.16/2.17 não entram na Receita/Despesa do DRE

Mútuo de sócio, AFAC, adiantamento de cliente (1.11) e a devolução deles
(2.17), junto com distribuição de lucro/dividendo (2.16), são movimentação de
**passivo**, não resultado operacional — entram e saem de caixa mas não são
receita nem despesa da operação. Por isso ficam no Fluxo de Caixa
(`entradas`/`saidas`), fora do DRE.

## Manutenção

Sempre que a constante `SECAO_POR_CODIGO_GRUPO` mudar no código (novo grupo
criado na Omie, ou reclassificação de um grupo existente), atualizar esta
tabela na mesma sessão de trabalho — documentação desatualizada é pior que
nenhuma, porque parece confiável sem ser.
