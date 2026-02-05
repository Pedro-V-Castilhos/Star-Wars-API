# Star Wars API

API REST de alta performance para consumo de dados do universo Star Wars, operando como camada intermediária entre aplicações cliente e a [SWAPI](https://swapi.dev/). Implementa cache HTTP com persistência SQLite, validação completa de erros HTTP, paginação de resultados, busca parametrizada e ordenação customizável.

## ✨ Principais Características

- 🚀 **34 endpoints RESTful** organizados em 6 recursos principais
- 🔍 **Sistema de busca** via query parameter `?search=`
- 📄 **Paginação configurável** com `?page=`
- 🔄 **Ordenação de resultados** com `?order_by=` e `?reverse=`
- ✅ **Tratamento robusto de exceções** (nunca retorna HTTP 500)
- ⚡ **Cache HTTP automático** com backend SQLite assíncrono
- 🧪 **Cobertura de testes unitários** com pytest e pytest-cov
- 📚 **Documentação OpenAPI** automática com Swagger UI e ReDoc
- ☁️ **Deploy em produção** no Google Cloud Platform via Cloud Run e API Gateway

## 🌐 Acesso à API em Produção

A API está disponível em produção através do Google Cloud API Gateway:

### **URL Base de Produção:**

```
https://sw-api-b5ifb19a.ue.gateway.dev/
```

### **Exemplos de Uso:**

```bash
# Listar todos os filmes
curl https://sw-api-b5ifb19a.ue.gateway.dev/films/

# Buscar personagem por nome
curl https://sw-api-b5ifb19a.ue.gateway.dev/characters/?search=luke

# Obter detalhes de um planeta
curl https://sw-api-b5ifb19a.ue.gateway.dev/planets/1

# Listar naves ordenadas por nome
curl https://sw-api-b5ifb19a.ue.gateway.dev/starships/?order_by=name
```

### **Documentação Interativa em Produção:**

- **Swagger UI**: [https://sw-api-b5ifb19a.ue.gateway.dev/docs](https://sw-api-b5ifb19a.ue.gateway.dev/docs)
- **ReDoc**: [https://sw-api-b5ifb19a.ue.gateway.dev/redoc](https://sw-api-b5ifb19a.ue.gateway.dev/redoc)

> **Nota:** A API em produção utiliza autenticação IAM gerenciada pelo Google Cloud para comunicação entre API Gateway e Cloud Run, garantindo segurança e controle de acesso.

## 🚀 Tecnologias

### Produção

- **Python 3.14**
- **FastAPI 0.128.0** - Framework web moderno e de alta performance
- **httpx 0.28.1** - Cliente HTTP assíncrono
- **hishel 1.1.8** - Sistema de cache HTTP com suporte SQLite
- **anysqlite 0.0.5** - Driver SQLite assíncrono
- **uvicorn 0.40.0** - Servidor ASGI

### Testes

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

## 🎯 Execução Local (Desenvolvimento)

Para desenvolvimento e testes locais, você pode executar a API em sua máquina:

### Modo de desenvolvimento (com reload automático):

```bash
uvicorn app.main:app --reload
```

### Modo de produção local:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Com porta customizada:

```bash
uvicorn app.main:app --reload --port 3000
```

A API estará disponível localmente em: `http://localhost:8000`

### 📖 Documentação Automática (Ambiente Local)

Em ambiente local, a documentação interativa estará disponível em:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

> **Recomendação:** Para testar a API completa, utilize o [ambiente de produção](#-acesso-à-api-em-produção) que já está configurado e disponível.

## ☁️ Implementação Google Cloud Platform

A API foi implementada em ambiente de produção utilizando serviços da Google Cloud Platform (GCP), seguindo arquitetura serverless com gerenciamento de acesso via Identity and Access Management (IAM).

### Arquitetura de Deploy

#### 1. **Containerização com Docker**

A aplicação foi containerizada utilizando o [Dockerfile](Dockerfile) presente no repositório:

```dockerfile
FROM python:3.11.14-alpine3.23
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app
EXPOSE 8080
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
```

**Características da imagem:**

- Base image Alpine Linux para otimização de tamanho
- Variáveis de ambiente Python otimizadas para produção
- Porta configurável via variável de ambiente `$PORT`
- Servidor ASGI Uvicorn para alta performance

#### 2. **Deploy no Cloud Run**

O container Docker foi implantado no **Google Cloud Run**, serviço serverless gerenciado que oferece:

- Auto-scaling baseado em demanda
- Cobrança por uso (pay-per-request)
- HTTPS nativo e certificados gerenciados
- Validação IAM para controle de acesso

**Endpoint do Cloud Run:**

```
https://sw-api-874003816990.southamerica-east1.run.app
```

#### 3. **Documentação OpenAPI com Swagger**

Foi criado o arquivo [swagger.yaml](swagger.yaml) seguindo especificação OpenAPI 2.0, documentando:

- Todos os 34 endpoints da API
- Parâmetros de query (search, page, order_by, reverse)
- Schemas de resposta
- Definições de recursos

O arquivo aponta para o backend do Cloud Run, permitindo validação da API em produção.

#### 4. **API Gateway**

O [swagger.yaml](swagger.yaml) foi utilizado para provisionar um **API Gateway** no Google Cloud, oferecendo:

- Ponto de entrada unificado para a API
- Gerenciamento de tráfego e rate limiting
- Autenticação e autorização via IAM
- Monitoramento e logging centralizado

### 🔗 URL Pública de Produção

**A API está disponível publicamente através do API Gateway:**

```
https://sw-api-b5ifb19a.ue.gateway.dev
```

**Endpoints principais:**

- Base: `https://sw-api-b5ifb19a.ue.gateway.dev/`
- Filmes: `https://sw-api-b5ifb19a.ue.gateway.dev/films/`
- Personagens: `https://sw-api-b5ifb19a.ue.gateway.dev/characters/`
- Planetas: `https://sw-api-b5ifb19a.ue.gateway.dev/planets/`
- Naves: `https://sw-api-b5ifb19a.ue.gateway.dev/starships/`
- Veículos: `https://sw-api-b5ifb19a.ue.gateway.dev/vehicles/`
- Espécies: `https://sw-api-b5ifb19a.ue.gateway.dev/species/`

**Documentação interativa:**

- Swagger UI: `https://sw-api-b5ifb19a.ue.gateway.dev/docs`
- ReDoc: `https://sw-api-b5ifb19a.ue.gateway.dev/redoc`

#### 5. **Fluxo de Requisições**

```
Cliente → API Gateway → Cloud Run (Container) → SWAPI
          (IAM Auth)     (IAM Auth)           (Cache HTTP)
```

### Segurança

- ✅ Autenticação IAM entre API Gateway e Cloud Run
- ✅ HTTPS obrigatório em todas as comunicações
- ✅ Validação de requisições no Gateway
- ✅ Isolamento de rede do container

### Monitoramento

- Cloud Logging para análise de logs
- Cloud Monitoring para métricas de performance
- Traces distribuídos para debugging

## 📚 Endpoints da API

A API fornece **34 endpoints** organizados em 6 recursos principais.

### 🔍 Parâmetros de Busca por Recurso

O parâmetro `search` permite filtrar resultados com base em campos específicos de cada recurso. A busca é delegada à API SWAPI, que realiza correspondência parcial (case-insensitive) nos campos especificados:

| Recurso         | Endpoint      | Campo(s) Pesquisado(s) | Exemplo                                      |
| --------------- | ------------- | ---------------------- | -------------------------------------------- |
| **Personagens** | `/characters` | `name`                 | `?search=luke` - busca por nome              |
| **Filmes**      | `/films`      | `title`                | `?search=empire` - busca por título          |
| **Planetas**    | `/planets`    | `name`                 | `?search=tatooine` - busca por nome          |
| **Naves**       | `/starships`  | `name`, `model`        | `?search=falcon` - busca por nome ou modelo  |
| **Veículos**    | `/vehicles`   | `name`, `model`        | `?search=speeder` - busca por nome ou modelo |
| **Espécies**    | `/species`    | `name`                 | `?search=wookiee` - busca por nome           |

**Observações importantes:**

- A busca é processada pela SWAPI, não pela aplicação
- Correspondência parcial: `?search=sky` encontra "Skywalker", "Skye", etc.
- Case-insensitive: maiúsculas e minúsculas são ignoradas
- Naves e veículos permitem busca em dois campos simultaneamente

### 🆕 Recursos Avançados dos Endpoints

Todos os endpoints de listagem suportam os seguintes query parameters:

| Parâmetro  | Tipo    | Descrição                       | Exemplo          |
| ---------- | ------- | ------------------------------- | ---------------- |
| `search`   | string  | Busca por termo no recurso      | `?search=Luke`   |
| `page`     | integer | Número da página para paginação | `?page=2`        |
| `order_by` | string  | Campo para ordenar resultados   | `?order_by=name` |
| `reverse`  | boolean | Inverte ordem de classificação  | `?reverse=true`  |

**Exemplos de uso combinado:**

- `GET /characters?search=skywalker&order_by=name`
- `GET /films?page=1&order_by=title&reverse=true`
- `GET /planets?search=tatooine`

---

### 🏠 Root

#### `GET /`

Endpoint raiz de boas-vindas.

---

### 🎬 Films (7 endpoints)

#### **`GET /films`**

Retorna todos os filmes da saga Star Wars.

- ✅ Suporta: `search`, `page`, `order_by`, `reverse`
- **Exemplos:**
  - `/films/` - Retorna todos os filmes (todas as páginas agregadas)
  - `/films/?search=empire` - Busca filmes com "empire" no título
  - `/films/?page=1` - Retorna primeira página (formato SWAPI original)
  - `/films/?order_by=title&reverse=true` - Ordena por título (Z-A)

#### **`GET /films/{film_id}`**

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

#### **`GET /characters`**

Retorna todos os personagens.

- ✅ Suporta: `search`, `page`, `order_by`, `reverse`

#### **`GET /characters/{character_id}`**

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

#### **`GET /planets`**

Retorna todos os planetas.

- ✅ Suporta: `search`, `page`, `order_by`, `reverse`

#### **`GET /planets/{planet_id}`**

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

#### **`GET /starships`**

Retorna todas as naves estelares.

- ✅ Suporta: `search`, `page`, `order_by`, `reverse`

#### **`GET /starships/{starship_id}`**

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

#### **`GET /vehicles`**

Retorna todos os veículos.

- ✅ Suporta: `search`, `page`, `order_by`, `reverse`

#### **`GET /vehicles/{vehicle_id}`**

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

#### **`GET /species`**

Retorna todas as espécies.

- ✅ Suporta: `search`, `page`, `order_by`, `reverse`

#### **`GET /species/{species_id}`**

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

## ⚠️ Códigos de Erro da API

A API implementa **validação completa de erros** e nunca retorna HTTP 500 ao cliente. Todos os erros são tratados e retornam códigos HTTP apropriados:

| Código  | Erro                | Descrição                              | Exemplo                                                                  |
| ------- | ------------------- | -------------------------------------- | ------------------------------------------------------------------------ |
| **400** | Bad Request         | Parâmetros inválidos na requisição     | Campo de ordenação inválido, página negativa, query params desconhecidos |
| **404** | Not Found           | Recurso não encontrado                 | ID inexistente, campo não encontrado no recurso                          |
| **503** | Service Unavailable | Erro de rede ao acessar API externa    | Falha de conexão com SWAPI                                               |
| **504** | Gateway Timeout     | Timeout ao buscar dados da API externa | SWAPI não respondeu a tempo                                              |

### Exemplos de Mensagens de Erro:

#### **400 - Bad Request**

```json
{
  "detail": "Invalid query parameters: invalid_param. Allowed parameters: order_by, page, reverse, search"
}
```

```json
{
  "detail": "The 'page' parameter must be a positive integer greater than zero"
}
```

```json
{
  "detail": "Invalid sorting field: 'invalid_field'. Check the available fields for this resource"
}
```

#### **404 - Not Found**

```json
{
  "detail": "Resource not found"
}
```

```json
{
  "detail": "Field 'invalid_field' not found in the resource"
}
```

#### **503/504 - External API Errors**

```json
{
  "detail": "Network error while fetching data from external API"
}
```

```json
{
  "detail": "Timeout while fetching data from external API"
}
```

### Validações Implementadas:

✅ **Validação de Query Parameters:**

- Rejeita parâmetros desconhecidos
- Lista parâmetros permitidos na mensagem de erro

✅ **Validação de Paginação:**

- Página deve ser número inteiro positivo > 0
- Mensagens de erro descritivas

✅ **Validação de Ordenação:**

- Verifica se o campo existe no recurso
- Valida tipo do campo (apenas string ou int)

✅ **Validação de Recursos:**

- Detecta IDs inexistentes (404)
- Trata campos ausentes em recursos

✅ **Tratamento de Erros Externos:**

- Timeout da API externa
- Erros de rede
- Respostas HTTP inválidas

---

## ⚠️ Avisos Importantes

### Inconsistências nos Dados da API Fonte

Esta API consome dados da [SWAPI (Star Wars API)](https://swapi.dev), que é mantida pela comunidade e pode conter inconsistências estruturais nos dados retornados:

**Problemas conhecidos:**

- ❌ **Dados faltantes**: Alguns recursos possuem campos vazios ou nulos
- ❌ **Índices ausentes**: Certos IDs podem não existir na sequência
- ❌ **Arrays vazios**: Relacionamentos podem retornar listas vazias mesmo quando deveriam conter dados
- ❌ **URLs inválidas**: Algumas referências de recursos podem apontar para endpoints inexistentes

**Exemplos de inconsistências:**

```json
// Exemplo: Personagem com homeworld null
{
  "name": "Character Name",
  "homeworld": null,
  "films": []
}

// Exemplo: Índices faltantes na sequência
// /api/species/1/ existe
// /api/species/2/ retorna 404
// /api/species/3/ existe
```

**Impacto na aplicação:**

- Esta API replica fielmente os dados da SWAPI, incluindo suas inconsistências
- Erros 404 podem ocorrer para IDs válidos na sequência numérica
- Campos vazios são retornados conforme recebidos da fonte
- A validação implementada trata esses casos retornando códigos HTTP apropriados

**Recomendação:** Implemente tratamento de dados ausentes nas aplicações cliente que consomem esta API.

**Consulte a documentação oficial:** [https://swapi.dev](https://swapi.dev)

---

## 🧪 Testes Automatizados

O projeto implementa testes unitários abrangentes usando **pytest** com análise de cobertura via **pytest-cov**.

### Testes de Validação

Além dos testes funcionais, o projeto inclui **testes de validação de erros** para garantir que a API retorne os códigos HTTP corretos:

#### Testes Positivos

- ✅ Resposta com array de resultados (`results`)
- ✅ Busca por termo (`?search=`)
- ✅ Paginação (`?page=`)
- ✅ Ordenação (`?order_by=` e `?reverse=`)
- ✅ Detalhes de recursos individuais

#### Testes Negativos (Validação de Erros)

- ✅ **404** - Recurso não encontrado
- ✅ **400** - Campo de ordenação inválido
- ✅ **400** - Número de página inválido
- ✅ **400** - Query parameters desconhecidos

### Estrutura de Testes Unificada

O projeto utiliza **helpers reutilizáveis** para eliminar duplicação nos testes:

**Arquivo:** [tests/utils/helpers.py](tests/utils/helpers.py)

```python
# Helpers para testes positivos
- test_results_in_response()
- test_response_by_field()
- test_search_in_results()
- test_pagination()
- test_ordering()

# Helpers para testes negativos
- test_not_found_response()
- test_invalid_parameter_response()
- test_invalid_ordering_response()
- test_invalid_pagination_response()
```

**Benefícios:**

- ✅ Reduz duplicação de código nos testes
- ✅ Facilita manutenção e adição de novos testes
- ✅ Garante consistência entre testes de diferentes recursos

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

#### Executar apenas testes de validação de erros:

```bash
pytest -k "not_found or invalid"
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

A aplicação utiliza uma arquitetura em camadas com foco em performance, reutilização e robustez:

### Validação Completa de Erros

O projeto implementa um sistema robusto de validação que **garante que a API nunca retorne HTTP 500**:

**Arquivo:** [app/utils/errors.py](app/utils/errors.py)

```python
# Exceções customizadas
- ResourceNotFoundError      # Para recursos não encontrados (404)
- InvalidOrderFieldError      # Para campos de ordenação inválidos (400)
- InvalidPageParameterError   # Para páginas inválidas (400)
- InvalidQueryParameterError  # Para query params inválidos (400)
- ExternalAPIError           # Para erros da API externa (503/504)
```

**Arquivo:** [app/utils/helpers.py](app/utils/helpers.py)

```python
# Funções de validação
- validate_page_parameter()      # Valida parâmetro page
- validate_order_by_field()      # Valida campo de ordenação
- validate_query_params()        # Valida query parameters permitidos
```

**Onde a validação acontece:**

1. **Camada de Endpoint**: Valida query parameters recebidos
2. **Camada de Helper**: Valida parâmetros de paginação e ordenação
3. **Camada HTTP**: Captura erros de rede, timeout e HTTP da API externa

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

O arquivo [app/utils/helpers.py](app/utils/helpers.py) contém **5 funções auxiliares** que eliminam duplicação de código:

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
    ├── errors.py        # 🆕 5 classes de erro customizadas
    └── helpers.py       # 🆕 5 funções auxiliares + 3 validações
tests/
├── __init__.py
├── conftest.py          # Fixture 'client' compartilhada
├── test_main.py         # Testes do endpoint raiz
├── endpoints/
│   ├── __init__.py
│   ├── test_films.py        # 🆕 Inclui testes de validação
│   ├── test_characters.py   # 🆕 Inclui testes de validação
│   ├── test_planets.py      # 🆕 Inclui testes de validação
│   ├── test_starships.py    # 🆕 Inclui testes de validação
│   ├── test_vehicles.py     # 🆕 Inclui testes de validação
│   └── test_species.py      # 🆕 Inclui testes de validação
└── utils/
    ├── __init__.py
    └── helpers.py       # 🆕 Helpers reutilizáveis para testes
prompts/
├── 01.md                # Implementação inicial
├── 02.md                # Expansão da API
├── 03.md                # Testes e documentação
├── 04.md                # 🆕 Validação de erros
├── 05.md                # 🆕 Atualização da documentação
└── Context.md           # Contexto do projeto
```

**Arquitetura modular** que facilita:

- ✅ Escalabilidade horizontal (novos recursos)
- ✅ Manutenção isolada por recurso
- ✅ Testes organizados espelhando estrutura da aplicação
- ✅ Reutilização de código via helpers
- ✅ **Validação robusta de erros em todas as camadas**

## � Organização de Prompts

O projeto mantém um histórico estruturado dos prompts utilizados durante o desenvolvimento na pasta `prompts/`:

```
prompts/
├── 01.md          # Implementação inicial da API (estrutura base)
├── 02.md          # Expansão com todos os recursos (characters, planets, etc.)
├── 03.md          # Testes automatizados e documentação
├── 04.md          # 🆕 Implementação de validação de erros completa
├── 05.md          # 🆕 Atualização da documentação
├── 06.md          # 🆕 Atualização da documentação
└── Context.md     # Contexto e instruções para o desenvolvimento
```

Esta organização permite:

- 📝 Rastreabilidade das decisões de desenvolvimento
- 🔄 Facilita replicação e entendimento do processo
- 📚 Serve como documentação evolutiva do projeto- 🎯 Demonstra a evolução incremental da aplicação

---

## 🎓 Princípios de Engenharia de Software

Este projeto implementa princípios consolidados de engenharia de software:

### 1. Validação Defensiva

- Validação de dados de entrada em todas as camadas
- Sanitização de parâmetros externos antes do processamento
- Retorno de códigos de status HTTP semanticamente corretos
- Tratamento explícito de exceções com mensagens descritivas

### 2. DRY (Don't Repeat Yourself)

- Helpers reutilizáveis para eliminação de duplicação de código
- Exceções customizadas para tratamento específico de domínio
- Fixtures compartilhadas em testes para consistência
- Funções auxiliares de teste para validação de cenários comuns

### 3. Otimização de Performance

- Cache HTTP com persistência SQLite assíncrona
- Paralelização de requisições com `asyncio.gather()`
- Cliente HTTP global com gerenciamento de lifecycle
- Minimização de I/O bloqueante

### 4. Design para Testabilidade

- Injeção de dependências via `Request.app.state`
- Testes parametrizados para cobertura eficiente
- Fixtures pytest para isolamento de testes
- Cobertura de happy path e edge cases

### 5. Documentação como Código

- Documentação OpenAPI gerada automaticamente via type hints
- README estruturado com exemplos práticos
- Histórico versionado de decisões arquiteturais
- Comentários descritivos em código complexo

---

## 🔮 Propostas Futuras

O projeto está em constante evolução. As seguintes funcionalidades estão planejadas para implementação futura:

### 1. **CI/CD Automático**

**Objetivo:** Automatizar pipeline de integração e deploy contínuo.

**Implementação planejada:**

- GitHub Actions para execução automática de testes
- Build automático da imagem Docker em cada push
- Deploy automático no Cloud Run após aprovação
- Validação de cobertura de testes mínima (threshold)
- Análise estática de código com pylint/flake8
- Versionamento semântico automático

**Benefícios:**

- Redução de erros humanos no deploy
- Feedback rápido sobre qualidade do código
- Deploys mais frequentes e confiáveis
- Rastreabilidade de mudanças

### 2. **Opções de Listagem para Arrays de URL**

**Objetivo:** Permitir ordenação e paginação de recursos relacionados.

**Funcionalidade proposta:**

Atualmente, endpoints de relacionamento retornam arrays simples:

```bash
# Estado atual
GET /characters/1/films
# Retorna: {"results": [{film1}, {film2}, {film3}]}
```

**Nova funcionalidade:**

```bash
# Ordenar filmes do personagem por título
GET /characters/1/films?order_by=title

# Ordenar naves do personagem por nome (descendente)
GET /characters/1/starships?order_by=name&reverse=true

# Paginar veículos do filme
GET /films/1/vehicles?page=1&order_by=model
```

**Endpoints afetados:**

- `/films/{id}/characters`, `/films/{id}/planets`, `/films/{id}/starships`, etc.
- `/characters/{id}/films`, `/characters/{id}/vehicles`, `/characters/{id}/starships`, etc.
- Todos os 21 endpoints de recursos relacionados

**Implementação técnica:**

- Aplicar ordenação nos resultados agregados após busca paralela
- Manter paralelização de requisições para performance
- Validar campos de ordenação específicos para cada tipo de recurso

**Benefícios:**

- Maior flexibilidade para aplicações cliente
- Melhor UX em listagens longas
- Consistência com endpoints de listagem principal

### 3. **Outras Melhorias Planejadas**

- **Rate Limiting**: Implementar limites de taxa por IP/cliente
- **Métricas**: Dashboard de uso e performance da API
- **Cache Configurável**: TTL customizável por recurso
- **Webhooks**: Notificações de mudanças nos dados
- **GraphQL**: Endpoint alternativo para queries complexas

## 👤 Autor

**Pedro V. Castilhos**

- GitHub: [@Pedro-V-Castilhos](https://github.com/Pedro-V-Castilhos)
