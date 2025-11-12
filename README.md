"# Freen – Voice, Vision, and Memory Companion

## 🌟 Overview
Freen is a personal AI companion that blends:
- Conversational intelligence powered by local Ollama models (Llama 3.1/3.2)
- Personal memory storage via Qdrant for contextual, emotionally aware responses
- Audio and vision hooks for eventual multimodal interactions

Use the project as a friendly assistant, a RAG playground, or a base for your own custom AI buddy.

## 🚀 Features
- Warm, empathetic chat experience with emotional tone detection
- Memory persistence using `FreenMemory` and Qdrant vector search
- Local-first model usage: no cloud OpenAI calls required
- Notebook quickstarts (`notebooks/`) plus executable FastAPI service scaffolding (`src/`)
- Extensible architecture (LangChain, LiteLLM, Transformers, Speech, Vision support)

## 📁 Project Layout
```
Freen/
├─ notebooks/               # Exploration & prototypes (setup, LLM, reminders, etc.)
├─ src/
│  ├─ api/                  # FastAPI app scaffolding (optional service)
│  └─ db/                   # Qdrant memory helpers, connection tests
├─ requirements.txt         # Python dependencies
└─ README.md                # You are here
```

## 🛠️ Prerequisites
- Python 3.12+
- Ollama (models: `llama3.2:latest`, `nomic-embed-text`)
- Qdrant (local Docker or Cloud endpoint)
- Optional: CUDA-capable GPU for faster inference

## ⚙️ Setup
1. Clone the repo and move into it  
   ```bash
   git clone <repo-url>
   cd Freen
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Populate `.env`  
   ```env
   QDRANT_URL=http://localhost:6333
   QDRANT_API_KEY=    # leave blank for local
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_EMBED_MODEL=nomic-embed-text
   OLLAMA_CHAT_MODEL=ollama/llama3.2:latest
   ```
4. Start services  
   - Ollama: `ollama serve`
   - Qdrant (Docker):  
     ```bash
     docker run -p 6333:6333 -p 6334:6334 -v qdrant_storage:/qdrant/storage qdrant/qdrant:latest
     ```

## 📓 Working with Notebooks
1. Launch Jupyter or VS Code notebooks.  
2. Execute `notebooks/00-setup.ipynb` to verify Ollama connectivity.  
3. Use `notebooks/01-llm_integration.ipynb` to test RAG + memory behavior.  
   - Add this cell first if `src` imports fail:
     ```python
     import os, sys
     sys.path.append(os.path.abspath(".."))
     ```
4. Explore extra features in other notebooks (reminders, voice, etc.).

## 🧠 Memory API Quick Peek
```python
from src.db.qdrant_memory import FreenMemory

memory = FreenMemory()
memory.add_memory("User loves learning Japanese greetings.")
top_hits = memory.get_relevant_memories("What does the user enjoy?")
```

## 🌐 Optional FastAPI Service
Spin up a chat endpoint (after configuring `.env`):
```bash
uvicorn src.api.main:app --reload
```
Then POST to `/chat` with `{ "session_id": "...", "user_input": "Hello!" }`.

## ✅ Troubleshooting
- `ModuleNotFoundError: 'src'`: add the project root to `sys.path` in notebooks.
- Embedding errors from Ollama: ensure `nomic-embed-text` is pulled and `OLLAMA_BASE_URL` is correct.
- Qdrant timeouts: check that the server is running (local Docker or cloud URL).
- Missing `.env`: copy `.env.example` (if provided) or create one using the snippet above.

## 🗺️ Roadmap Ideas
- Voice capture + TTS loop for real-time conversations
- Vision pipeline integration (OpenCV + image captioning)
- Memory pruning & summarization strategies
- GUI or mobile companion interface

## 🤝 Contributing
1. Fork & branch: `feature/your-idea`
2. Keep notebooks clean (restart & run all)
3. Ensure lint/tests pass (`python -m src.db.test_qdrant_connection`)
4. Submit a PR with a friendly summary 😄

## 📜 License
MIT License – feel free to remix and build your own Freen!
