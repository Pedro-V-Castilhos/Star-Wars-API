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

### `GET /films/{film_id}/characters`

Retorna todos os personagens que aparecem em um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

**Exemplo:** `GET /films/1/characters`

**Resposta:**

```json
{
  "results": [
    {
      "name": "Luke Skywalker",
      "height": "172",
      "mass": "77",
      "hair_color": "blond",
      "skin_color": "fair",
      "eye_color": "blue",
      "birth_year": "19BBY",
      "gender": "male",
      "homeworld": "https://swapi.dev/api/planets/1/",
      "films": [...],
      "species": [],
      "vehicles": [...],
      "starships": [...],
      "created": "2014-12-09T13:50:51.644000Z",
      "edited": "2014-12-20T21:17:56.891000Z",
      "url": "https://swapi.dev/api/people/1/"
    }
    // ... outros personagens
  ]
}
```

**Nota:** Este endpoint realiza múltiplas requisições em paralelo para buscar os dados de todos os personagens, otimizando o tempo de resposta.

## 🏗️ Arquitetura

A aplicação utiliza uma arquitetura em camadas com foco em performance e reutilização:

### Cliente HTTP Global com Cache

O projeto implementa um **cliente HTTP global com cache automático** usando:

- **Hishel 1.1.8**: Sistema de cache HTTP com suporte a múltiplos backends
- **SQLite**: Armazenamento persistente do cache via anysqlite
- **AsyncCacheClient**: Cliente gerenciado no ciclo de vida da aplicação (lifespan)

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.cache_client = AsyncCacheClient()
    yield
    await app.state.cache_client.aclose()
```

**Benefícios:**

- ✅ Cache automático de respostas HTTP
- ✅ Redução de latência em requisições repetidas
- ✅ Cliente compartilhado entre todas as requisições
- ✅ Gerenciamento eficiente de recursos

### Helpers Reutilizáveis

- **`get_from_url()`**: Centraliza requisições HTTP com cache automático
- **`get_all_from_urls()`**: Executa múltiplas requisições em paralelo com `asyncio.gather()`

### Estrutura de Diretórios

```
app/
├── __init__.py
├── main.py              # Aplicação FastAPI principal
├── config.py            # Configuração do cache client e lifespan
├── api/
│   ├── __init__.py
│   ├── router.py        # Definição dos routers da aplicação
│   └── endpoints/
│       ├── __init__.py
│       └── films.py     # Endpoints de filmes
└── utils/
    ├── __init__.py
    └── helpers.py       # Funções auxiliares reutilizáveis
prompts/
├── 01.md                # Prompts de desenvolvimento
├── 02.md
└── Context.md
```

**Organização modular** que facilita escalabilidade e manutenção do código.

## � Organização de Prompts

O projeto mantém um histórico estruturado dos prompts utilizados durante o desenvolvimento na pasta `prompts/`:

```
prompts/
├── 01.md          # Implementação inicial da API
├── 02.md          # Atualização da documentação
└── Context.md     # Contexto e instruções para o desenvolvimento
```

Esta organização permite:

- 📝 Rastreabilidade das decisões de desenvolvimento
- 🔄 Facilita replicação e entendimento do processo
- 📚 Serve como documentação evolutiva do projeto

## �📝 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

**Pedro V. Castilhos**

- GitHub: [@Pedro-V-Castilhos](https://github.com/Pedro-V-Castilhos)
