# Trilha de Revisão e Fundamentos - Sistemas Inteligentes (PAM0466)

> **Docente:** Prof. Dr. Pedro Thiago Valério de Souza  
> **Aluno:** Gil (UFERSA)  
> **Foco:** Entendimento conceitual profundo, fluência em Python/Scikit-Learn e preparação para a **Defesa Oral Individual**.

---

## 🎯 Por que esta revisão antes do código?
A avaliação não consiste apenas na entrega de código funcionando:
1. **Códigos em repositório público** (limpos, organizados e reprodutíveis).
2. **Relatório em `.md`** justificando decisões estatísticas e respondendo perguntas analíticas.
3. **Defesa Oral Individual** na sala do professor. Saber *o que* o algoritmo faz por debaixo dos panos, *por que* foi aplicada uma transformação e *como* interpretar as métricas é o que garante nota máxima.

---

## 🗺️ Mapa de Conhecimentos por Projeto

### ⚡ Projeto 1: Regressão Linear Múltipla (Usina CCPP)
* **Objetivo:** Prever a potência elétrica (`PE`) a partir de sensores ambientais (`AT`, `V`, `AP`, `RH`).
* **Conceitos Teóricos:**
  * Regressão Linear Simples vs. Múltipla ($y = \beta_0 + \sum \beta_i X_i + \epsilon$).
  * Matriz de Correlação (Pearson) e interpretação de força/sentido.
  * **Multicolinearidade**: o que é, como identificar (correlação alta entre variáveis explicativas) e por que afeta a estabilidade dos coeficientes.
  * Métricas de Regressão: $R^2$ (coeficiente de determinação), MAE (Erro Médio Absoluto) e RMSE (Raiz do Erro Quadrático Médio — penalização de grandes erros).
* **Python / Scikit-Learn Prático:**
  * `pandas`: `.corr()`, `.isna().sum()`, `.describe()`.
  * `seaborn` / `matplotlib`: `sns.heatmap(..., annot=True)`, gráficos de dispersão com linha de regressão (`sns.regplot`).
  * `sklearn.model_selection.train_test_split(..., test_size=0.2, random_state=42)`.
  * `sklearn.preprocessing.StandardScaler` vs `MinMaxScaler`.
  * `sklearn.linear_model.LinearRegression`.
  * `sklearn.metrics`: `r2_score`, `mean_squared_error(..., squared=False)`, `mean_absolute_error`.

---

### 🫀 Projeto 2: Regressão Logística (Doenças Cardíacas - Cleveland)
* **Objetivo:** Classificar a presença ou ausência de cardiopatia (0 ou 1) com base em 13 variáveis clínicas.
* **Conceitos Teóricos:**
  * Diferença entre Regressão Linear e Logística (função sigmoide $\sigma(z) = \frac{1}{1 + e^{-z}}$, log-odds / logit).
  * Otimizadores numéricos: por que não há solução analítica fechada e o papel do `solver='liblinear'` com convergência via iterações (`max_iter`).
  * Binarização de alvos multiclasse (0 = sem doença, 1 a 4 = com doença).
  * Métricas de Classificação:
    * Matriz de Confusão: TP, FP, TN, FN.
    * Acurácia, Precisão ($TP / (TP + FP)$) e Recall ($TP / (TP + FN)$).
    * F1-Score (média harmônica entre Precisão e Recall).
    * Curva ROC e AUC (capacidade discriminativa independente de limiar de corte).
* **Python / Scikit-Learn Prático:**
  * `pandas`: binarização com `.apply()` ou `np.where(y > 0, 1, 0)`, tratamento de interrogações `'?'` como missing values.
  * `sklearn.linear_model.LogisticRegression(solver='liblinear', random_state=42, max_iter=1000)`.
  * Atributo `model.n_iter_` para verificar quantas iterações foram necessárias para convergir.
  * `sklearn.metrics`: `classification_report`, `confusion_matrix`, `ConfusionMatrixDisplay`, `roc_curve`, `roc_auc_score`, `RocCurveDisplay`.

---

### 🍷 Projeto 3: Classificação com $k$-NN (Qualidade de Vinhos)
* **Objetivo:** Prever classes de qualidade (ruim $\le 5$, médio $6-7$, bom $\ge 8$) com base em físico-química.
* **Conceitos Teóricos:**
  * Como funciona o $k$-NN: algoritmo baseado em instâncias (lazy learning), métrica de distância (Euclidiana, Manhattan).
  * **Por que a normalização é obrigatória no $k$-NN?** (Variáveis em escalas grandes dominam o cálculo da distância Euclidiana).
  * Divisão **Estratificada** (`stratify=y`): preservação das proporções originais das classes em problemas desbalanceados.
  * Validação Cruzada ($k$-fold CV, no caso 5 folds) para escolha do hiperparâmetro $k$.
  * Comportamento dos extremos:
    * $k$ muito baixo (ex: $k=1$): sensível a ruído e outliers (overfitting, alta variância).
    * $k$ muito alto: fronteira de decisão excessivamente suave, viés em direção à classe majoritária (underfitting).
