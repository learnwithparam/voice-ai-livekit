# Building Voice AI Agents with LiveKit and Deepgram

![learnwithparam.com](https://www.learnwithparam.com/ai-bootcamp/opengraph-image)

Build a real-time voice AI restaurant assistant. Integrate LiveKit for WebRTC audio, Deepgram for speech-to-text and text-to-speech, and enable voice agents to call tools and manage order state.

> Start learning at [learnwithparam.com](https://learnwithparam.com). Regional pricing available with discounts of up to 60%.

## What You'll Learn

- Real-time voice AI with LiveKit
- STT/TTS with Deepgram
- Voice agent architecture
- Tool calling for voice agents

## Tech Stack

- **LiveKit** - Real-time WebRTC audio streaming
- **Deepgram** - Speech-to-text and text-to-speech
- **FastAPI** - High-performance async Python web framework
- **LLM Provider Pattern** - Supports Fireworks, OpenRouter, OpenAI
- **Pydantic** - Data validation and type safety
- **Docker** - Containerized development

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (installed automatically by `make setup`)
- API keys for LiveKit, Deepgram, and an LLM provider

### Quick Start

```bash
# One command to set up and run
make dev

# Or step by step:
make setup          # Create .env and install dependencies
# Edit .env with your API keys
make run            # Start the FastAPI server
make run-agent      # Start the LiveKit voice agent worker (separate terminal)
```

### With Docker

```bash
make build          # Build the Docker image
make up             # Start the container
make logs           # View logs
make down           # Stop the container
```

### API Documentation

Once running, open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Challenges

Work through these incrementally to build the full application:

1. **The First Connection** - Set up LiveKit room and generate access tokens
2. **The Basic Agent** - Create a voice agent with STT, LLM, and TTS
3. **The Menu Tool** - Add a tool for the agent to read menu items
4. **The Order Tool** - Add a tool to add items to the customer's order
5. **The Order View Tool** - Add a tool to view the current order
6. **The Place Order Tool** - Add a tool to finalize and place orders
7. **The Frontend Integration** - Connect a web frontend to the voice agent
8. **Enhanced Features** - Add personalization, error handling, and advanced features

## Makefile Targets

```
make help           Show all available commands
make setup          Initial setup (create .env, install deps)
make dev            Setup and run (one command!)
make run            Start FastAPI server
make run-agent      Start the LiveKit voice agent worker
make build          Build Docker image
make up             Start container
make down           Stop container
make clean          Remove venv and cache
```

## Learn more

- Start the course: [learnwithparam.com/courses/voice-ai-agents-livekit](https://www.learnwithparam.com/courses/voice-ai-agents-livekit)
- AI Bootcamp for Software Engineers: [learnwithparam.com/ai-bootcamp](https://www.learnwithparam.com/ai-bootcamp)
- All courses: [learnwithparam.com/courses](https://www.learnwithparam.com/courses)
