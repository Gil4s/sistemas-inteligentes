# Guia Mestre de Sistemas Inteligentes (PAM0466)
**Docente:** Prof. Dr. Pedro Thiago Valério de Souza  
**Aluno:** Gil | Engenharia / Ciência da Computação (UFERSA - Campus Pau dos Ferros)  
**Objetivo:** Domínio conceitual e prático das Listas de Exercícios (30 Questões) e Projetos (5 Problemas com defesa oral).

---

## Estrutura do Estudo (Cronograma de 4 Dias)

- [x] **Setup do Ambiente:** Python 3.14 + PyTorch + Scikit-Learn + Pandas + NumPy + Matplotlib + Seaborn configurados.
- [ ] **Módulo 1 (Dia 1):** Fundamentos de AM, AED, Pré-Processamento e Python Essencial (Questões 1 a 6).
- [ ] **Módulo 2 (Dia 2):** Regressão Linear, Otimização (Equação Normal vs Gradiente Descendente em PyTorch), Regularização Ridge/Lasso e Projeto 1 (Questões 7 a 12).
- [ ] **Módulo 3 (Dia 3):** Classificação, Regressão Logística, Métricas (Acurácia, Precisão, Recall, F1, ROC/AUC), K-Fold CV, k-NN e Projetos 2 e 3 (Questões 13 a 17).
- [ ] **Módulo 4 (Dia 4):** Árvores de Decisão (Entropia, Gini, Ganho de Informação, Pruning), Clusterização (k-Means, Silhueta, Cotovelo, Hierárquico) e Projetos 4 e 5 (Questões 18 a 30).
- [ ] **Módulo 5 (Dias 5-6):** Implementação e Relatórios `.md` dos 5 Projetos Oficiais.
- [ ] **Módulo 6 (Dia 7):** Simulação de Defesa Oral individual.

---

## Módulo 1: Fundamentos de Aprendizado de Máquina e Pré-Processamento

### 1.1 Paradigmas de Aprendizado (Questões 1 e 2 da Lista Conceitual)
- **Supervisionado:** Dados rotulados $(X, y)$. O modelo aprende a função de mapeamento $f: X \to y$.
  - Tarefas: *Regressão* (saída contínua) e *Classificação* (saída discreta/classes).
  - Exemplos: Detecção de spam (classificação binária), previsão de temperatura ou potência elétrica (regressão).
- **Não Supervisionado:** Dados não rotulados apenas $X$. O algoritmo busca regularidades, agrupamentos ou representações latentes.
  - Tarefas: *Clusterização* (agrupamento), *Redução de Dimensionalidade* (PCA, t-SNE), *Detecção de Anomalias/Outliers*.
  - Exemplo: Segmentação de clientes com base em hábitos de compra.
- **Aprendizado por Reforço (RL):** Um *agente* interage com um *ambiente*, observa o estado, toma ações e recebe recompensas ou penalidades (+/- pontos). O objetivo é aprender uma política ótima $\pi^*$ para maximizar a recompensa acumulada no tempo.
  - Exemplos: Robô andando por terrenos desconhecidos, AlphaGo, controle autônomo de drones.

---
*(Este documento será enriquecido continuamente a cada bloco concluído)*
