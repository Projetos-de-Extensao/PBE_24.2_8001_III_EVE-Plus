# Casos de Uso - Plataforma de Streaming de Audiobooks com Sons Relaxantes

[Diagrama de Casos de Uso](./assets/Casos_De_Uso/casodeuso.png)
 
## VST: Visitante

### VST-01: Cadastrar Usuário
- **Ator Principal**: Visitante
- **Descrição**: Permitir que o visitante da plataforma crie uma conta para utilizar todos os recursos disponíveis.
- **Fluxo Principal**:
  1. O visitante acessa a página de cadastro.
  2. Preenche as informações pessoais (nome, e-mail, senha, etc.).
  3. O sistema valida e armazena os dados.
  4. O sistema confirma o cadastro e o usuário está autenticado.

## USR: Usuário

### USR-01: Fazer Login
- **Ator Principal**: Usuário
- **Descrição**: Autenticar um usuário já cadastrado para acessar sua conta e funcionalidades da plataforma.
- **Fluxo Principal**:
  1. O usuário acessa a página de login.
  2. Insere suas credenciais (e-mail e senha).
  3. O sistema verifica a autenticidade das informações.
  4. O usuário é redirecionado para sua página inicial.

### USR-02: Pesquisar Audiobook
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário busque audiobooks pelo título, autor ou categoria.
- **Fluxo Principal**:
  1. O usuário acessa a barra de busca.
  2. Insere os termos de pesquisa (título, autor, gênero).
  3. O sistema retorna uma lista de audiobooks que correspondem à pesquisa.
  4. O usuário escolhe um audiobook para visualizar mais detalhes ou ouvir.

### USR-03: Ouvir Audiobook
- **Ator Principal**: Usuário
- **Descrição**: Reproduzir um audiobook escolhido pelo usuário.
- **Fluxo Principal**:
  1. O usuário seleciona um audiobook da biblioteca ou resultado de busca.
  2. O sistema exibe os controles de reprodução (play, pause, avançar, retroceder).
  3. O usuário inicia a reprodução.
  4. O sistema toca o audiobook até o final ou até que o usuário pause.

### USR-04: Personalizar Sons Relaxantes
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário adicione ou altere sons relaxantes enquanto ouve um audiobook.
- **Fluxo Principal**:
  1. O usuário começa a ouvir um audiobook.
  2. O sistema exibe as opções de sons relaxantes (ex.: som de chuva, vento, mar).
  3. O usuário seleciona o som de fundo desejado.
  4. O sistema reproduz o som relaxante junto com o audiobook.

### USR-05: Gerenciar Playlists
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário crie e gerencie playlists de audiobooks.
- **Fluxo Principal**:
  1. O usuário acessa sua área de playlists.
  2. Cria uma nova playlist inserindo um nome.
  3. Adiciona audiobooks à playlist.
  4. O sistema armazena a playlist e permite que o usuário a edite ou remova audiobooks.

### USR-06: Avaliar e Comentar Audiobook
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário avalie e comente sobre um audiobook após ouvi-lo.
- **Fluxo Principal**:
  1. O usuário acessa a seção de avaliações de um audiobook.
  2. Insere uma avaliação (estrelas) e, opcionalmente, um comentário.
  3. O sistema salva e exibe as avaliações e comentários para outros usuários.

### USR-07: Gerenciar Perfil de Usuário
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário edite suas informações pessoais.
- **Fluxo Principal**:
  1. O usuário acessa a área de perfil.
  2. Altera informações como nome, e-mail, senha, foto de perfil, etc.
  3. O sistema valida e atualiza os dados.

### USR-08: Receber Recomendações Personalizadas
- **Ator Principal**: Usuário
- **Descrição**: Oferecer ao usuário recomendações de audiobooks com base em suas preferências e histórico de uso.
- **Fluxo Principal**:
  1. O sistema analisa o histórico de audiobooks do usuário.
  2. O sistema gera uma lista de audiobooks recomendados com base em seus interesses.
  3. O usuário pode visualizar e escolher ouvir um audiobook recomendado.

### USR-09: Ver Histórico de Audiobooks Ouvidos
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário visualize a lista de audiobooks que já ouviu.
- **Fluxo Principal**:
  1. O usuário acessa a área de histórico.
  2. O sistema exibe os audiobooks já ouvidos, com informações sobre a última reprodução.
  3. O usuário pode selecionar um audiobook do histórico para ouvir novamente.

