
# WSIP - What Should I Play?

## Sobre o Projeto

WSIP (What Should I Play?) é uma aplicação web desenvolvida em Python utilizando o framework Flask.

O objetivo do sistema é ajudar jogadores que possuem muitos jogos em sua biblioteca e têm dificuldade em decidir qual jogar. O usuário pode cadastrar seus jogos, organizar o progresso de cada um e utilizar um sistema de sorteio para receber uma recomendação aleatória.

Além disso, o sistema realiza o consumo de uma API externa (RAWG) para buscar automaticamente informações dos jogos cadastrados, como capa, gênero, data de lançamento e avaliação.

---

## Funcionalidades

* Cadastro de jogos
* Exclusão de jogos
* Atualização de status
* Biblioteca de jogos organizada em cards
* Busca automática de informações através de API
* Exibição automática da capa do jogo
* Sorteio aleatório de um jogo da biblioteca
* Mensagens personalizadas conforme o status do jogo
* Persistência dos dados utilizando SQLite

---

## Tecnologias Utilizadas

### Backend

* Python 3
* Flask

### Banco de Dados

* SQLite

### Frontend

* HTML5
* CSS3

### Integrações

* RAWG Video Games Database API

---

## Estrutura do Projeto

WSIP/

├── app.py

├── games.db

├── README.md

├── static/

│   └── style.css

└── templates/

```
├── index.html

└── random.html
```

---

## Requisitos

* Python 3.12 ou superior
* Flask
* Requests

---

## Instalação

Clone o repositório:

git clone (https://github.com/srbruno29/WSIP)

Acesse a pasta do projeto:

cd WSIP

Crie um ambiente virtual:

python -m venv .venv

Ative o ambiente virtual:

Windows:

.venv\Scripts\activate

Linux/Mac:

source .venv/bin/activate

Instale as dependências:

pip install flask requests

---

## Execução

Execute o arquivo principal:

python app.py

Após iniciar o servidor, abra o navegador e acesse:

http://127.0.0.1:5000

---

## Como Utilizar

1. Digite o nome de um jogo.
2. Escolha o status desejado.
3. Clique em "Adicionar".
4. O sistema buscará automaticamente as informações do jogo.
5. Os jogos cadastrados serão exibidos na biblioteca.
6. Utilize o botão "Escolher meu jogo" para receber uma recomendação aleatória.

---

## Funcionalidades Acadêmicas Atendidas

O projeto atende aos requisitos propostos na atividade:

* Utilização de Framework Web (Flask)
* CRUD completo (Create, Read, Update e Delete)
* Consumo de API externa
* Processamento de dados
* Persistência em banco de dados SQLite
* Renderização de páginas HTML através de Templates
* Controle de versão utilizando Git e GitHub

---

## Autor

Bruno da Silva Martins, Felipe da Silva Paz

Projeto desenvolvido para a disciplina de Desenvolvimento Web.
