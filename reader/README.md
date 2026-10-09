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

## Article import

Article loading stays in the existing static GitHub Pages site. There is no backend, CORS proxy, extraction API, account, or API key.

- **Load article:** fetches the supplied public HTTP(S) link directly, without cookies or a referrer. It works only when the target website permits browser access (CORS); HTTPS-hosted readers require HTTPS article links.
- **Preview:** Mozilla Readability extracts the main text locally. We can edit the preview and explicitly choose **Use this text in the reader** to replace the existing text.
- **Import a file:** opens saved `.html`, `.htm`, or `.txt` files locally, without uploading them. Copy-paste remains available, especially on phones.
- **Limits:** imports are capped at 5 MB and direct fetches time out after 20 seconds. PDF, login-protected, paywalled, and JavaScript-rendered content are not supported by this importer. Extraction is heuristic; review the preview for missing or extra content.
- **Inactive HTML:** source HTML is parsed in an inert template, active elements/resource attributes are removed, and only plain text is displayed. Imported scripts and media are never added to the live page.

The extractor is bundled at `vendor/Readability.js` from [Mozilla Readability 0.6.0](https://github.com/mozilla/readability/tree/0.6.0), unchanged (upstream Git blob `ad32a65c6b094139204ee8af9ae0d2c3a2d72da9`). Its license notice is preserved in the source and in `vendor/LICENSE.md`. It loads from the same static host as the reader.

Loading an article URL still requires internet access to that website. Speech model/runtime downloads are unchanged; there is no new requirement for server-side processing, but this does not make the whole app guaranteed offline.
