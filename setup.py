from setuptools import setup, find_packages

setup(
    name='ai-assistant-call-bot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "fastapi", "uvicorn", "whisper", "openai", "coqui-ai", "TTS",
        "gradio", "aiortc", "numpy", "sounddevice", "onnxruntime",
        "webrtcvad", "chromadb", "tensorflow-federated", "transformers", "paho-mqtt"
    ],
    entry_points={
        'console_scripts': [
            'ai-call-bot=backend.main:app',
        ],
    },
)
