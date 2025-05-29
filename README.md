# Sistema de Reservas de Salas  📙

Este serviço RESTful é responsável por gerenciar o agendamento e controle de reservas de salas. Ele garante a disponibilidade das salas, prevenindo conflitos de horário e validando as entidades envolvidas (turmas e professores) através da integração com o microsserviço de Sistema de Gerenciamento Escolar.

Esta API depende da API de Gerenciamento Escolar (School System), que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via requisições HTTP REST, para validar:
- Verifica se a turma existe via GET /turmas/{id}
- Verifica se o professor existe via GET /professores/{id}
- Se a API-SchoolSystem estiver indisponível ou os dados não forem encontrados, a API retorna erro 400 Bad Request


## 🛠 Tecnologias Utilizadas
* Python 3.11
* Flask
* Docker & Docker Compose

## 🚀 Como Executar o Projeto

## Pré-requisitos
* Docker instalado
* Docker Compose instalado
* Python 3.11 (se for executar sem Docker)
* pip (gerenciador de pacotes do Python)

### Passo a Passo
1. Clone o repositório da API de Reservas de Sala:

Bash

git clone https://github.com/pedrhnttz/apidev_reservas.git
cd apidev_reservas

2. Inicie os contêineres Docker:

Certifique-se de que a API da qual este microsserviço depende (Sistema de Gerenciamento Escolar) esteja também em execução (seja em outro contêiner Docker ou localmente) e acessível pela rede Docker.

Bash

3. docker-compose up --build
Este comando irá construir as imagens Docker e iniciar os serviços definidos no docker-compose.yml. A API de Reservas de Sala estará acessível na porta configurada no docker-compose.yml (geralmente http://localhost:5000 se for a porta padrão do Flask).

## 🎯 Endpoints da API
A API de Reservas de Sala oferece os seguintes endpoints para gerenciamento das reservas:

#### 1. POST /reservas - Criar uma Nova Reserva
Cria uma nova reserva de sala no sistema.

Corpo da Requisição (JSON):

JSON

{
    "turma_id": 1,
    "sala": "sala 101",
    "data": "2025-06-28", // Formato "YYYY-MM-DD"
    "hora_inicio": "20:12",
    "hora_fim": "21:40"
}
#### 2. GET /reservas - Retornar Todas as Reservas
Recupera uma lista de todas as reservas de sala registradas.

Retorno (JSON):

JSON

[
    {
        "id_reserva": 1,
        "turma_id": 1,
        "sala": "sala 101",
        "data": "2025-06-28",
        "hora_inicio": "20:12:00",
        "hora_fim": "21:40:00"
    },
    {
        "id_reserva": 2,
        "turma_id": 2,
        "sala": "sala 205",
        "data": "2025-07-10",
        "hora_inicio": "09:00:00",
        "hora_fim": "10:30:00"
    }
]
#### 3. GET /reservas/<id_reserva> - Retornar Reserva por ID
Recupera os detalhes de uma reserva específica usando seu id_reserva.

Parâmetros de URL:

id_reserva: O ID único da reserva a ser recuperada.
Exemplo de Retorno (para id_reserva = 1):

JSON

{
    "id_reserva": 1,
    "turma_id": 1,
    "sala": "sala 101",
    "data": "2025-06-28",
    "hora_inicio": "20:12:00",
    "hora_fim": "21:40:00"
}
#### 4. PUT /reservas/<id_reserva> - Atualizar uma Reserva Existente
Atualiza os detalhes de uma reserva de sala existente.

Parâmetros de URL:

id_reserva: O ID único da reserva a ser atualizada.
Corpo da Requisição (JSON):

JSON

{
    "turma_id": 1,
    "sala": "sala 102",
    "data": "2025-06-29",
    "hora_inicio": "09:00",
    "hora_fim": "10:00"
}
Todos os campos são opcionais, mas pelo menos um deve ser fornecido para a atualização.
Exemplo de Retorno (para id_reserva = 1):

JSON

{
    "id_reserva": 1,
    "turma_id": 1,
    "sala": "sala 102",
    "data": "2025-06-29",
    "hora_inicio": "09:00:00",
    "hora_fim": "10:00:00"
}
#### 5. DELETE /reservas/<id_reserva> - Excluir uma Reserva
Exclui uma reserva de sala existente pelo seu id_reserva.

Parâmetros de URL:

id_reserva: O ID único da reserva a ser excluída.
Retorno em caso de sucesso (Exemplo):

JSON

{
    "message": "Reserva com ID 1 excluída com sucesso."
}
Retorno em caso de reserva não encontrada (Exemplo):

JSON

{
    "message": "Reserva com ID 999 não encontrada."
}