### USR-10: Favoritar Audiobook
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário adicione audiobooks à sua lista de favoritos.
- **Fluxo Principal**:
  1. O usuário acessa a página de um audiobook.
  2. Seleciona a opção de adicionar aos favoritos.
  3. O sistema armazena o audiobook na lista de favoritos do usuário.

### USR-11: Fazer Download de Audiobook (Offline)
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário baixe audiobooks para ouvir offline.
- **Fluxo Principal**:
  1. O usuário seleciona um audiobook.
  2. Escolhe a opção de download.
  3. O sistema baixa o arquivo de áudio para o dispositivo do usuário.

### USR-12: Assinar Plano Premium
- **Ator Principal**: Usuário
- **Descrição**: Permitir que o usuário faça uma assinatura premium para acessar funcionalidades exclusivas.
- **Fluxo Principal**:
  1. O usuário acessa a página de planos.
  2. Escolhe um plano e insere suas informações de pagamento.
  3. O sistema confirma a assinatura e desbloqueia os recursos premium.

## ADM: Administrador

### ADM-01: Gerenciar Usuários
- **Ator Principal**: Administrador
- **Descrição**: Permitir que o administrador visualize, edite e remova usuários da plataforma.
- **Fluxo Principal**:
  1. O administrador acessa o painel de gestão de usuários.
  2. O sistema exibe a lista de usuários cadastrados.
  3. O administrador pode buscar, editar ou remover um usuário da lista.
  4. O sistema aplica as alterações e salva os dados.

### ADM-02: Gerenciar Audiobooks
- **Ator Principal**: Administrador
- **Descrição**: Permitir que o administrador adicione, edite ou remova audiobooks do catálogo.
- **Fluxo Principal**:
  1. O administrador acessa o painel de audiobooks.
  2. O sistema exibe a lista de audiobooks cadastrados.
  3. O administrador pode adicionar um novo audiobook, editar informações ou removê-lo.
  4. O sistema atualiza o catálogo conforme as alterações feitas.

### ADM-03: Gerenciar Planos de Assinatura
- **Ator Principal**: Administrador
- **Descrição**: Permitir que o administrador configure e edite os planos de assinatura da plataforma.
- **Fluxo Principal**:
  1. O administrador acessa o painel de gestão de planos.
  2. O sistema exibe os planos de assinatura atuais.
  3. O administrador pode criar novos planos, alterar valores ou remover planos existentes.
  4. O sistema atualiza as informações dos planos de assinatura.

### ADM-04: Gerar Relatórios de Uso
- **Ator Principal**: Administrador
- **Descrição**: Permitir que o administrador gere relatórios sobre o uso da plataforma, como número de usuários, audiobooks mais ouvidos, e dados financeiros.
- **Fluxo Principal**:
  1. O administrador acessa o painel de relatórios.
  2. Escolhe o tipo de relatório que deseja gerar (usuários, audiobooks, finanças, etc.).
  3. O sistema processa e exibe o relatório solicitado.
  4. O administrador pode exportar o relatório em formato PDF ou CSV.

## EDT: Editora

### EDT-01: Cadastrar Audiobooks
- **Ator Principal**: Editora
- **Descrição**: Permitir que uma editora faça o upload e cadastre novos audiobooks na plataforma.
- **Fluxo Principal**:
  1. A editora acessa sua área de gerenciamento de conteúdo.
  2. Escolhe a opção de adicionar novo audiobook.
  3. Insere informações sobre o audiobook (título, autor, descrição, capa, arquivo de áudio).
  4. O sistema valida e armazena o audiobook no catálogo.

### EDT-02: Gerenciar Audiobooks
- **Ator Principal**: Editora
- **Descrição**: Permitir que a editora edite informações ou remova seus audiobooks do catálogo.
- **Fluxo Principal**:
  1. A editora acessa sua área de gerenciamento de audiobooks.
  2. Visualiza a lista de audiobooks que ela cadastrou.
  3. A editora pode editar informações ou remover audiobooks da lista.
  4. O sistema aplica as alterações e atualiza o catálogo.

### EDT-03: Acompanhar Estatísticas de Audiobooks
- **Ator Principal**: Editora
- **Descrição**: Permitir que a editora veja relatórios e estatísticas de desempenho de seus audiobooks (número de reproduções, avaliações, etc.).
- **Fluxo Principal**:
  1. A editora acessa a área de relatórios.
  2. Seleciona o audiobook ou grupo de audiobooks que deseja visualizar as estatísticas.
  3. O sistema exibe dados como número de reproduções, avaliações, e desempenho geral.
  4. A editora pode exportar os relatórios.
