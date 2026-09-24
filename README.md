# 🤖 AI Chatbot with LangGraph, Gemini API, Qdrant & Voice Mode

A multi-agent AI chatbot platform built with **FastAPI**, **LangGraph**, and **Google Gemini API**, featuring multi-tenant vector storage with **Qdrant**, cross-chat memory with **Mem0**, MCP tool integration, and real-time voice mode via **LiveKit**.

---

## 🚀 Quick Start with Docker

The easiest way to run the entire stack is using Docker Compose:

1. **Configure Environment**:
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

2. **Launch Services**:
   ```bash
   docker-compose up --build
   ```

- **Frontend UI**: http://localhost:3000
- **Backend API Docs**: http://localhost:8000/docs
- **Qdrant Dashboard**: http://localhost:6333/dashboard

---

## 🌟 Key Features

- **Multi-Agent Orchestration (LangGraph)**: Supervisor agent delegating tasks between Research and Web Scraper agents powered by Gemini (`gemini-2.5-flash`).
- **Google Gemini API Integration**: Replaced OpenAI with Gemini for low-latency reasoning and embeddings (`models/text-embedding-004`).
- **Multi-Tenant Vector Search (Qdrant)**: Isolated payload filtering by tenant ID for secure semantic search.
- **Cross-Chat Memory (Mem0)**: Long-term memory extraction to personalize user interactions across sessions.
- **MCP Tools**: Web search (Tavily) and web scraping (Firecrawl) via FastMCP.
- **Voice Assistant (LiveKit)**: WebRTC voice mode with Deepgram STT, Cartesia TTS, and Silero VAD.
- **React Frontend**: Modern Material-UI chat interface with real-time streaming and voice toggle.

---

## 🛠️ Local Setup (Without Docker)

### 1. Backend Setup

```bash
# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Qdrant (via Docker)
docker run -d -p 6333:6333 qdrant/qdrant

# Run MCP Tool Servers (in separate terminals)
python -m app.mcp_server.search_server
python -m app.mcp_server.web_scrapping_server

# Start Backend API
python app.py
```

### 2. LiveKit Voice Agent (Optional)

```bash
python app/agent/livekit_agent.py dev
```

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## ⚙️ Environment Variables (.env)

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key

# Qdrant
QDRANT_HOST=localhost
QDRANT_PORT=6333

# External Tools
TAVILY_API_KEY=your_tavily_key
FIRECRAWL_API_KEY=your_firecrawl_key

# LiveKit (Voice Mode)
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret
```

---

## 📜 License
Apache 2.0
