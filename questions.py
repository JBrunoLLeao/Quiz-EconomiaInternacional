QUESTIONS = [

    # ══════════════════════════════════════════════════════
    # CNN (Q1–18)
    # ══════════════════════════════════════════════════════
    {
        "topic": "CNN",
        "question": (
            "No código MNIST do slide, a primeira camada Conv2D(32, (3,3)) "
            "recebe entrada (28,28,1) e produz saída (26,26,32). "
            "Por que a dimensão espacial diminuiu de 28 para 26?"
        ),
        "options": [
            "A) Porque o stride padrão é 2",
            "B) Porque o padding padrão é 'valid', e um filtro 3×3 sem padding reduz cada dimensão em 2",
            "C) Porque o max-pooling é aplicado automaticamente após cada convolução",
            "D) Porque o ReLU remove as bordas da imagem",
        ],
        "answer": "B) Porque o padding padrão é 'valid', e um filtro 3×3 sem padding reduz cada dimensão em 2",
        "explanation": (
            "Com padding='valid' (padrão no Keras), o filtro só é aplicado onde "
            "cabe inteiramente dentro da entrada. Para um filtro 3×3, perde-se "
            "1 pixel em cada lado → 28 - 3 + 1 = 26. Nenhum pooling ou ReLU "
            "afeta dimensões espaciais dessa forma."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "No summary do modelo MNIST, a camada Conv2D(64, (3,3)) após "
            "MaxPooling2D tem 18.496 parâmetros. Como esse número é obtido?"
        ),
        "options": [
            "A) 64 filtros × (3×3 pesos × 1 canal) + 64 bias = 640",
            "B) 64 filtros × (3×3 pesos × 32 canais) + 64 bias = 18.496",
            "C) 64 filtros × (3×3 pesos × 64 canais) + 64 bias = 36.928",
            "D) 32 filtros × (3×3 pesos × 64 canais) + 32 bias = 18.464",
        ],
        "answer": "B) 64 filtros × (3×3 pesos × 32 canais) + 64 bias = 18.496",
        "explanation": (
            "A camada anterior produz 32 mapas de características (canais). "
            "Cada filtro da nova camada tem dimensão 3×3×32 = 288 pesos, "
            "mais 1 bias = 289. Com 64 filtros: 289 × 64 = 18.496. "
            "Esse é exatamente o valor mostrado no model.summary() do slide."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide afirma que 'Dense layers → global patterns' e "
            "'Convolution layers → local patterns'. "
            "Qual propriedade das ConvNets garante isso?"
        ),
        "options": [
            "A) O uso de max-pooling que seleciona apenas o maior valor de cada região",
            "B) O compartilhamento de pesos (weight sharing): o mesmo filtro é aplicado em todas as posições da imagem",
            "C) O uso de ReLU que remove valores negativos",
            "D) O flattening que transforma a imagem em vetor antes da classificação",
        ],
        "answer": "B) O compartilhamento de pesos (weight sharing): o mesmo filtro é aplicado em todas as posições da imagem",
        "explanation": (
            "Em camadas convolucionais, cada filtro desliza sobre toda a imagem "
            "aplicando a mesma operação local. Isso cria detectores de padrões "
            "locais (bordas, texturas) que funcionam em qualquer posição. "
            "Camadas densas conectam cada neurônio a todos os pixels, aprendendo "
            "padrões globais mas sem invariância à translação."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide menciona 'Translation invariance' como propriedade das ConvNets. "
            "O que isso significa na prática?"
        ),
        "options": [
            "A) A rede consegue classificar imagens traduzidas para outros idiomas",
            "B) Um padrão aprendido em uma posição da imagem pode ser reconhecido em qualquer outra posição",
            "C) A rede é invariante ao número de classes do problema",
            "D) Os filtros são transladados para diferentes camadas durante o treinamento",
        ],
        "answer": "B) Um padrão aprendido em uma posição da imagem pode ser reconhecido em qualquer outra posição",
        "explanation": (
            "Como os mesmos pesos (filtro) são aplicados em todas as posições espaciais, "
            "um detector de orelha de gato aprende independente de onde a orelha "
            "aparece na imagem. Isso é diferente de uma camada densa, onde a posição "
            "do pixel importa diretamente para o peso aplicado."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide compara usar Max Pooling vs. não usar Max Pooling no MNIST. "
            "Sem max pooling, o mapa final é 22×22×64 = 30.976 coeficientes. "
            "Qual é o principal problema disso?"
        ),
        "options": [
            "A) Aumenta o risco de vanishing gradient nas camadas convolucionais",
            "B) Não há hierarquia espacial de features e há muito mais coeficientes para processar",
            "C) O ReLU não consegue operar sobre mapas muito grandes",
            "D) O modelo fica com menos parâmetros treináveis do que o necessário",
        ],
        "answer": "B) Não há hierarquia espacial de features e há muito mais coeficientes para processar",
        "explanation": (
            "Conforme o slide: sem pooling (1) não há hierarquia espacial — "
            "camadas mais profundas não 'veem' janelas progressivamente maiores "
            "da imagem original, e (2) o mapa final 22×22×64 tem 30.976 coeficientes "
            "vs. o modelo com pooling que produz 3×3×64 = 576 antes do flatten, "
            "muito mais eficiente."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "Por que o slide recomenda Max Pooling em vez de Average Pooling?"
        ),
        "options": [
            "A) Porque o Max Pooling tem menos parâmetros treináveis",
            "B) Porque features tendem a codificar a presença de padrões, e a presença máxima é mais informativa que a média",
            "C) Porque Average Pooling causa overfitting mais facilmente",
            "D) Porque Max Pooling preserva as dimensões espaciais da entrada",
        ],
        "answer": "B) Porque features tendem a codificar a presença de padrões, e a presença máxima é mais informativa que a média",
        "explanation": (
            "O slide cita explicitamente: 'Features tend to encode the spatial "
            "presence of some pattern' e 'it's more informative to look at the "
            "maximal presence of different features than at their average presence'. "
            "Se um olho de gato aparece em algum lugar da janela 2×2, o max captura isso; "
            "a média pode diluir o sinal."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "No problema Dogs vs. Cats com apenas 2000 imagens de treino, "
            "qual é o principal obstáculo esperado segundo o slide?"
        ),
        "options": [
            "A) Underfitting, pois a rede não tem capacidade suficiente",
            "B) Overfitting, pois o modelo memoriza o conjunto de treino pequeno",
            "C) Vanishing gradient, pois imagens de cães e gatos são muito similares",
            "D) Exploding gradient, pois as imagens coloridas têm valores altos",
        ],
        "answer": "B) Overfitting, pois o modelo memoriza o conjunto de treino pequeno",
        "explanation": (
            "O slide afirma: 'On a small dataset, overfitting will be the main issue'. "
            "Com poucas amostras, redes com muitos parâmetros tendem a memorizar "
            "nuances do treino em vez de aprender padrões generalizáveis. "
            "É exatamente por isso que técnicas como data augmentation e "
            "transfer learning são introduzidas na sequência."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide descreve Data Augmentation com rotação, shift, shear, zoom e flip. "
            "Qual é o papel desta técnica no contexto de generalização?"
        ),
        "options": [
            "A) Aumenta o número de parâmetros da rede para aprender mais padrões",
            "B) Gera variações artificiais das imagens existentes para que o modelo aprenda invariâncias e reduza overfitting",
            "C) Substitui completamente a necessidade de regularização L2",
            "D) Acelera o treinamento ao reduzir o tamanho de cada imagem",
        ],
        "answer": "B) Gera variações artificiais das imagens existentes para que o modelo aprenda invariâncias e reduza overfitting",
        "explanation": (
            "Data augmentation cria novas amostras por transformações que preservam "
            "a classe (um gato rotacionado ainda é um gato). Isso expande efetivamente "
            "o dataset e ensina a rede que essas transformações não mudam o rótulo, "
            "reduzindo overfitting sem coletar mais dados reais."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "No Transfer Learning com VGG16, o código usa include_top=False. "
            "O que isso faz e por quê?"
        ),
        "options": [
            "A) Remove as camadas de convolução e mantém apenas o classificador denso",
            "B) Remove as camadas densas finais (classificador) e mantém apenas a base convolucional para extração de features",
            "C) Descongela todas as camadas para fine-tuning imediato",
            "D) Reduz a resolução de entrada de 224×224 para 150×150",
        ],
        "answer": "B) Remove as camadas densas finais (classificador) e mantém apenas a base convolucional para extração de features",
        "explanation": (
            "include_top=False exclui as 3 camadas densas originais do VGG16 "
            "(treinadas para 1000 classes do ImageNet). Mantém apenas a base "
            "convolucional (14,7M parâmetros) como extrator de features. "
            "Depois adicionamos nosso próprio classificador (Flatten + Dense) "
            "para o novo problema (cães vs. gatos)."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "Ao fazer Transfer Learning com conv_base.trainable = False, "
            "qual é o efeito no treinamento?"
        ),
        "options": [
            "A) A base convolucional não recebe gradientes, apenas o classificador no topo é atualizado",
            "B) Todo o modelo para de treinar para evitar overfitting",
            "C) Os pesos da base são zerados antes do treinamento começar",
            "D) O learning rate é automaticamente reduzido para evitar destruir os pesos",
        ],
        "answer": "A) A base convolucional não recebe gradientes, apenas o classificador no topo é atualizado",
        "explanation": (
            "O slide mostra que após conv_base.trainable = False, o número de "
            "'trainable weights' cai drasticamente. Os 14,7M de parâmetros da "
            "base VGG16 ficam congelados (frozen), e o backprop atualiza apenas "
            "os pesos do Flatten+Dense adicionados. Isso evita destruir as "
            "representações aprendidas no ImageNet."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide descreve Fine-Tuning como descongelar apenas as últimas camadas "
            "da base convolucional (block5_conv1 em diante). "
            "Por que não descongelar as primeiras camadas também?"
        ),
        "options": [
            "A) As primeiras camadas têm mais parâmetros e treinam muito mais rápido",
            "B) Camadas iniciais aprendem features genéricas e reutilizáveis (bordas, texturas), enquanto camadas finais são mais especializadas e precisam ser adaptadas ao novo domínio",
            "C) As primeiras camadas do VGG16 usam ativações incompatíveis com o novo problema",
            "D) Descongelar camadas iniciais aumentaria o overfitting pois elas têm mais neurônios",
        ],
        "answer": "B) Camadas iniciais aprendem features genéricas e reutilizáveis (bordas, texturas), enquanto camadas finais são mais especializadas e precisam ser adaptadas ao novo domínio",
        "explanation": (
            "O slide afirma: 'Earlier layers = more-generic, reusable features' e "
            "'higher layers = more-specialized features'. Bordas e texturas são "
            "úteis para qualquer tarefa de visão. Features especializadas em "
            "classes do ImageNet precisam ser ajustadas para o novo problema. "
            "Além disso, treinar mais parâmetros aumenta o risco de overfitting "
            "com datasets pequenos."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide mostra que filtros das camadas iniciais (block1_conv1) detectam "
            "bordas direcionais, enquanto filtros de camadas mais profundas detectam "
            "texturas complexas. O que isso revela sobre a hierarquia das ConvNets?"
        ),
        "options": [
            "A) Camadas profundas processam informações mais rápido por terem menos parâmetros",
            "B) A rede aprende uma hierarquia progressiva: features simples (bordas) nas camadas iniciais são combinadas em features complexas (partes de objetos) nas camadas finais",
            "C) Apenas as camadas finais são úteis para classificação; as iniciais são redundantes",
            "D) Camadas iniciais aprendem cores e camadas finais aprendem formas geométricas básicas",
        ],
        "answer": "B) A rede aprende uma hierarquia progressiva: features simples (bordas) nas camadas iniciais são combinadas em features complexas (partes de objetos) nas camadas finais",
        "explanation": (
            "O slide descreve explicitamente essa hierarquia: 'First layer → edge "
            "detectors', camadas médias detectam texturas, camadas finais detectam "
            "conceitos como 'orelha de gato' ou 'olho de gato'. Isso é o que o "
            "slide chama de 'Deep Neural Network: Information distillation pipeline'."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O slide menciona que nas camadas mais profundas 'sparsity increases': "
            "mais filtros ficam em branco (não ativados). O que isso indica?"
        ),
        "options": [
            "A) A rede está sofrendo vanishing gradient nas camadas finais",
            "B) Filtros profundos são especializados: só ativam quando seu padrão específico está presente na imagem",
            "C) O dropout está removendo neurônios aleatoriamente nas camadas finais",
            "D) O max-pooling elimina as ativações menores, deixando apenas os valores máximos",
        ],
        "answer": "B) Filtros profundos são especializados: só ativam quando seu padrão específico está presente na imagem",
        "explanation": (
            "O slide afirma: 'in the first layer, all filters are activated by the "
            "input image; but in the following layers, more and more filters are blank'. "
            "Um filtro de 'orelha de gato' só ativa se uma orelha de gato aparecer "
            "na imagem. Isso é a especialização progressiva da hierarquia de features."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "O que é Grad-CAM e qual problema ele resolve no contexto das ConvNets?"
        ),
        "options": [
            "A) É uma técnica de regularização que aplica gradientes para reduzir overfitting",
            "B) É um método de visualização que gera heatmaps indicando quais regiões da imagem mais influenciaram a predição de uma classe",
            "C) É um otimizador baseado em gradientes adaptativos para treinar ConvNets mais rapidamente",
            "D) É uma técnica para inicializar os filtros das ConvNets usando gradientes do dataset",
        ],
        "answer": "B) É um método de visualização que gera heatmaps indicando quais regiões da imagem mais influenciaram a predição de uma classe",
        "explanation": (
            "O slide mostra o Grad-CAM (Gradient-weighted Class Activation Mapping): "
            "calcula gradientes da saída de uma classe em relação à última camada "
            "convolucional, produzindo um mapa de calor. No exemplo do elefante, "
            "responde 'Por que a rede classificou como elefante africano?' e "
            "'Onde está o elefante na imagem?'."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "Por que o slide afirma que 'ConvNets are the opposite of black boxes'?"
        ),
        "options": [
            "A) Porque ConvNets têm menos parâmetros que redes densas e são mais simples de entender",
            "B) Porque é possível visualizar o que cada filtro detecta e quais regiões da imagem ativam cada classe, tornando as representações interpretáveis",
            "C) Porque o código fonte das ConvNets é open-source e pode ser auditado",
            "D) Porque ConvNets sempre produzem a mesma predição para a mesma imagem, ao contrário de redes com dropout",
        ],
        "answer": "B) Porque é possível visualizar o que cada filtro detecta e quais regiões da imagem ativam cada classe, tornando as representações interpretáveis",
        "explanation": (
            "O slide lista 3 técnicas de visualização: (1) ativações intermediárias, "
            "(2) visualização de filtros, e (3) heatmaps de ativação de classe (Grad-CAM). "
            "Essas técnicas permitem entender o que cada parte da rede aprendeu, "
            "algo impossível em modelos verdadeiramente caixa-preta."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "No slide de Transfer Learning, o learning rate usado no fine-tuning "
            "(1e-5) é muito menor que o usado no treinamento do classificador (2e-5). "
            "Por que usar um learning rate tão baixo no fine-tuning?"
        ),
        "options": [
            "A) Para compensar o maior número de parâmetros treináveis durante o fine-tuning",
            "B) Para evitar destruir as representações já aprendidas na base convolucional com atualizações muito grandes",
            "C) Porque o fine-tuning usa um otimizador diferente que requer taxas menores",
            "D) Para garantir que apenas as últimas camadas sejam atualizadas, ignorando as primeiras",
        ],
        "answer": "B) Para evitar destruir as representações já aprendidas na base convolucional com atualizações muito grandes",
        "explanation": (
            "Os pesos da base VGG16 foram cuidadosamente treinados no ImageNet. "
            "Um LR alto poderia modificar drasticamente esses pesos em poucos steps, "
            "destruindo representações valiosas. O LR muito baixo permite ajustes "
            "sutis para o novo domínio sem perder o conhecimento pré-treinado."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "Uma Siamese Network usa duas redes com pesos compartilhados para "
            "comparar duas entradas. Para que tipo de tarefa essa arquitetura é "
            "especialmente útil?"
        ),
        "options": [
            "A) Classificação multiclasse com muitas categorias bem definidas",
            "B) Verificação de similaridade entre pares de imagens, como reconhecimento facial com poucos exemplos por pessoa (few-shot learning)",
            "C) Detecção de objetos em tempo real em vídeos",
            "D) Segmentação semântica pixel a pixel de imagens médicas",
        ],
        "answer": "B) Verificação de similaridade entre pares de imagens, como reconhecimento facial com poucos exemplos por pessoa (few-shot learning)",
        "explanation": (
            "Siamese Networks aprendem uma função de distância/similaridade entre "
            "entradas. Como os pesos são compartilhados, ambas as redes extraem "
            "embeddings no mesmo espaço. É ideal quando há poucas amostras por "
            "classe (few-shot) pois aprende 'quão similares são duas imagens' em "
            "vez de aprender N classificadores separados. Usada em verificação facial "
            "e assinatura de documentos."
        ),
    },
    {
        "topic": "CNN",
        "question": (
            "Uma ResNet (Residual Network) usa conexões residuais (skip connections) "
            "da forma: saída = F(x) + x. Qual problema de treinamento essa "
            "arquitetura resolve?"
        ),
        "options": [
            "A) Overfitting em datasets pequenos, pois reduz o número de parâmetros",
            "B) O problema de vanishing gradient em redes muito profundas, pois o gradiente pode fluir diretamente pelo caminho residual sem desaparecer",
            "C) A necessidade de data augmentation, pois a skip connection já introduz variações nos dados",
            "D) O tempo de inferência, pois as skip connections permitem pular camadas durante a predição",
        ],
        "answer": "B) O problema de vanishing gradient em redes muito profundas, pois o gradiente pode fluir diretamente pelo caminho residual sem desaparecer",
        "explanation": (
            "Em redes muito profundas, os gradientes podem se tornar tão pequenos "
            "que as camadas iniciais param de aprender (vanishing gradient). "
            "A conexão residual x + F(x) cria um 'atalho' pelo qual o gradiente "
            "flui diretamente para camadas anteriores. Isso permitiu treinar redes "
            "com mais de 100 camadas (ResNet-152), algo impraticável sem skip connections."
        ),
    },

    # ══════════════════════════════════════════════════════
    # RNN (Q19–36)
    # ══════════════════════════════════════════════════════
    {
        "topic": "RNN",
        "question": (
            "O slide mostra a fórmula da RNN: a⟨t⟩ = tanh(W_ax·x⟨t⟩ + W_aa·a⟨t-1⟩ + b_a). "
            "O que representa o termo W_aa·a⟨t-1⟩?"
        ),
        "options": [
            "A) A entrada atual multiplicada pela matriz de pesos de entrada",
            "B) O estado oculto do passo anterior multiplicado pela matriz de pesos recorrentes, permitindo que informação de passos anteriores influencie o passo atual",
            "C) O bias da camada, que é atualizado a cada passo de tempo",
            "D) A predição do passo anterior que é realimentada como nova entrada",
        ],
        "answer": "B) O estado oculto do passo anterior multiplicado pela matriz de pesos recorrentes, permitindo que informação de passos anteriores influencie o passo atual",
        "explanation": (
            "W_aa é a matriz de pesos recorrentes (hidden-to-hidden). "
            "Ela transforma o estado oculto a⟨t-1⟩ do passo anterior e o "
            "adiciona à contribuição da entrada atual (W_ax·x⟨t⟩). "
            "É esse mecanismo que dá à RNN a capacidade de 'lembrar' contexto "
            "de passos anteriores, essencial para dados sequenciais."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide mostra que a RNN é conectada ao longo do tempo como células "
            "encadeadas: a⟨0⟩ → RNN-cell → a⟨1⟩ → RNN-cell → ... "
            "O que acontece com a⟨0⟩ geralmente na prática?"
        ),
        "options": [
            "A) É calculado como a média de todas as entradas da sequência",
            "B) É inicializado como vetor de zeros",
            "C) É o vetor de bias da primeira camada",
            "D) É copiado da saída da última célula da sequência anterior",
        ],
        "answer": "B) É inicializado como vetor de zeros",
        "explanation": (
            "O estado inicial a⟨0⟩ representa o 'contexto' antes de ver qualquer "
            "entrada. Como não há informação anterior, a convenção padrão é "
            "inicializá-lo com zeros. Em algumas arquiteturas avançadas, a⟨0⟩ "
            "pode ser aprendido ou inicializado com informações do problema, "
            "mas zeros é o padrão mais comum."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide destaca que RNNs capturam 'dynamic information in sequential "
            "data' e mantêm um 'context state'. "
            "Por que uma rede densa (MLP) não seria adequada para processar sequências?"
        ),
        "options": [
            "A) Porque MLPs não conseguem usar a função de ativação tanh",
            "B) Porque MLPs têm entrada de tamanho fixo e não compartilham pesos ao longo do tempo, não capturando dependências temporais naturalmente",
            "C) Porque MLPs são muito rápidas e não permitem processar tokens um a um",
            "D) Porque MLPs exigem que todos os dados estejam normalizados, o que é difícil em sequências",
        ],
        "answer": "B) Porque MLPs têm entrada de tamanho fixo e não compartilham pesos ao longo do tempo, não capturando dependências temporais naturalmente",
        "explanation": (
            "Um MLP exige tamanho de entrada fixo e trata cada posição "
            "independentemente com pesos distintos. Não há mecanismo para "
            "passar informação de t para t+1. A RNN resolve isso com o estado "
            "recorrente a⟨t⟩ que acumula contexto ao longo da sequência, "
            "e com weight sharing (W_aa, W_ax compartilhados em todos os steps)."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "Na equação de saída do slide: ŷ⟨t⟩ = softmax(W_ya·a⟨t⟩ + b_y). "
            "O que acontece se quisermos classificar uma sequência inteira "
            "(ex: análise de sentimento de uma frase), em vez de produzir "
            "uma saída por passo de tempo?"
        ),
        "options": [
            "A) Usamos apenas ŷ⟨1⟩ como resultado final, pois é o estado mais informativo",
            "B) Usamos apenas ŷ⟨Tx⟩ (saída do último passo), pois o estado oculto final acumula toda a informação da sequência",
            "C) Somamos todas as saídas ŷ⟨t⟩ de cada passo de tempo",
            "D) Calculamos ŷ na camada de entrada, antes do processamento recorrente",
        ],
        "answer": "B) Usamos apenas ŷ⟨Tx⟩ (saída do último passo), pois o estado oculto final acumula toda a informação da sequência",
        "explanation": (
            "Para tarefas many-to-one (sequência → classe), o estado oculto "
            "a⟨Tx⟩ do último passo encapsula o contexto de toda a sequência. "
            "Passamos apenas esse estado final para o classificador. "
            "Isso contrasta com tarefas many-to-many (ex: NER, tradução) "
            "onde cada ŷ⟨t⟩ é usado."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide mostra o gradiente ∂J/∂a⟨t-1⟩ = (∂J/∂a⟨t⟩) · (∂a⟨t⟩/∂a⟨t-1⟩). "
            "O que é o 'Vanishing Gradient Problem' que afeta RNNs básicas?"
        ),
        "options": [
            "A) O gradiente explode para valores muito grandes ao longo do tempo",
            "B) O gradiente se multiplica por W_aa em cada passo de tempo; se os valores singulares de W_aa são < 1, o gradiente encolhe exponencialmente e as dependências de longo prazo não são aprendidas",
            "C) A função tanh satura e produz gradientes sempre iguais a zero",
            "D) O bias b_a acumula gradientes muito grandes e desestabiliza o treinamento",
        ],
        "answer": "B) O gradiente se multiplica por W_aa em cada passo de tempo; se os valores singulares de W_aa são < 1, o gradiente encolhe exponencialmente e as dependências de longo prazo não são aprendidas",
        "explanation": (
            "O BPTT propaga ∂J/∂a⟨1⟩ multiplicando repetidamente pela Jacobiana "
            "∂a⟨t⟩/∂a⟨t-1⟩ = W_aa^T · diag(1-tanh²(·)). "
            "Se os valores singulares de W_aa < 1, após T multiplicações o "
            "gradiente → 0, e a rede não consegue aprender que, por exemplo, "
            "o sujeito no início da frase determina a conjugação do verbo no final."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide mostra a célula LSTM com forget gate Γ_f, update gate Γ_u "
            "e output gate Γ_o. "
            "Qual é a principal vantagem do LSTM sobre a RNN básica (Elman)?"
        ),
        "options": [
            "A) O LSTM tem menos parâmetros e treina mais rapidamente",
            "B) O LSTM introduz o estado de célula c⟨t⟩, que permite que informação flua por longos períodos sem ser modificada, mitigando o vanishing gradient",
            "C) O LSTM usa a função sigmoid em vez de tanh, o que evita saturação",
            "D) O LSTM processa a sequência em paralelo, ao contrário da RNN que é sequencial",
        ],
        "answer": "B) O LSTM introduz o estado de célula c⟨t⟩, que permite que informação flua por longos períodos sem ser modificada, mitigando o vanishing gradient",
        "explanation": (
            "A inovação central do LSTM é o cell state c⟨t⟩ e os gates. "
            "A equação c⟨t⟩ = Γ_f ⊙ c⟨t-1⟩ + Γ_u ⊙ c̃⟨t⟩ permite que "
            "informações antigas sejam preservadas (se Γ_f ≈ 1) sem passar "
            "por multiplicações repetidas que causariam vanishing gradient. "
            "O gradiente flui pelo 'highway' do cell state quase sem atenuação."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "No LSTM do slide: c⟨t⟩ = Γ_f⟨t⟩ ⊙ c⟨t-1⟩ + Γ_u⟨t⟩ ⊙ c̃⟨t⟩. "
            "O que acontece quando o forget gate Γ_f⟨t⟩ ≈ 0?"
        ),
        "options": [
            "A) O estado da célula anterior é completamente preservado",
            "B) O estado da célula anterior é apagado, e apenas a nova informação c̃⟨t⟩ contribui para c⟨t⟩",
            "C) A nova informação c̃⟨t⟩ é bloqueada e o estado anterior é mantido intacto",
            "D) O output gate fecha automaticamente, zerando a saída do LSTM",
        ],
        "answer": "B) O estado da célula anterior é apagado, e apenas a nova informação c̃⟨t⟩ contribui para c⟨t⟩",
        "explanation": (
            "Γ_f⟨t⟩ ≈ 0 → Γ_f ⊙ c⟨t-1⟩ ≈ 0, então c⟨t⟩ ≈ Γ_u ⊙ c̃⟨t⟩. "
            "A memória anterior é 'esquecida'. Note a aparente confusão de nome: "
            "forget gate = 0 significa 'esqueça tudo'. "
            "Isso ocorre quando o LSTM detecta uma mudança de contexto, "
            "como o início de uma nova frase."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide mostra que a⟨t⟩ = Γ_o⟨t⟩ ⊙ tanh(c⟨t⟩). "
            "Qual é o papel do output gate Γ_o⟨t⟩ nesta equação?"
        ),
        "options": [
            "A) Decide quanta informação nova deve ser escrita no cell state",
            "B) Controla quanta informação do cell state c⟨t⟩ é exposta como estado oculto a⟨t⟩ para a saída e próxima célula",
            "C) Determina se o forget gate deve ser ativado no próximo passo",
            "D) Escala o learning rate para o passo de tempo atual",
        ],
        "answer": "B) Controla quanta informação do cell state c⟨t⟩ é exposta como estado oculto a⟨t⟩ para a saída e próxima célula",
        "explanation": (
            "O cell state c⟨t⟩ pode conter muita informação acumulada. "
            "O output gate Γ_o age como um filtro: decide o que do c⟨t⟩ "
            "deve ser exposto como saída a⟨t⟩ neste momento. "
            "Por exemplo, o LSTM pode saber o gênero do sujeito desde o início "
            "da frase mas só revelar essa informação quando necessário para "
            "gerar a palavra correta."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide menciona que RNNs capturam contexto em 'context windows of "
            "any length'. Porém, na prática, qual limitação afeta "
            "o aprendizado de dependências muito longas em RNNs simples?"
        ),
        "options": [
            "A) RNNs simples têm um limite fixo de 100 passos de tempo definido no Keras",
            "B) O vanishing gradient faz com que o sinal de erro de passos muito distantes se torne negligenciável, impedindo que a rede aprenda dependências de longo prazo",
            "C) O max-pooling nas camadas anteriores remove informações temporais",
            "D) O softmax na saída normaliza as probabilidades e apaga o contexto anterior",
        ],
        "answer": "B) O vanishing gradient faz com que o sinal de erro de passos muito distantes se torne negligenciável, impedindo que a rede aprenda dependências de longo prazo",
        "explanation": (
            "Embora teoricamente a RNN possa propagar informação por qualquer "
            "número de passos, na prática o BPTT multiplica os gradientes por "
            "W_aa repetidamente. Com W_aa pequeno, o gradiente de passos distantes "
            "vira efetivamente zero. Por isso LSTMs e GRUs foram criados: "
            "para aprender dependências de longo prazo de forma mais confiável."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide lista vídeo, áudio e frases como exemplos de sequências "
            "processadas por RNNs. "
            "Para uma tarefa de tradução automática (ex: Português → Inglês), "
            "qual arquitetura de RNN seria mais adequada?"
        ),
        "options": [
            "A) Many-to-one: a frase em português entra e apenas a última palavra em inglês é gerada",
            "B) One-to-many: uma única representação entra e uma sequência em inglês é gerada",
            "C) Many-to-many com tamanhos diferentes (encoder-decoder): a sequência em português é codificada e depois decodificada para inglês",
            "D) One-to-one: cada palavra em português é traduzida independentemente para inglês",
        ],
        "answer": "C) Many-to-many com tamanhos diferentes (encoder-decoder): a sequência em português é codificada e depois decodificada para inglês",
        "explanation": (
            "Tradução é many-to-many assimétrico: frases de comprimentos diferentes "
            "em idiomas diferentes. A arquitetura seq2seq usa um encoder RNN "
            "que comprime a frase de entrada em um vetor de contexto, e um "
            "decoder RNN que gera a tradução token a token. "
            "Esse design permite lidar com sequências de comprimentos arbitrários."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "No cache da célula RNN do slide: cache = (a⟨t⟩, a⟨t-1⟩, x⟨t⟩, parameters). "
            "Por que é necessário armazenar a⟨t-1⟩ durante o forward pass?"
        ),
        "options": [
            "A) Para calcular a predição ŷ⟨t⟩ na saída",
            "B) Porque o backpropagation through time (BPTT) precisará de a⟨t-1⟩ para calcular o gradiente ∂J/∂a⟨t-1⟩ durante a fase de retropropagação",
            "C) Para normalizar o estado oculto atual antes de passá-lo para a próxima célula",
            "D) Para calcular o forget gate no LSTM que depende do estado anterior",
        ],
        "answer": "B) Porque o backpropagation through time (BPTT) precisará de a⟨t-1⟩ para calcular o gradiente ∂J/∂a⟨t-1⟩ durante a fase de retropropagação",
        "explanation": (
            "O slide mostra que ∂J/∂a⟨t-1⟩ = (∂J/∂a⟨t⟩) · (∂a⟨t⟩/∂a⟨t-1⟩). "
            "Para calcular ∂a⟨t⟩/∂a⟨t-1⟩ = W_aa^T · (1 - tanh²(·)), precisamos "
            "dos valores intermediários do forward pass. "
            "Por isso todos os estados devem ser armazenados durante o forward "
            "para uso no backward — é o custo de memória O(T) do BPTT."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "Qual das seguintes aplicações práticas é um exemplo de tarefa "
            "'many-to-one' para RNNs?"
        ),
        "options": [
            "A) Geração de música: a rede produz uma sequência de notas",
            "B) Análise de sentimento: uma sequência de palavras entra e a rede produz 'positivo' ou 'negativo'",
            "C) Tradução automática: uma frase em um idioma é traduzida para outro",
            "D) Reconhecimento de voz: um áudio é transcrito palavra por palavra",
        ],
        "answer": "B) Análise de sentimento: uma sequência de palavras entra e a rede produz 'positivo' ou 'negativo'",
        "explanation": (
            "Many-to-one: a RNN processa uma sequência inteira (palavras da frase) "
            "e produz uma única saída (classificação de sentimento) usando o "
            "estado oculto final. Geração de música é one-to-many, tradução é "
            "many-to-many assimétrico, e reconhecimento de voz é many-to-many."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide destaca que hidden layers 'in current and next moment are related' "
            "na RNN. Qual é a consequência disso para o treinamento em comparação "
            "com um MLP treinado com backpropagation padrão?"
        ),
        "options": [
            "A) A RNN usa um otimizador diferente (SGD em vez de Adam)",
            "B) O backpropagation na RNN deve percorrer os passos de tempo de trás para frente (BPTT), acumulando gradientes ao longo do tempo",
            "C) A RNN não requer backpropagation, pois os estados recorrentes já corrigem os pesos automaticamente",
            "D) Os gradientes na RNN são calculados apenas para o último passo de tempo",
        ],
        "answer": "B) O backpropagation na RNN deve percorrer os passos de tempo de trás para frente (BPTT), acumulando gradientes ao longo do tempo",
        "explanation": (
            "O slide mostra o grafo de computação da RNN ao longo do tempo. "
            "Como os mesmos pesos W são usados em cada step, o gradiente de J "
            "em relação a W é a soma das contribuições de todos os passos: "
            "∂J/∂W = Σ_t (∂J_t/∂W). O BPTT unrola a sequência e propaga "
            "os gradientes do último passo até o primeiro."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "O slide mostra que no LSTM, Γ_f, Γ_u, Γ_o são calculados com sigmoid σ, "
            "enquanto c̃⟨t⟩ usa tanh. Por que os gates usam sigmoid e não tanh?"
        ),
        "options": [
            "A) Sigmoid é mais rápida de calcular do que tanh em GPUs",
            "B) Sigmoid produz valores entre 0 e 1, funcionando como uma 'porta' que controla quanto de uma informação passa (0 = bloqueia, 1 = deixa passar totalmente)",
            "C) Tanh produziria gradientes negativos, que são indesejados nos gates",
            "D) Sigmoid é usada nos gates para manter a compatibilidade com a função de perda cross-entropy",
        ],
        "answer": "B) Sigmoid produz valores entre 0 e 1, funcionando como uma 'porta' que controla quanto de uma informação passa (0 = bloqueia, 1 = deixa passar totalmente)",
        "explanation": (
            "Gates são mecanismos de controle: precisam de valores em [0,1] "
            "para funcionar como multiplicação seletiva (⊙). "
            "Sigmoid(x) ∈ (0,1) permite interpretação como 'proporção de passagem'. "
            "Já c̃⟨t⟩ representa o candidato a nova informação, onde valores "
            "negativos (tanh ∈ (-1,1)) são válidos e representam 'desativar' "
            "uma feature que estava ativa."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "Por que o slide afirma que RNNs se estendem 'in space and time sequences'? "
            "O que significa a dimensão 'espaço' neste contexto?"
        ),
        "options": [
            "A) Que a RNN pode processar imagens além de sequências temporais",
            "B) Que além de se estender ao longo do tempo (passos t), a RNN pode ser empilhada em múltiplas camadas (profundidade), criando uma rede recorrente profunda",
            "C) Que a RNN usa coordenadas espaciais para localizar padrões em vídeos",
            "D) Que os estados ocultos são organizados em uma grade 2D para capturar contexto espacial",
        ],
        "answer": "B) Que além de se estender ao longo do tempo (passos t), a RNN pode ser empilhada em múltiplas camadas (profundidade), criando uma rede recorrente profunda",
        "explanation": (
            "RNNs empilhadas (stacked RNNs) têm múltiplas camadas recorrentes, "
            "onde a saída a⟨t⟩ de uma camada alimenta a próxima camada como entrada. "
            "Isso cria hierarquia tanto temporal (ao longo de t) quanto espacial "
            "(ao longo das camadas), permitindo aprender representações mais abstratas "
            "das sequências."
        ),
    },
    {
        "topic": "RNN",
        "question": (
            "Considerando a arquitetura LSTM encadeada mostrada no slide, "
            "quais são os dois estados que passam de uma célula para a próxima?"
        ),
        "options": [
            "A) O vetor de entrada x⟨t⟩ e o vetor de bias b_a",
            "B) O cell state c⟨t⟩ e o hidden state a⟨t⟩",
            "C) O forget gate Γ_f e o update gate Γ_u",
            "D) A predição ŷ⟨t⟩ e o cell state c⟨t⟩",
        ],
        "answer": "B) O cell state c⟨t⟩ e o hidden state a⟨t⟩",
        "explanation": (
            "O diagrama de LSTM encadeado do slide mostra claramente duas 'linhas' "
            "conectando células consecutivas: c⟨t-1⟩ → c⟨t⟩ (cell state, a 'memória "
            "de longo prazo') e a⟨t-1⟩ → a⟨t⟩ (hidden state, a 'memória de curto "
            "prazo'). A RNN simples passa apenas a⟨t⟩; é o cell state extra que "
            "dá ao LSTM sua capacidade de longo prazo."
        ),
    },

    # ══════════════════════════════════════════════════════
    # Regularização (Q37–50)
    # ══════════════════════════════════════════════════════
    {
        "topic": "Regularização",
        "question": (
            "O slide define: E[MSE] = Bias² + Variance + Noise. "
            "Qual componente dessa equação NÃO pode ser reduzido, "
            "mesmo com o modelo perfeito?"
        ),
        "options": [
            "A) Bias², pois modelos complexos sempre terão alguma simplificação",
            "B) Variance, pois dados reais sempre têm variações aleatórias",
            "C) Noise (σ²ε), pois representa variações aleatórias irredutíveis nos dados",
            "D) Bias², pois é impossível estimar a função verdadeira f(x)",
        ],
        "answer": "C) Noise (σ²ε), pois representa variações aleatórias irredutíveis nos dados",
        "explanation": (
            "O slide afirma: 'Cannot do anything about it even if seeded with "
            "knowledge about true model'. O noise σ²ε vem de fatores como "
            "erro humano de rotulação ou sensor defeituoso. "
            "Mesmo o modelo perfeito que aprende f(x) exatamente ainda erra "
            "nessas amostras ruidosas. É o piso mínimo do MSE."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide explica que um modelo polinomial de grau 4 tem menos bias "
            "mas mais variance que um modelo linear. "
            "O que é 'model variance' neste contexto?"
        ),
        "options": [
            "A) A variância dos valores de y no dataset de treino",
            "B) O quanto as predições do modelo mudam quando treinado em diferentes amostras do mesmo problema",
            "C) A diferença entre a predição média e a predição mínima do modelo",
            "D) O número de parâmetros do modelo dividido pelo tamanho do dataset",
        ],
        "answer": "B) O quanto as predições do modelo mudam quando treinado em diferentes amostras do mesmo problema",
        "explanation": (
            "O slide mostra o experimento: amostrar 5 pontos duas vezes e treinar "
            "modelo polinomial → predições de x=2 'wildly varying'. "
            "O modelo linear produz predições muito mais estáveis. "
            "Model variance = sensibilidade do modelo ao dataset de treino "
            "específico. Alto variance indica overfitting às nuances do treino."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide mostra o fluxograma: High Bias? → Bigger network. "
            "High Variance? → More data / Regularization. "
            "Se um modelo tem 95% de acurácia no treino e 70% na validação, "
            "qual é o diagnóstico e a solução recomendada?"
        ),
        "options": [
            "A) Alto bias → usar rede maior com mais camadas e épocas",
            "B) Alta variance (overfitting) → obter mais dados ou aplicar regularização",
            "C) Alto ruído nos dados → coletar um dataset mais limpo",
            "D) Baixo bias e baixa variance → o modelo está pronto, nenhuma ação necessária",
        ],
        "answer": "B) Alta variance (overfitting) → obter mais dados ou aplicar regularização",
        "explanation": (
            "Alta acurácia no treino (95%) + baixa acurácia na validação (70%) "
            "= gap grande = overfitting = alto variance. "
            "O slide indica: 'Get more data (to reduce overfitting)' e "
            "'Apply regularization techniques'. Se a acurácia de treino fosse "
            "também baixa (ex: 70%), seria alto bias, e a solução seria "
            "uma rede maior."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide apresenta L2 regularization adicionando λ·Σw²ᵢ à loss. "
            "Qual é o efeito desta penalidade na regra de atualização dos pesos?"
        ),
        "options": [
            "A) Os pesos são zerados a cada época antes do gradiente ser aplicado",
            "B) A atualização se torna wᵢ ← wᵢ(1 - αλ) - α·∂L/∂wᵢ: o fator (1-αλ) decai o peso antes da atualização por gradiente",
            "C) O learning rate α é multiplicado por λ a cada batch",
            "D) Pesos negativos são zerados automaticamente pela penalidade quadrática",
        ],
        "answer": "B) A atualização se torna wᵢ ← wᵢ(1 - αλ) - α·∂L/∂wᵢ: o fator (1-αλ) decai o peso antes da atualização por gradiente",
        "explanation": (
            "O slide mostra exatamente: 'wi ← wi(1-αλ) - α·∂L/∂wi'. "
            "O termo (1-αλ) ∈ (0,1) é chamado de 'weight decay' e age como "
            "'decay-based forgetting': a cada atualização, pesos são ligeiramente "
            "reduzidos. A menos que um peso receba gradientes grandes e consistentes, "
            "ele tende a zero. Previne memorização do treino."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide afirma: 'L2-regularization with parameter λ is equivalent "
            "to adding Gaussian noise with variance λ to input'. "
            "Qual é a intuição por trás dessa equivalência?"
        ),
        "options": [
            "A) Ruído gaussiano e L2 ambos reduzem o learning rate de forma adaptativa",
            "B) Modelos mais simples (parâmetros menores) são menos afetados pelo ruído; a penalidade L2 força o modelo a ser simples o suficiente para ser robusto ao ruído de entrada",
            "C) Ambos adicionam um termo quadrático à função de perda, tornando-a mais convexa",
            "D) O ruído gaussiano e L2 ambos eliminam features com variância baixa",
        ],
        "answer": "B) Modelos mais simples (parâmetros menores) são menos afetados pelo ruído; a penalidade L2 força o modelo a ser simples o suficiente para ser robusto ao ruído de entrada",
        "explanation": (
            "O slide explica: 'Bad effect of noise will be minimized with simpler "
            "models (smaller parameters)'. Um modelo que depende muito de features "
            "específicas (pesos grandes) é destruído por ruído. L2 força pesos "
            "pequenos → modelo mais robusto. Para regressão linear, pode-se "
            "mostrar matematicamente que as duas formulações são equivalentes."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide descreve L1 regularization com a atualização: wᵢ ← wᵢ - αλsᵢ - α·∂L/∂wᵢ, "
            "onde sᵢ = sign(wᵢ). "
            "Por que L1 tende a produzir pesos exatamente iguais a zero (soluções esparsas)?"
        ),
        "options": [
            "A) Porque sᵢ = ±1 é constante, então o gradiente da penalidade sempre 'empurra' wᵢ em direção a zero com força constante, podendo cruzar e travar em zero",
            "B) Porque L1 penaliza pesos grandes mais severamente que L2",
            "C) Porque o gradiente de |wᵢ| é zero para todos os valores, zerando os pesos",
            "D) Porque αλ > 1 garante que os pesos sempre diminuam a cada passo",
        ],
        "answer": "A) Porque sᵢ = ±1 é constante, então o gradiente da penalidade sempre 'empurra' wᵢ em direção a zero com força constante, podendo cruzar e travar em zero",
        "explanation": (
            "Com L1: -αλ·sign(wᵢ) sempre tem magnitude αλ independente do valor de wᵢ. "
            "Para pesos pequenos, essa força constante pode cruzar zero e 'travar' o "
            "peso lá. Com L2: -αλ·2wᵢ → 0 conforme wᵢ → 0, nunca chegando exatamente a zero. "
            "Por isso L1 gera sparsidade (redes com bordas removidas) e L2 gera "
            "pesos pequenos mas não zero."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide afirma que 'L2-regularization generally provides better "
            "performance' que L1. Em que situação L1 seria preferível?"
        ),
        "options": [
            "A) Quando se deseja interpretabilidade: L1 zera pesos irrelevantes, efetivamente selecionando features e simplificando a rede",
            "B) Quando o dataset é grande, pois L1 escala melhor com o número de amostras",
            "C) Quando o modelo usa ReLU, pois L1 é compatível e L2 não",
            "D) Quando se quer regularização mais forte, pois L1 penaliza mais que L2",
        ],
        "answer": "A) Quando se deseja interpretabilidade: L1 zera pesos irrelevantes, efetivamente selecionando features e simplificando a rede",
        "explanation": (
            "O slide afirma: 'L1-regularization leads to sparse parameter learning. "
            "Zero values of wi can be dropped. Equivalent to dropping edges from "
            "neural network.' Pesos zero eliminam conexões, tornando a rede menor "
            "e mais interpretável. Em redes neurais para NLP isso pode identificar "
            "quais features (palavras, n-gramas) são realmente relevantes."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide descreve Dropout: 'Sample each node in the network with "
            "probability p. Keep only edges for which both ends are included.' "
            "O que acontece com os pesos durante a fase de TESTE (inferência)?"
        ),
        "options": [
            "A) O dropout continua ativo com a mesma probabilidade p do treino",
            "B) Os pesos de saída de cada neurônio são multiplicados por (1-p) para compensar os neurônios que ficavam desativados durante o treino",
            "C) Todos os neurônios são sempre descartados para fazer média dos sub-modelos",
            "D) O modelo seleciona automaticamente a subrede com melhor desempenho no treino",
        ],
        "answer": "B) Os pesos de saída de cada neurônio são multiplicados por (1-p) para compensar os neurônios que ficavam desativados durante o treino",
        "explanation": (
            "O slide chama isso de 'weight scaling inference rule (more common)': "
            "na inferência, usa-se a rede completa mas com pesos multiplicados por "
            "(1-p). Isso é uma aproximação do ensemble: se um neurônio ficava ativo "
            "apenas (1-p) fração do tempo no treino, na inferência sua contribuição "
            "deve ser reduzida proporcionalmente."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide explica que Dropout 'will resist co-adaptation, unless "
            "the features are truly synergistic'. "
            "O que é Feature Co-Adaptation e por que ela é prejudicial?"
        ),
        "options": [
            "A) É quando dois filtros convolucionais detectam o mesmo padrão, desperdiçando capacidade",
            "B) É quando neurônios ajustam seus pesos para depender uns dos outros por ineficiência de treinamento, não por sinergia real, memorando nuances do treino que não generalizam",
            "C) É quando o learning rate se adapta automaticamente às features mais importantes",
            "D) É a tendência dos pesos de camadas adjacentes convergirem para valores similares",
        ],
        "answer": "B) É quando neurônios ajustam seus pesos para depender uns dos outros por ineficiência de treinamento, não por sinergia real, memorando nuances do treino que não generalizam",
        "explanation": (
            "O slide afirma: 'Uninformative dependencies are sensitive to nuances "
            "of specific training data → OVERFITTING'. Co-adaptação ocorre quando "
            "partes da rede treinam em velocidades diferentes, causando que algumas "
            "partes se 'acostumem' às outras em vez de aprender padrões independentes. "
            "Dropout força cada neurônio a ser útil mesmo sem a presença de outros, "
            "criando representações mais robustas."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide recomenda para Dropout: 'Better to use a larger network with "
            "Dropout to enable learning of independent representations'. "
            "Por que usar uma rede MAIOR com Dropout, em vez de uma menor sem Dropout?"
        ),
        "options": [
            "A) Porque redes maiores treinam mais rápido com dropout ativado",
            "B) Porque o dropout efetivamente reduz o tamanho da rede durante o treino; a rede maior compensada pelo dropout tem mais capacidade efetiva que uma rede menor sem regularização",
            "C) Porque dropout só funciona em redes com mais de 1000 neurônios por camada",
            "D) Porque redes menores nunca sofrem de overfitting e não precisam de dropout",
        ],
        "answer": "B) Porque o dropout efetivamente reduz o tamanho da rede durante o treino; a rede maior compensada pelo dropout tem mais capacidade efetiva que uma rede menor sem regularização",
        "explanation": (
            "Se p=0.5 e a rede tem N neurônios, cada forward pass usa ~N/2 neurônios "
            "em média. Para manter a capacidade expressiva suficiente nas subredes "
            "amostradas, a rede maior compensa. Além disso, a rede maior aprende "
            "representações mais redundantes e independentes — exatamente o que "
            "o dropout encoraja."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide descreve Bagging como: amostrar com reposição, treinar k modelos, "
            "e fazer média das predições. "
            "Por que a média reduz a variance em comparação com um único modelo?"
        ),
        "options": [
            "A) A média elimina o bias de cada modelo individual",
            "B) Se os erros dos modelos individuais são independentes, a variância da média de k modelos é reduzida por um fator de k em relação à variância de um modelo único",
            "C) A média aumenta o bias mas reduz o noise irredutível",
            "D) Cada modelo individual tem variance zero quando treinado em bootstrap samples",
        ],
        "answer": "B) Se os erros dos modelos individuais são independentes, a variância da média de k modelos é reduzida por um fator de k em relação à variância de um modelo único",
        "explanation": (
            "Matematicamente: Var(média de k variáveis independentes) = Var(X)/k. "
            "Na prática, os modelos não são completamente independentes (treinados "
            "em subsets do mesmo dataset), então a redução é parcial. O slide nota: "
            "'Predictions will be positively correlated → variance proportional to "
            "level of correlation'. Mas mesmo imperfecto, é melhor que um único modelo."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide afirma que Early Stopping é 'Almost always used'. "
            "Como ele funciona e o que monitora?"
        ),
        "options": [
            "A) Para o treinamento quando o learning rate atinge um valor muito pequeno",
            "B) Monitora o erro de validação durante o treino e para quando o erro de validação começa a aumentar, salvando o modelo do ponto de menor erro de validação",
            "C) Para o treinamento após um número fixo de épocas definido pelo usuário",
            "D) Monitora o erro de treino e para quando ele atinge zero, evitando overfitting",
        ],
        "answer": "B) Monitora o erro de validação durante o treino e para quando o erro de validação começa a aumentar, salvando o modelo do ponto de menor erro de validação",
        "explanation": (
            "O gráfico do slide mostra erro de treino e validação ao longo das épocas. "
            "Inicialmente ambos diminuem. Eventualmente o treino continua melhorando "
            "mas a validação piora (overfitting começa). Early stopping salva o modelo "
            "no ponto mínimo da validação, atuando como regularizador sem modificar "
            "a função de perda."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide descreve Penalizing Hidden Units: L' = L + λ·Σ|hᵢ|, "
            "onde hᵢ são os valores das unidades ocultas. "
            "Qual é o efeito prático de penalizar as ativações (não os pesos)?"
        ),
        "options": [
            "A) Os pesos da rede são forçados a zero, removendo conexões desnecessárias",
            "B) A rede aprende representações esparsas: na maioria dos exemplos, poucos neurônios ficam ativos ao mesmo tempo",
            "C) As ativações são normalizadas automaticamente para ter média zero e variância 1",
            "D) O gradiente explodente é prevenido pois as ativações ficam sempre abaixo de 1",
        ],
        "answer": "B) A rede aprende representações esparsas: na maioria dos exemplos, poucos neurônios ficam ativos ao mesmo tempo",
        "explanation": (
            "Penalizar |hᵢ| encoraja que as ativações sejam zero na maioria dos casos. "
            "Resultado: representações esparsas — cada padrão é representado por "
            "poucos neurônios ativos, similar ao que observamos no córtex visual. "
            "Isso é diferente de penalizar pesos (L1/L2): aqui controlamos "
            "diretamente quão ativas as unidades ficam, não seus pesos."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "O slide descreve Unsupervised Pre-training como inicializar uma "
            "rede usando autoencoders antes do treinamento supervisionado. "
            "Qual é o benefício principal dessa técnica?"
        ),
        "options": [
            "A) Elimina a necessidade de dados rotulados para o treinamento final",
            "B) Inicializa os pesos próximos de uma boa região do espaço de parâmetros (perto do ótimo global), melhorando convergência e atuando como regularizador",
            "C) Garante que o modelo não vai overfittar, pois os pesos já estão otimizados",
            "D) Permite usar learning rates muito maiores durante o fine-tuning",
        ],
        "answer": "B) Inicializa os pesos próximos de uma boa região do espaço de parâmetros (perto do ótimo global), melhorando convergência e atuando como regularizador",
        "explanation": (
            "O slide afirma: 'Pretraining already brings the activations of the "
            "neural network to the manifold of the data distribution' e "
            "'Pretraining initializes the problem closer to the basin of global optima'. "
            "Isso resolve dois problemas: inicializações ruins que levam a mínimos locais "
            "ruins, e overfitting (pois o pretraining aprende estrutura dos dados sem labels)."
        ),
    },
    {
        "topic": "Regularização",
        "question": (
            "Segundo o slide, qual é a principal diferença entre Bagging e Dropout "
            "como métodos de ensemble?"
        ),
        "options": [
            "A) Bagging usa redes diferentes com arquiteturas distintas; Dropout usa uma única arquitetura",
            "B) Bagging treina k modelos completos e independentes (ineficiente); Dropout simula o ensemble de 2ⁿ subredes compartilhando pesos em um único modelo (eficiente)",
            "C) Dropout reduz bias; Bagging reduz variance",
            "D) Bagging só funciona com modelos lineares; Dropout funciona com redes neurais profundas",
        ],
        "answer": "B) Bagging treina k modelos completos e independentes (ineficiente); Dropout simula o ensemble de 2ⁿ subredes compartilhando pesos em um único modelo (eficiente)",
        "explanation": (
            "O slide menciona: 'Main challenge [of Bagging] is to construct multiple "
            "training models → highly inefficient'. O Dropout resolve isso: com n "
            "neurônios e p=0.5, existem 2ⁿ subredes possíveis, todas compartilhando "
            "pesos. Cada forward pass treina uma subrede diferente. Na inferência, "
            "o weight scaling aproxima a média do ensemble sem custo adicional."
        ),
    },
]
# Q50 — adicionada para completar 50 questões
QUESTIONS.append(
    {
        "topic": "Regularização",
        "question": (
            "O slide cita Neural Networks como 'inherently low-bias and high-variance learners'. "
            "Qual afirmação resume corretamente o dilema que isso cria?"
        ),
        "options": [
            "A) Redes neurais são sempre preferíveis a modelos lineares independente do tamanho do dataset",
            "B) Redes neurais têm capacidade de aproximar qualquer função (baixo bias), mas com dados limitados essa complexidade se volta contra o modelo (alta variance), exigindo técnicas de regularização",
            "C) A alta variance de redes neurais é irrelevante pois GPUs modernas compensam com mais épocas de treino",
            "D) Redes neurais têm baixo bias apenas quando usam ReLU como função de ativação",
        ],
        "answer": "B) Redes neurais têm capacidade de aproximar qualquer função (baixo bias), mas com dados limitados essa complexidade se volta contra o modelo (alta variance), exigindo técnicas de regularização",
        "explanation": (
            "O slide afirma: 'Neural networks are inherently low-bias and high-variance "
            "learners ⇒ Need ways of handling complexity'. Uma rede grande pode memorizar "
            "qualquer dataset de treino (bias ≈ 0), mas memorização de nuances do treino "
            "não generaliza. Por isso todo o restante da aula foca em técnicas para "
            "reduzir a variance: L1/L2, Dropout, Early Stopping, Bagging, etc."
        ),
    }
)
