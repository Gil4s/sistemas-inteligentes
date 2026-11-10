# Problema 1 - Regressão Linear na Previsão de Energia (Usina de Ciclo Combinado)

## Contexto e Pré-processamento

O objetivo deste projeto é prever a potência elétrica líquida gerada por hora (`PE`, em MW) de uma usina termelétrica de ciclo combinado a partir de quatro variáveis ambientais:
- `AT`: Temperatura Ambiente (°C)
- `V`: Vácuo de Escape (cm Hg)
- `AP`: Pressão Atmosférica (mbar)
- `RH`: Umidade Relativa (%)

O dataset possui 9.568 amostras e não apresentou valores ausentes (`0` nulos em todas as colunas). Antes do treinamento, os dados foram divididos em 80% para treino (7.654 amostras) e 20% para teste (1.914 amostras), e as variáveis independentes foram padronizadas com Z-score (`StandardScaler`), ajustando a média e o desvio padrão apenas no conjunto de treino para evitar vazamento de dados.

---

## 1. Correlação com a Variável Alvo (PE)

A correlação de Pearson calculada entre cada variável independente e a produção de energia (`PE`) foi:
- **AT com PE:** `-0.9481` (correlação negativa muito forte)
- **V com PE:** `-0.8698` (correlação negativa forte)
- **AP com PE:** `0.5184` (correlação positiva moderada)
- **RH com PE:** `0.3898` (correlação positiva fraca a moderada)

**Conclusão:** As variáveis que têm maior influência na produção de energia são a Temperatura Ambiente (`AT`) e o Vácuo de Escape (`V`). Como ambas têm correlação negativa, o aumento da temperatura ou do vácuo reduz a potência elétrica gerada pela usina.

---

## 2. Correlação entre as Variáveis Independentes (Multicolinearidade)

Analisando a correlação das variáveis de entrada entre si, os principais valores encontrados foram:
- **AT e V:** `0.8441` (correlação positiva forte)
- **AT e RH:** `-0.5425` (correlação negativa moderada)
- **AT e AP:** `-0.5075` (correlação negativa moderada)

**Conclusão:** Existe uma relação forte entre `AT` e `V` (`0.8441`), o que indica presença de multicolinearidade. Na prática, isso significa que essas duas variáveis variam juntas e trazem parte da mesma informação para o modelo linear, tornando os pesos individuais de cada uma mais sensíveis.

---

## 3. Modelo de Regressão Linear Múltipla

Após o treinamento do modelo `LinearRegression` com os dados padronizados de treino, a equação obtida apresentou os seguintes parâmetros:
- **Intercepto:** `454.4310`
- **Coeficiente AT:** `-14.7639`
- **Coeficiente V:** `-2.9496`
- **Coeficiente AP:** `0.3698`
- **Coeficiente RH:** `-2.3122`

Como os dados foram padronizados, é possível comparar a magnitude dos coeficientes diretamente, confirmando que `AT` é a variável de maior peso no cálculo da previsão.

---

## 4. Avaliação de Desempenho no Conjunto de Teste

Avaliando o modelo nos 20% de dados separados para teste, as métricas obtidas foram:
- **R² (Coeficiente de Determinação):** `0.9301`
- **RMSE (Raiz do Erro Quadrático Médio):** `4.5026 MW`
- **MAE (Erro Médio Absoluto):** `3.5959 MW`

**Justificativa sobre a adequação do modelo:**
O modelo é adequado para prever a produção de energia da usina. O valor de `R² = 0.9301` mostra que cerca de 93% da variação na geração de energia é explicada linearmente pelas quatro variáveis ambientais. Além disso, como a produção da usina gira em torno de 420 MW a 495 MW, um erro médio absoluto de `3.60 MW` (e `4.50 MW` no RMSE) representa uma margem de erro inferior a 1%, o que garante uma boa precisão para estimar a geração elétrica.