* **Python / Scikit-Learn Prático:**
  * `pandas`: mapeamento de classes numéricas para categorias (`pd.cut` ou lógica customizada).
  * `sklearn.model_selection.StratifiedKFold`, `cross_val_score`.
  * `sklearn.neighbors.KNeighborsClassifier`.
  * Plot de hiperparâmetro: curva de acurácia média $\pm$ desvio padrão em função de $k$.
  * Análise de erros específicos por classe na matriz de confusão.

---

### 💳 Projeto 4: Árvores de Decisão (Risco de Crédito - German Credit)
* **Objetivo:** Classificar solicitantes como bom ou mau pagador, com foco em interpretabilidade e regras de decisão.
* **Conceitos Teóricos:**
  * Estrutura da árvore: Nó raiz, nós de decisão (divisões/splits) e nós folha.
  * Critérios de divisão de nós: Índice de Impureza de Gini vs. Entropia / Ganho de Informação.
  * **Por que árvores NÃO exigem normalização de atributos?** (As divisões são baseadas apenas em limiares ordinais monotônicos $X_j \le \theta$).
  * Pré-processamento categórico: One-Hot Encoding vs. Ordinal Encoding.
  * Risco de Crédito e Desbalanceamento (70% bom / 30% mau): por que acurácia pura engana e o custo assimétrico dos erros (Falso Positivo vs. Falso Negativo: aprovar um caloteiro é muito mais grave para o banco do que recusar um bom pagador).
  * Controle de complexidade e overfitting: `max_depth` e curvas de treino vs. validação.
  * Extração de regras em linguagem natural e `feature_importances_`.
* **Python / Scikit-Learn Prático:**
  * `sklearn.datasets.fetch_openml('credit-g', version=1)` ou leitura do arquivo `german.data`.
  * `pd.get_dummies` / `OneHotEncoder`.
  * `sklearn.tree.DecisionTreeClassifier(criterion='gini' / 'entropy', max_depth=...)`.
  * `sklearn.tree.plot_tree`, `sklearn.tree.export_text`.
  * Curvas de aprendizado / complexidade (`validation_curve`).
  * Ajustes de custo / threshold: `class_weight='balanced'`.

---

### 🛒 Projeto 5: Segmentação com $k$-Means (Wholesale Customers - Não Supervisionado)
* **Objetivo:** Descobrir perfis de consumo agrupando clientes atacadistas sem uso de rótulos prévios.
* **Conceitos Teóricos:**
  * Aprendizado Supervisionado vs. Não Supervisionado: ausência de variável alvo ($y$) e o desafio da validação sem "gabarito".
  * Pré-processamento específico:
    * Assimetria à direita e calda longa: transformação logarítmica $x' = \log(1 + x)$ (`np.log1p`).
    * Padronização $Z$-score e a distância euclidiana para o cálculo dos centroides.
  * Escolha de $k$: Método do Cotovelo (Inércia / WCSS) vs. Coeficiente de Silhueta Médio. Por que a inércia decresce monotonicamente e o que acontece quando $k=N$.
  * Mínimos locais e Inicialização: `init='random'` vs `init='k-means++'`.
  * Interpretação de negócios: reverter centroides para a escala real em unidades monetárias ($\exp(x') - 1$).
  * Validação Externa (comparação com canais `Channel` e regiões `Region`) usando tabelas de contingência e **Adjusted Rand Index (ARI)**.
  * Redução de Dimensionalidade (PCA 2D) para visualização e identificação das limitações do $k$-Means (clusters esféricos e sensibilidade a outliers).
* **Python / Scikit-Learn Prático:**
  * `numpy.log1p`, `numpy.expm1`.
  * `sklearn.cluster.KMeans(n_clusters=..., init='k-means++', n_init=...)`.
  * `sklearn.metrics.silhouette_score`, `silhouette_samples`.
  * `sklearn.metrics.adjusted_rand_score`.
  * `sklearn.decomposition.PCA`.
  * Gráficos comparativos com Seaborn: scatterplot 2D colorido por cluster e centroides projetados.

---

## 🗓️ Roteiro Proposto de Estudos Juntos
1. **Passo 1:** Revisão Express das Ferramentas Fundamentais (Pandas, NumPy, Matplotlib/Seaborn e pipeline básico do Scikit-Learn).
2. **Passo 2:** Estudo Dirigido do **Projeto 1** (Regressão Linear Múltipla, correlações e métricas contínuas).
3. **Passo 3:** Estudo Dirigido do **Projeto 2** (Regressão Logística, probabilidade, convergência e métricas de diagnóstico).
4. **Passo 4:** Estudo Dirigido do **Projeto 3** ($k$-NN, impacto da escala, distância e validação cruzada estratificada).
5. **Passo 5:** Estudo Dirigido do **Projeto 4** (Árvores de decisão, Gini vs Entropia, interpretabilidade e custo de erro em crédito).
6. **Passo 6:** Estudo Dirigido do **Projeto 5** ($k$-Means, transformações log, silhueta, PCA e validação externa não supervisionada).
