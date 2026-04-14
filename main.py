from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router

app = FastAPI(
    title="Building Voice AI Agents with LiveKit and Deepgram",
    description="Build real-time voice AI with LiveKit, Deepgram STT/TTS, and tool calling",
    version="1.0.0",
)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(router)

@app.get("/")
async def root():
    return {"service": "voice-ai-livekit", "docs": "/docs"}
