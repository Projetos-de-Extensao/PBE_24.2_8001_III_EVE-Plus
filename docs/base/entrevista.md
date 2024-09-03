---
id: entrevista
title: Entrevista
---

## Introdução

A técnica da entrevista trata-se de uma conversa guiada por um roteiro de perguntas ou tópicos, com o objetivo de questionar os stakeholders sobre o sistema atual e esclarecer suas necessidades para o sistema que será desenvolvido. A entrevista permite uma investigação em profundidade sobre o problema, possibilitando a coleta de uma grande quantidade de informações para o desenvolvimento do sistema.

### Metodologia

Para esta entrevista, optamos por seguir um modelo de entrevista aberta, com uma série de perguntas de apoio pré-definidas, visando que os stakeholders exponham informações importantes para o sistema. As questões foram formuladas e filtradas de acordo com o interesse da equipe, com o propósito de orientar o entrevistador durante a entrevista. Tanto o entrevistador quanto o entrevistado tiveram liberdade para abordar qualquer assunto relacionado ao sistema durante a entrevista.

### Roteiro

1. Você pode descrever como você imagina a plataforma de streaming ideal para sua biblioteca?
2. Como funcionava o sistema anterior que você utilizava para disponibilizar conteúdo multimídia?
3. Você já usou alguma aplicação similar para streaming de audiobooks, filmes ou música? Como foi a experiência?
4. Teve algum problema específico com o sistema atual que gostaria de ver resolvido na nova plataforma?
5. O que você acha de uma aplicação que integre audiobooks, resenhas e trilhas sonoras em um único ambiente?
6. Para você, qual seria o sistema ideal para gerenciar e oferecer conteúdo multimídia aos usuários?
7. Você gostaria de poder se cadastrar e salvar suas preferências pessoais, como playlists e histórico de audição?
8. Você gostaria que as informações de segurança e privacidade fossem claramente destacadas na plataforma?

## Entrevistas

*Versão 1.0*

#### Entrevista 1

| Nome           | Papel            |
|----------------|------------------|
| João Gabriel   | Entrevistador     |
| Stakeholder XYZ | Entrevistado     |

| Data       | Horário de início | Horário de fim | Descrição                                    |
|------------|-------------------|----------------|----------------------------------------------|
| 03/09/2024 | 12:11              | 12:38          | Entrevista realizada via chat.       |

### Diálogo durante a apresentação dos projetos

- *João Gabriel*: Você poderia descrever como imagina a plataforma de streaming ideal para sua biblioteca?
- *Stakeholder XYZ*: Sim, eu imagino uma plataforma que seja intuitiva e permita que os usuários acessem audiobooks, filmes e trilhas sonoras relacionados aos livros de forma integrada. A ideia é criar uma experiência imersiva, onde o usuário possa alternar facilmente entre ler um livro e ouvir a trilha sonora relacionada, por exemplo.
  
- *João Gabriel*: Como funcionava o sistema anterior que você utilizava?
- *Stakeholder XYZ*: O sistema anterior era bastante limitado, apenas oferecia audiobooks sem muita integração com outros tipos de conteúdo. Nós tínhamos uma plataforma básica para audiobooks, mas os usuários sempre pediam por mais opções, como vídeos ou trilhas sonoras que complementassem a leitura.

- *João Gabriel*: Já usou alguma aplicação similar para streaming de audiobooks, filmes ou música?
- *Stakeholder XYZ*: Já, mas não era muito satisfatória. Havia muitos problemas de navegação e a qualidade do áudio era inconsistente. A integração entre diferentes tipos de mídia também era fraca, e não havia uma forma de conectar a leitura de um livro com, por exemplo, sua adaptação cinematográfica.

- *João Gabriel*: Teve algum problema específico com o sistema atual que gostaria de ver resolvido na nova plataforma?
- *Stakeholder XYZ*: Um dos maiores problemas foi a falta de personalização. Os usuários queriam criar suas próprias playlists de conteúdo relacionado, mas o sistema não oferecia essa funcionalidade. Além disso, a segurança dos dados era uma preocupação, especialmente em relação ao armazenamento e uso das informações pessoais dos usuários.

- *João Gabriel*: O que você acha de uma aplicação que integre audiobooks, resenhas e trilhas sonoras em um único ambiente?
- *Stakeholder XYZ*: Isso seria perfeito! Poder ver resenhas, ouvir trilhas sonoras e acessar o audiobook de um livro, tudo em um só lugar, tornaria a experiência muito mais rica e envolvente. Além disso, a possibilidade de assistir a vídeos relacionados, como entrevistas com autores ou trailers de adaptações, seria um grande diferencial.

- *João Gabriel*: Para você, qual seria o sistema ideal para gerenciar e oferecer conteúdo multimídia aos usuários?
- *Stakeholder XYZ*: O sistema ideal deveria ser fácil de usar, com uma interface limpa e responsiva. Ele também precisa oferecer recursos avançados de pesquisa e filtragem para ajudar os usuários a encontrar exatamente o que procuram. A personalização é crucial, permitindo que os usuários salvem preferências, como playlists e temas de interface.

