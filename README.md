# Star Wars API

API REST para consumo especializado de dados sobre o universo de Star Wars, funcionando como camada intermediária entre o Front End e a [SWAPI](https://swapi.dev/). Implementa cache HTTP para otimizar requisições e reduzir latência.

## 🚀 Tecnologias

### Produção

- **Python 3.14**
- **FastAPI 0.128.0** - Framework web moderno e de alta performance
- **httpx 0.28.1** - Cliente HTTP assíncrono
- **hishel 1.1.8** - Sistema de cache HTTP com suporte SQLite
- **anysqlite 0.0.5** - Driver SQLite assíncrono
- **uvicorn 0.40.0** - Servidor ASGI

### Desenvolvimento e Testes

- **pytest 9.0.2** - Framework de testes robusto e flexível
- **pytest-cov 7.0.0** - Plugin para análise de cobertura de código

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

### 📖 Documentação Automática

O FastAPI gera automaticamente documentação interativa completa de todos os endpoints:

- **Swagger UI**: `http://localhost:8000/docs` - Interface interativa para testar endpoints
- **ReDoc**: `http://localhost:8000/redoc` - Documentação alternativa em formato limpo

Ambas interfaces permitem explorar todos os 34 endpoints da API, ver schemas de resposta e executar requisições diretamente do navegador.

## 📚 Endpoints da API

A API fornece **34 endpoints** organizados em 6 recursos principais. Todos os endpoints de listagem suportam busca via parâmetro `?search=<termo>`.

### 🏠 Root

#### `GET /`

Endpoint raiz de boas-vindas.

---

### 🎬 Films (7 endpoints)

##### `GET /films`

Retorna informações sobre todos os filmes da saga Star Wars.

**Parâmetros de Query (opcionais):**

- `search` (string): Busca filmes por título

#### `GET /films/{film_id}`

Retorna informações detalhadas sobre um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

#### `GET /films/{film_id}/characters`

Retorna todos os personagens que aparecem em um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

**Nota:** Este endpoint realiza múltiplas requisições em paralelo para buscar os dados de todos os personagens, otimizando o tempo de resposta.

#### `GET /films/{film_id}/planets`

Retorna todos os planetas que aparecem em um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

#### `GET /films/{film_id}/starships`

Retorna todas as naves estelares que aparecem em um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

#### `GET /films/{film_id}/vehicles`

Retorna todos os veículos que aparecem em um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

#### `GET /films/{film_id}/species`

Retorna todas as espécies que aparecem em um filme específico.

**Parâmetros:**

- `film_id` (int): ID do filme (1-6)

---

### 👥 Characters (7 endpoints)

#### `GET /characters`

Retorna todos os personagens.

**Parâmetros:** `?search=<nome>` para busca por nome.

#### `GET /characters/{character_id}`

Retorna detalhes de um personagem específico.

**Parâmetros:**

- `character_id` (int): ID do personagem

#### `GET /characters/{character_id}/films`

Retorna todos os filmes em que o personagem aparece.

**Parâmetros:**

- `character_id` (int): ID do personagem

#### `GET /characters/{character_id}/vehicles`

Retorna todos os veículos pilotados pelo personagem.

**Parâmetros:**

- `character_id` (int): ID do personagem

#### `GET /characters/{character_id}/starships`

Retorna todas as naves pilotadas pelo personagem.

**Parâmetros:**

- `character_id` (int): ID do personagem

#### `GET /characters/{character_id}/species`

Retorna a(s) espécie(s) do personagem.

**Parâmetros:**

- `character_id` (int): ID do personagem

#### `GET /characters/{character_id}/homeworld`

Retorna o planeta natal do personagem.

**Parâmetros:**

- `character_id` (int): ID do personagem

---

### 🪐 Planets (4 endpoints)

#### `GET /planets`

Retorna todos os planetas.

**Parâmetros:** `?search=<nome>` para busca por nome.

#### `GET /planets/{planet_id}`

Retorna detalhes de um planeta específico.

**Parâmetros:**

- `planet_id` (int): ID do planeta

#### `GET /planets/{planet_id}/films`

Retorna todos os filmes em que o planeta aparece.

**Parâmetros:**

- `planet_id` (int): ID do planeta

#### `GET /planets/{planet_id}/residents`

Retorna todos os residentes do planeta.

**Parâmetros:**

- `planet_id` (int): ID do planeta

---

### 🚀 Starships (4 endpoints)

#### `GET /starships`

Retorna todas as naves estelares.

**Parâmetros:** `?search=<nome>` para busca por nome ou modelo.

#### `GET /starships/{starship_id}`

Retorna detalhes de uma nave específica.

**Parâmetros:**

- `starship_id` (int): ID da nave

#### `GET /starships/{starship_id}/films`

Retorna todos os filmes em que a nave aparece.

**Parâmetros:**

- `starship_id` (int): ID da nave

#### `GET /starships/{starship_id}/pilots`

Retorna todos os pilotos da nave.

**Parâmetros:**

- `starship_id` (int): ID da nave

---

### 🛸 Vehicles (4 endpoints)

#### `GET /vehicles`

Retorna todos os veículos.

**Parâmetros:** `?search=<nome>` para busca por nome ou modelo.

#### `GET /vehicles/{vehicle_id}`

Retorna detalhes de um veículo específico.

**Parâmetros:**

- `vehicle_id` (int): ID do veículo

#### `GET /vehicles/{vehicle_id}/films`

Retorna todos os filmes em que o veículo aparece.

**Parâmetros:**

- `vehicle_id` (int): ID do veículo

#### `GET /vehicles/{vehicle_id}/pilots`

Retorna todos os pilotos do veículo.

**Parâmetros:**

- `vehicle_id` (int): ID do veículo

---

### 🦎 Species (5 endpoints)

#### `GET /species`

Retorna todas as espécies.

**Parâmetros:** `?search=<nome>` para busca por nome.

#### `GET /species/{species_id}`

Retorna detalhes de uma espécie específica.

**Parâmetros:**

- `species_id` (int): ID da espécie

#### `GET /species/{species_id}/films`

Retorna todos os filmes em que a espécie aparece.

**Parâmetros:**

- `species_id` (int): ID da espécie

#### `GET /species/{species_id}/people`

Retorna todos os personagens da espécie.

**Parâmetros:**

- `species_id` (int): ID da espécie

#### `GET /species/{species_id}/homeworld`

Retorna o planeta natal da espécie.

**Parâmetros:**

- `species_id` (int): ID da espécie

---

## 🧪 Testes Automatizados

O projeto implementa testes unitários abrangentes usando **pytest** com análise de cobertura via **pytest-cov**.

### Estrutura de Testes

- **Cliente de teste único**: Fixture `client` compartilhada em [conftest.py](tests/conftest.py) usando `TestClient` do FastAPI
- **Testes parametrizados**: URLs serializadas em arrays para testes eficientes de múltiplos endpoints
- **Cobertura completa**: Todos os 34 endpoints possuem testes automatizados

### Como Executar os Testes

#### Executar todos os testes:

```bash
pytest
```

#### Executar testes com relatório de cobertura:

```bash
pytest --cov=app --cov-report=term-missing
```

#### Gerar relatório HTML de cobertura:

```bash
pytest --cov=app --cov-report=html
```

O relatório HTML será gerado em `htmlcov/index.html`.

#### Executar testes de um módulo específico:

```bash
pytest tests/endpoints/test_characters.py
```

### Padrões de Teste Implementados

1. **Testes de resposta com array**: Validam que endpoints de listagem retornam `{"results": [...]}`
2. **Testes de busca**: Verificam funcionalidade de `?search=` em todos os recursos
3. **Testes de entidades**: Validam resposta de endpoints específicos (por ID)
4. **Testes de recursos relacionados**: Verificam endpoints de relacionamentos (ex: `/films/{id}/characters`)

### Fixture Compartilhada

Todos os testes utilizam a fixture `client` definida em [conftest.py](tests/conftest.py):

```python
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
```

Esta abordagem garante:

- ✅ **Isolamento**: Cada teste recebe um cliente limpo
- ✅ **Eficiência**: Cliente é reutilizado sem overhead de criação repetida
- ✅ **Consistência**: Todos os testes usam a mesma configuração

---

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

### Routers Modulares

A aplicação utiliza **6 routers independentes** organizados em [router.py](app/api/router.py), cada um responsável por um recurso específico:

| Router              | Prefixo       | Tag        | Arquivo                                          |
| ------------------- | ------------- | ---------- | ------------------------------------------------ |
| `films_router`      | `/films`      | Films      | [films.py](app/api/endpoints/films.py)           |
| `characters_router` | `/characters` | Characters | [characters.py](app/api/endpoints/characters.py) |
| `planets_router`    | `/planets`    | Planets    | [planets.py](app/api/endpoints/planets.py)       |
| `starships_router`  | `/starships`  | Starships  | [starships.py](app/api/endpoints/starships.py)   |
| `vehicles_router`   | `/vehicles`   | Vehicles   | [vehicles.py](app/api/endpoints/vehicles.py)     |
| `species_router`    | `/species`    | Species    | [species.py](app/api/endpoints/species.py)       |

**Benefícios:**

- ✅ Separação clara de responsabilidades
- ✅ Facilita manutenção e escalabilidade
- ✅ Organização automática na documentação do FastAPI
- ✅ Reduz acoplamento entre recursos

### Helpers Reutilizáveis

O arquivo [helpers.py](app/utils/helpers.py) contém **3 funções auxiliares** que eliminam duplicação de código:

#### `fetch_data(url: str, request: Request) -> dict`

Busca dados de uma única URL usando o cliente HTTP com cache.

```python
async def fetch_data(url: str, request: Request) -> dict:
    cache_client = request.app.state.cache_client
    response = await cache_client.get(url)
    return response.json()
```

**Uso:** Endpoints de detalhes (ex: `/films/1/`)

#### `get_all_from_url(url: str, data: str, request: Request) -> dict`

Busca uma entidade, extrai um array específico de URLs relacionadas e busca todas em paralelo.

```python
async def get_all_from_url(url: str, data: str, request: Request) -> dict:
    entity = await fetch_data(url, request)
    urls = entity.get(data, [])
    results = await fetch_multiple_urls(urls, request)
    return {"results": results}
```

**Uso:** Endpoints de recursos relacionados (ex: `/films/1/characters`)

#### `fetch_multiple_urls(urls: list[str], request: Request) -> list[dict]`

Executa múltiplas requisições HTTP em paralelo usando `asyncio.gather()`.

```python
async def fetch_multiple_urls(urls: list[str], request: Request) -> list[dict]:
    tasks = [fetch_data(url, request) for url in urls]
    return await asyncio.gather(*tasks)
```

**Benefício:** Reduz tempo de resposta drasticamente ao buscar dados relacionados.

**Exemplo prático:**

Buscar 18 personagens de um filme:

- **Sem paralelização**: ~1.8 segundos (18 × 100ms)
- **Com `asyncio.gather()`**: ~100-200ms (todas simultâneas)

### Padrão de Resposta

Todos os endpoints que retornam múltiplos recursos seguem o padrão:

```json
{
  "results": [
    {
      /* objeto 1 */
    },
    {
      /* objeto 2 */
    }
  ]
}
```

### Estrutura de Diretórios

```
app/
├── __init__.py
├── main.py              # Aplicação FastAPI principal
├── config.py            # Configuração do cache client e lifespan
├── api/
│   ├── __init__.py
│   ├── router.py        # Registro de todos os routers
│   └── endpoints/
│       ├── __init__.py
│       ├── films.py        # 7 endpoints de filmes
│       ├── characters.py   # 7 endpoints de personagens
│       ├── planets.py      # 4 endpoints de planetas
│       ├── starships.py    # 4 endpoints de naves
│       ├── vehicles.py     # 4 endpoints de veículos
│       └── species.py      # 5 endpoints de espécies
└── utils/
    ├── __init__.py
    └── helpers.py       # 3 funções auxiliares reutilizáveis
tests/
├── __init__.py
├── conftest.py          # Fixture 'client' compartilhada
├── test_main.py         # Testes do endpoint raiz
└── endpoints/
    ├── __init__.py
    ├── test_films.py
    ├── test_characters.py
    ├── test_planets.py
    ├── test_starships.py
    ├── test_vehicles.py
    └── test_species.py
prompts/
├── 01.md                # Implementação inicial
├── 02.md                # Expansão da API
├── 03.md                # Atualização de documentação
└── Context.md           # Contexto do projeto
```

**Arquitetura modular** que facilita:

- ✅ Escalabilidade horizontal (novos recursos)
- ✅ Manutenção isolada por recurso
- ✅ Testes organizados espelhando estrutura da aplicação
- ✅ Reutilização de código via helpers

## � Organização de Prompts

O projeto mantém um histórico estruturado dos prompts utilizados durante o desenvolvimento na pasta `prompts/`:

```
prompts/
├── 01.md          # Implementação inicial da API (estrutura base)
├── 02.md          # Expansão com todos os recursos (characters, planets, etc.)
├── 03.md          # Atualização da documentação e testes
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
