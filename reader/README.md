# Read Aloud (browser-only KittenTTS)

This folder is a self-contained static page. It does not alter other Everlearning content.

Open `index.html` from any static web host, e.g. GitHub Pages at `/reader/` if this repository publishes from its root.

## Features

- KittenTTS **Nano int8**, **Micro**, **Mini**, and **Nano fp32**
- All eight SDK voices, speech speed, playback, pause/resume/stop
- Sentence-based chunking for longer text, with WAV export
- On-device synthesis; no paid API key
- SDK generation analytics disabled (`analytics: false`)

## Dependencies

The HTML loads the official KittenTTS Web browser bundle through jsDelivr, pinned to upstream commit `c846fe92858f3447f4912226471f5a63983b3f94`. KittenTTS downloads model assets from Hugging Face, and ONNX Runtime WASM files from its configured CDN. Initial online access is required. Browser caching may retain models; fully offline hosting needs additional asset pinning/service-worker work.

SDK: [KittenTTS Web](https://github.com/KittenML/KittenTTS-web)

## Limitations

This is an initial implementation, not yet verified on iOS Safari or with actual model inference. Some mobile browsers may not allow automatic playback after lengthy asynchronous generation: use the native audio Play button in that case. Audio is assembled in memory and long books may exceed device resources. WAV output can be large; MP3 and progressive playback can be added later. Changing controls or pressing Stop during generation will discard the old result after the current synthesis section finishes.

The KittenTTS Web SDK is a developer preview; model compatibility, file hosting and browser support may change.
