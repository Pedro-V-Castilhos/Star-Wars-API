# Star Wars API

API REST para consumo especializado de dados sobre o universo de Star Wars, funcionando como camada intermediária entre o Front End e a [SWAPI](https://swapi.dev/). Implementa cache HTTP para otimizar requisições e reduzir latência.

## 🚀 Tecnologias

- **Python 3.14**
- **FastAPI 0.128.0** - Framework web moderno e de alta performance
- **httpx 0.28.1** - Cliente HTTP assíncrono
- **hishel 1.1.8** - Sistema de cache HTTP com suporte SQLite
- **anysqlite 0.0.5** - Driver SQLite assíncrono
- **uvicorn 0.40.0** - Servidor ASGI

## 📋 Pré-requisitos

- Python 3.14 ou superior
- pip (gerenciador de pacotes Python)

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Pedro-V-Castilhos/Star-Wars-API.git
cd Star-Wars-API
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🎯 Como Executar

### Modo de desenvolvimento (com reload automático):

```bash
uvicorn app.main:app --reload
```

### Modo de produção:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Com porta customizada:

```bash
uvicorn app.main:app --reload --port 3000
```

A API estará disponível em: `http://localhost:8000`
Documentação interativa (Swagger): `http://localhost:8000/docs`

## 📚 Endpoints

### `GET /`

Endpoint raiz de boas-vindas.

**Resposta:**

```json
{
  "greetings": "May the Force be with you!"
}
```

### `GET /films`

Retorna informações sobre todos os filmes da saga Star Wars.

**Resposta:**

```json
{
  "count": 6,
  "next": null,
  "previous": null,
  "results": [
    {
      "title": "A New Hope",
      "episode_id": 4,
      "opening_crawl": "...",
      "director": "George Lucas",
      "producer": "Gary Kurtz, Rick McCallum",
      "release_date": "1977-05-25",
      "characters": [...],
      "planets": [...],
      "starships": [...],
      "vehicles": [...],
      "species": [...],
      "created": "2014-12-10T14:23:31.880000Z",
      "edited": "2014-12-20T19:49:45.256000Z",
      "url": "https://swapi.dev/api/films/1/"
    }
    // ... outros filmes
  ]
}
```

### `GET /films/{film_id}`

Retorna informações detalhadas sobre um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

**Exemplo:** `GET /films/1`

**Resposta:**

```json
{
  "title": "A New Hope",
  "episode_id": 4,
  "opening_crawl": "It is a period of civil war...",
  "director": "George Lucas",
  "producer": "Gary Kurtz, Rick McCallum",
  "release_date": "1977-05-25",
  "characters": [
    "https://swapi.dev/api/people/1/",
    "https://swapi.dev/api/people/2/"
  ],
  "planets": [...],
  "starships": [...],
  "vehicles": [...],
  "species": [...],
  "created": "2014-12-10T14:23:31.880000Z",
  "edited": "2014-12-20T19:49:45.256000Z",
  "url": "https://swapi.dev/api/films/1/"
}
```

## 🏗️ Arquitetura

A aplicação utiliza uma arquitetura em camadas:

- **Cache HTTP Assíncrono**: Implementado com Hishel + SQLite, gerenciado no ciclo de vida da aplicação (lifespan) para reutilização eficiente das conexões
- **Helper Reutilizável**: Função `get_from_url()` centraliza requisições HTTP com cache automático, evitando repetição de código
- **Cliente Global**: `AsyncCacheClient` inicializado uma única vez e compartilhado entre todas as requisições

### Estrutura de Diretórios

```
app/
├── __init__.py
├── main.py          # Definição de rotas e aplicação FastAPI
├── config.py        # Configuração do cache client e lifespan
└── utils/
    ├── __init__.py
    └── helpers.py   # Funções auxiliares reutilizáveis
```

## 📝 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

**Pedro V. Castilhos**

- GitHub: [@Pedro-V-Castilhos](https://github.com/Pedro-V-Castilhos)
