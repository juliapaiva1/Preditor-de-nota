# Preditor de nota
# Aluna: Júlia Ferreira de Paiva

1. Funcionamento do sistema

O programa utiliza a SVD (decomposição em valores singulares) para tentar prever a nota que um usuário daria para um filme que ele ainda não assistiu. Ela funciona decompondo uma matriz A (que contém as avaliações de usuários para filmes) em três outras matrizes: uma matriz U (em que suas colunas são os auto-vetores de $A^T A$,), uma matriz S (onde $s_{i,i}$ é a raiz quadrada dos auto-valores de $A^T A$ ou de $A A^T$) e uma matriz Vt (uma matriz transposta de V, em que suas as linhas de $V^T$ são auto-vetores de $A A^T$).

Para formar a matriz B, pegamos um valor qualquer diferente de 0 na matriz A e o multiplicamos por um valor aleatório entre 0 e 5, gerando uma matriz ruidosa. Esse procedimento é feito na função criacao_matriz_b, que usa loops e verificações para gerar a matriz.

No sistema criado, decompomos essa matriz B em u, s e vt (três outras matrizes) usando a função svd(). A partir delas, selecionamos um valor aleatório para k, que determina quantos elementos serão mantidos nas matrizes u_, s_ e vt_. Nessas matrizes U, S e Vt é preservada uma quantidade K de elementos mais significantes, escolhida de forma aleatória, gerando novas matrizes u_, s_ e vt_. Cria-se uma matriz sigma (matriz diagonal com valores singulares na diagonal e 0 em outras posições) com com s_, o número de linhas da matriz u_ e o número de colunas da atrix vt_. Por fim, para reduzir o ruído, utiliza-se a fórmula U @ Sigma @ Vt, representada no código por: matriz_b_alterada = u_ @ diagsvd(s_, u_.shape[1], vt_.shape[0]) @ vt_.

Esse processo é repetido várias vezes quando demo.py é executado para testar a acurácia do programa. Em cada uma dessas vezes, é calculada a diferença entre o valor original e o valor predito, e esse resultado é armazenado numa lista que será usada para construir um histograma.

2. Como rodar

Tenha instalado em sua máquina um editor de código, como por exemplo, Visual Studio Code. Na página do projeto no Github, clique em "Code" e baixe como zip. Extraia em uma pasta e abra essa pasta no editor de código. Instale os pacotes necessários com o comando "pip install -r requirements.txt", pelo terminal. Depois que a instalação tiver sido bem-sucedida, entre no arquivo "demo.py" e execute-o. Aguarde alguns minutos, pois ele leva um tempo para analisar os dados. Depois de terminar de rodas, um arquivo "histograma.png" irá aparecer na pasta principal do projeto, nele contendo o histograma de erros do sistema preditor.

O programa já vem com uma demonstração do que seria esse histograma, o arquivo "exemplo.png", que foi criado a partir dos dados de 100 repetições do nosso sistema.

3. Resultados encontrados

Tomando como referência o arquivo "exemplo.py", que simulou 100 vezes o sistema criado, pode-se dizer que ele é razoavelmente confiável, e que poderia ser usado em produção. Os erros apontados apresentam uma margem de diferença bem pequena, a maior parte apresenta uma diferença entre 2 ou -2 em relação ao valor original. Entretanto, é um sistema que poderia ser melhorado para apresentar uma taxa de erros ainda menor, talvez experimentando novas formas de pegar valores mais relevantes ou testando com casos diferentes.