- *João Gabriel*: Você gostaria de poder se cadastrar e salvar suas preferências pessoais, como playlists e histórico de audição?
- *Stakeholder XYZ*: Sim, isso é muito importante. A capacidade de salvar e retomar o conteúdo de onde parei, criar playlists personalizadas, e até compartilhar minhas recomendações com amigos, adicionaria muito valor à plataforma.

- *João Gabriel*: Você gostaria que as informações de segurança e privacidade fossem claramente destacadas na plataforma?
- *Stakeholder XYZ*: Com certeza. Transparência sobre como os dados são utilizados e a garantia de que as informações estão seguras são fundamentais para construir a confiança dos usuários na plataforma.

## Requisitos Elicitados

| *ID*  | *Descrição* |
|---------|---------------|
| REQ01   | O sistema deve permitir o streaming de audiobooks em alta qualidade, com suporte para múltiplos formatos de áudio, garantindo uma experiência de escuta clara e imersiva. |
| REQ02   | A interface do usuário deve ser intuitiva e facilitar a navegação pelos audiobooks, com funcionalidades de busca avançada, recomendação personalizada e filtros por gênero, autor e popularidade. |
| REQ03   | O sistema deve integrar resenhas em texto e vídeo, oferecendo aos usuários insights e análises detalhadas sobre os livros disponíveis na plataforma. |
| REQ04   | A plataforma deve incluir vídeos de bastidores de adaptações cinematográficas, trailers, e entrevistas com autores e diretores relacionados aos livros presentes na biblioteca. |
| REQ05   | O sistema deve permitir o acesso a trilhas sonoras e playlists temáticas, conectadas ao conteúdo dos livros, para enriquecer a experiência dos usuários. |
| REQ06   | O sistema deve oferecer a funcionalidade de reprodução simultânea de sons ambientes e músicas relaxantes, como som de chuva, ondas do mar, ou melodias suaves, durante a audição de audiobooks ou leitura de eBooks. |
| REQ07   | Deve ser possível para os usuários configurar preferências pessoais, como sons ambientes e temas de interface, para personalizar a experiência de uso da plataforma. |
| REQ08   | A plataforma deve ser compatível com múltiplos dispositivos (desktop, mobile, tablet), ajustando automaticamente a qualidade do streaming de acordo com a conexão do usuário. |
| REQ09   | O sistema deve ter um módulo de gerenciamento de conteúdo que permita a administração e organização do catálogo de audiobooks, resenhas e conteúdos multimídia. |
| REQ10   | O sistema deve implementar funcionalidades de segurança, incluindo criptografia de dados, para proteger as informações pessoais e de uso dos usuários. |
| REQ11   | A plataforma deve suportar a criação de contas de usuário, permitindo que os usuários salvem suas preferências, histórico de audição, e listas de favoritos. |
| REQ12   | Deve ser possível para os usuários compartilharem resenhas, playlists e conteúdos favoritos em redes sociais diretamente a partir da plataforma. |
| REQ13   | O sistema deve incluir uma funcionalidade de recomendação automática, sugerindo audiobooks, filmes, músicas e resenhas baseadas no histórico de audição e leitura dos usuários. |
| REQ14   | A plataforma deve fornecer acesso a eBooks, permitindo que os usuários alternem entre a leitura e a audição de um mesmo título, sincronizando o progresso entre os dois formatos. |
| REQ15   | O sistema deve incluir funcionalidades de acessibilidade, como suporte a comandos de voz, ajustes de contraste e fontes, para atender usuários com necessidades especiais. |
| REQ16   | A plataforma deve incluir um sistema de avaliação e comentários, permitindo que os usuários avaliem os conteúdos e deixem feedbacks para outros usuários. |
| REQ17   | O sistema deve permitir a criação de playlists personalizadas de audiobooks e músicas relaxantes, que podem ser salvas e acessadas a qualquer momento. |
| REQ18   | Deve haver uma política de privacidade clara e acessível que informe os usuários sobre como seus dados são coletados, armazenados e utilizados pela plataforma. |
| REQ19   | A plataforma deve incluir um sistema de suporte ao cliente, com canais de comunicação (chat, e-mail) para resolver problemas técnicos e responder a dúvidas dos usuários. |
| REQ20   | O sistema deve oferecer notificações personalizadas, alertando os usuários sobre novos lançamentos, atualizações de conteúdo, e sugestões baseadas em seus interesses. |

## Conclusão

Através da aplicação da técnica de entrevista aberta, foi possível elicitar um conjunto robusto de requisitos que cobre todos os aspectos essenciais para o desenvolvimento da plataforma de streaming proposta. Esses requisitos irão guiar o processo de design e desenvolvimento, garantindo que a plataforma atenda às necessidades do cliente e ofereça uma experiência rica e personalizada para os usuários finais.
