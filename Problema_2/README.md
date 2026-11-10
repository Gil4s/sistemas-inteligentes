# Problema 2 - Regressão Logística na Previsão de Doenças Cardíacas

## Contexto e Pré-processamento

O objetivo deste projeto é prever a presença ou ausência de doença cardíaca a partir de 13 variáveis clínicas do dataset Heart Disease Cleveland (UCI).

Etapas realizadas no pré-processamento:
1. **Tratamento de valores ausentes:** O arquivo original possui 303 registros, com valores ausentes representados pelo caractere `'?'` (4 na coluna `ca` e 2 na coluna `thal`). Ao carregá-los com `na_values='?'` e remover as 6 linhas incompletas (`dropna()`), restaram **297 pacientes**.
2. **Binarização da variável alvo (`target`):** No dataset original, `0` indica ausência de doença e os valores de `1` a `4` indicam presença de doença. A coluna foi convertida para binária (`0` = sem doença, com 160 amostras; `1` = com doença, com 137 amostras).
3. **Divisão e Padronização:** Os dados foram divididos de forma estratificada em 80% para treino (237 amostras) e 20% para teste (60 amostras), e as 13 variáveis independentes foram padronizadas via `StandardScaler` ajustado apenas no treino.

---

## 1. Treinamento do Modelo e Convergência

O modelo foi treinado utilizando `LogisticRegression(solver='liblinear', random_state=42, max_iter=1000)` sobre os dados de treino padronizados.
- **Número de iterações necessárias para a convergência:** `6` iterações (obtido pelo atributo `modelo.n_iter_`).

---

## 2. Avaliação do Modelo no Conjunto de Teste

Avaliando o modelo nos 60 pacientes do conjunto de teste, foram obtidos os seguintes resultados:

**Matriz de Confusão:**
- Verdadeiros Negativos (sem doença e previstos sem doença): `32`
- Falsos Positivos (sem doença, mas previstos com doença): `4`
- Falsos Negativos (com doença, mas previstos sem doença): `4`
- Verdadeiros Positivos (com doença e previstos com doença): `20`

**Métricas de Desempenho:**
- **Acurácia:** `0.8667` (86,67% de acerto geral)
- **Precisão:** `0.8333` (dos pacientes classificados como doentes pelo modelo, 83,33% realmente tinham a doença)
- **Recall (Sensibilidade):** `0.8333` (dos pacientes que realmente tinham doença cardíaca, o modelo identificou 83,33%)
- **F1-score:** `0.8333`
- **AUC (Área sob a Curva ROC):** `0.9421`

**Conclusão:** O modelo apresentou bom desempenho preditivo, com equilíbrio entre Precisão e Recall (`83,33%`) e uma área sob a curva ROC de `0.9421`, indicando alta capacidade de separar pacientes saudáveis de pacientes com doença cardíaca.
