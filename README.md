Perfeito! O conteúdo completo que geramos está pronto para ser colocado no seu arquivo README.md.

API de Reservas de Sala
Esta API é um microsserviço responsável por gerenciar reservas de salas, dependendo da execução de outra API para seu funcionamento completo. Ela permite criar novas reservas, consultar todas as reservas existentes, buscar uma reserva específica por ID, atualizar reservas existentes e excluir reservas.

Requisitos
Certifique-se de ter os seguintes softwares instalados em seu ambiente:

Docker
Docker Compose
Python 3.11 (para execução local, caso não use Docker)
Flask (framework utilizado pela API)
Execução do Projeto
Para colocar a API de Reservas de Sala em funcionamento, siga os passos abaixo:

Clone o repositório da API de Reservas:

Bash

git clone https://github.com/pedrhnttz/apidev_reservas.git
cd apidev_reservas
Inicie os contêineres Docker:

Certifique-se de que a API da qual este microsserviço depende esteja também em execução (seja em outro contêiner Docker ou localmente).

Bash

docker-compose up --build
Este comando irá construir as imagens Docker e iniciar os serviços definidos no docker-compose.yml.

Endpoints
A API de Reservas de Sala oferece os seguintes endpoints:

1. Criar uma Nova Reserva
Cria uma nova reserva de sala no sistema.

URL: /reservas

Método: POST

Body Request:

JSON

{
    "turma_id": 1,
    "sala": "sala 101",
    "data": "2025-06-28", // Formato "YYYY-MM-DD"
    "hora_inicio": "20:12",
    "hora_fim": "21:40"
}
2. Retornar Todas as Reservas Registradas
Recupera uma lista de todas as reservas de sala registradas.

URL: /reservas

Método: GET

Retorno:

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
3. Retornar Reserva por ID
Recupera os detalhes de uma reserva específica usando seu id_reserva.

URL: /reservas/<id_reserva>

Método: GET

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
4. Atualizar uma Reserva Existente
Atualiza os detalhes de uma reserva de sala existente.

URL: /reservas/<id_reserva>

Método: PUT

Parâmetros de URL:

id_reserva: O ID único da reserva a ser atualizada.
Body Request:

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
5. Excluir uma Reserva
Exclui uma reserva de sala existente pelo seu id_reserva.

URL: /reservas/<id_reserva>

Método: DELETE

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
