# sps_genai

FastAPI app with a bigram text generator and spaCy word embeddings.

## Run with Docker
```bash
docker build -t sps-genai .
docker run -p 8000:80 sps-genai
```
Docs: http://127.0.0.1:8000/docs

## Endpoints
- `POST /generate`: `{"start_word": "bigram", "length": 5}`
- `POST /embedding`: `{"word": "apple"}` returns a 300-dimension vector
- `POST /similarity`: `{"word1": "apple", "word2": "orange"}`

## Example
```bash
curl -X POST http://127.0.0.1:8000/embedding \
  -H "Content-Type: application/json" \
  -d '{"word": "apple"}'
```