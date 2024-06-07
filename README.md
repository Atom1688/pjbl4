### Objetivo: Deve ser realizada uma entrega e apresentação do trabalho final, contendo toda a estrutura de Hardware e Software, ou seja: Banco de dados conectado com o Flask e armazenando os dados de sensores e atuadores, Hardware funcional com pelo menos 2 sensores e 2 atuadores (no mínimo) e interface Web Flask.

### Observações: Pode ser utilizado o simulador Wokwi para o desenvolvimento e validação da parte de hardware do projeto final.   

## Deve ser entregue um relatório final, o relatório deve conter a descrição completa do projeto, bem como das ferramentas utilizadas. O que deve conter no relatório e ser entregue:

- Web (2 pontos referente ao relatório): 
  - [x] Aplicação Flask: controladores (Blueprints) e visualizações (páginas HTML).
  - [ ] No mínimo 4 páginas de cadastro e 4 páginas de listagem. 
  - [ ] Página inicial contendo as informações do projeto. 
  - [x] Página para acionamento e recuperação de dados históricos dos Atuadores e Sensores. 
  - [ ] Controle de Acesso com o Flask-Login.
  - OBS: se algum grupo utilizar outra tecnologia, considerações e ponderações específicas serão realizadas

- Banco de Dados (2 pontos referente ao relatório):
  - [x] Modelos SQLAlchemy (mínimo 6 modelos).
  - Será criado mais modelos pro MQTT, que precisarão de CRUD
  - [x] Métodos para inserir, selecionar, editar e excluir os dados do banco de dados.
  - [ ] Modelagem Conceitual, Lógica e Física do banco de dados.

- Hardware (2 pontos referente ao relatório):
  - [x] Esquemática do Hardware utilizado – sensores, atuadores e microcontrolador.
  - [x] No mínimo 2 sensores e dois atuadores.
  - [x] Tópicos MQTT utilizados (nomes e explicações de funcionalidades).
  - [ ] Todas as entregas exigidas no PjBL 3, agora integrado ao flask. O PjBL3 pode ser uma seção do relatório final.

- Integração (2 pontos referente ao relatório):
  - [ ] Integração dos três tópicos principais da disciplina apresentados anteriormente: Web, Banco de Dados, Hardware.
  - [x] Comunicação IoT com o Flask-Mqtt: os dados dos sensores e atuadores devem ser processados pela aplicação flask e salvos no banco de dados, bem como a aplicação flask deve publicar mensagens (solicitações), por meio de tópicos específicos, solicitando ações do hardware.

- TDEs desenvolvidos ao longo do semestre (2 pontos referente ao relatório): 
  - Deve conter um capítulo/sessão para cada TDE, conforme apresentado no início da disciplina.
    - [ ] TDE1 – Entendendo o projeto final e seus requisitos de Hardware Turma U
    - [ ] TDE2 - Design de Aplicações Web
    - [ ] TDE3 - Flask Login com Role
