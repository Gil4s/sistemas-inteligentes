# Problema 4 - Classificação de Risco de Crédito com Árvores de Decisão

## 1. Preparação dos Dados, Atributos e Balanceamento

O arquivo `german.data` possui 1.000 amostras com 20 atributos de entrada e 1 variável alvo (`risco`):
- **7 atributos numéricos:** `duracao_meses`, `valor_credito`, `taxa_parcela`, `tempo_residencia`, `idade`, `creditos_existentes`, `dependentes`.
- **13 atributos categóricos:** `status_conta`, `historico_credito`, `finalidade`, `poupanca`, `tempo_emprego`, `estado_civil_sexo`, `fiador`, `propriedade`, `outros_planos`, `moradia`, `trabalho`, `telefone`, `trabalhador_estrangeiro`.
- **Codificação:** Foi aplicado One-Hot Encoding (`pd.get_dummies` com `drop_first=True`), resultando em 48 colunas numéricas, evitando criar uma ordem artificial em atributos nominais (como finalidade do empréstimo).
- **Balanceamento:** O dataset possui **700 bons pagadores (70%) e 300 maus pagadores (30%)**. Esse desbalanceamento faz com que a acurácia isolada seja enganosa: um modelo que aprove crédito para 100% das pessoas teria 70% de acurácia, mas falharia em barrar qualquer inadimplente.

---

## 2. Por que a Normalização não é Necessária para uma Árvore de Decisão?

A árvore de decisão divide os nós testando um atributo por vez com regras de corte (`atributo <= valor`), avaliando apenas a ordem dos valores e a pureza das classes de cada lado (Gini ou Entropia), sem calcular distâncias geométricas entre colunas. Alterar a escala numérica não muda a ordem dos valores nem os pontos de divisão da árvore.

---

## 3. Divisão Treino e Teste Estratificada

Os dados foram divididos em 80% para treino (800 amostras) e 20% para teste (200 amostras) com `stratify=y`, preservando exatamente 70% de classe `bom` e 30% de classe `mau` em ambos os conjuntos.

---

## 4. Controle de Complexidade (Profundidade, Gini e Entropia)

Resultados da validação cruzada de 5 folds no treino variando `max_depth`:

| Profundidade | Treino (Gini) | Validação (Gini) | Treino (Entropia) | Validação (Entropia) |
| --- | --- | --- | --- | --- |
| 2 | 0.7000 | 0.6888 | 0.7000 | 0.6938 |
| 3 | 0.7050 | 0.6975 | 0.7050 | 0.6988 |
| **5** | **0.7575** | **0.7012** | **0.7475** | **0.7137** |
| 7 | 0.8325 | 0.6900 | 0.8225 | 0.7000 |
| 10 | 0.9175 | 0.6662 | 0.8912 | 0.7088 |
| Sem limite | 1.0000 | 0.6650 | 1.0000 | 0.7088 |

- **Profundidade escolhida:** `max_depth = 5` (melhor validação tanto em Gini quanto em Entropia).
- **Profundidades baixas (ex: 2):** A árvore faz poucas perguntas e não captura os padrões dos dados (*underfitting*).
- **Profundidades altas (ex: 10 ou Sem limite):** O treino chega a 100%, mas a validação cai (*overfitting*), pois a árvore decora o ruído do conjunto de treino.
- **Gini vs Entropia:** Os dois critérios tiveram comportamento muito próximo, com leve vantagem para Entropia em `max_depth = 5` (`71,37%` vs `70,12%`).

---

## 5. Interpretação do Modelo e Importância dos Atributos

**Três atributos mais determinantes (`max_depth = 5`):**
1. `status_conta_A14` (`29,54%`): indica se o cliente não possui conta corrente registrada.
2. `valor_credito` (`21,78%`): valor total solicitado no empréstimo.
3. `duracao_meses` (`8,53%`): prazo de pagamento do empréstimo em meses.

**Regra em linguagem natural até a folha classificada como mau risco com mais amostras (22 maus e 3 bons):**
> Se o cliente possui conta corrente com saldo baixo ou negativo (`status_conta_A14 <= 0.5`), o prazo do empréstimo é maior que 11,5 meses (`duracao_meses > 11.5`), possui poupança registrada (`poupanca_A65 <= 0.5`), o valor solicitado é superior a 8.015,50 DM (`valor_credito > 8015.50`) e não se enquadra como trabalhador não qualificado residente (`trabalho_A172 <= 0.5`), então o cliente é classificado como **mau risco**.

---

## 6. Avaliação no Conjunto de Teste e Ajuste de Treinamento

Avaliando no conjunto de teste (200 amostras: 140 `bom` e 60 `mau`), a **acurácia foi de `0.6950` (69,50%)**:
- **Classe `bom`:** Precisão `0.72`, Recall `0.94`, F1-score `0.81` (`131` acertos e `9` erros).
- **Classe `mau`:** Precisão `0.47`, Recall `0.13`, F1-score `0.21` (`8` acertos e `52` erros).

**Análise do erro mais frequente e ajuste:**
- O erro mais frequente do modelo padrão é classificar um **mau pagador real como bom pagador** (52 casos entre os 60 maus pagadores, gerando um Recall de apenas `13,33%` na classe `mau`).
- Esse é o erro mais grave para o banco, pois conceder empréstimo a um inadimplente causa perda direta do capital emprestado, que custa muito mais caro do que deixar de ganhar os juros de um bom cliente recusado.
- **Ajuste aplicado:** Passando o parâmetro `class_weight='balanced'` no treinamento da árvore para compensar o desbalanceamento 70%/30%, o Recall da classe `mau` subiu de **`13,33%` para `71,67%`** (detectando 43 dos 60 maus pagadores no teste).
