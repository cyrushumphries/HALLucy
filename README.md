# HALLucy

**HALLucy** is a creative unified visual programming environment for building real‑time music, real‑time visual effects, and audio‑reactive art.

With **HALLucy** you can:
- create music using modular building blocks,
- design visualisations and VFX that react to sound,
- create generative art driven by audio,
- experiment freely through an intuitive visual programming interface,
- be guided through your creative flow by the onboarded intelligence **Lucy**

In the future, **HALLucy** will also support tangible programming using physical tokens.

## About

### Inspiration
Years ago, I discovered the (now archived) VSXU project by [vovoid](https://github.com/vovoid/vsxu). Its visual programming approach to audio-reactive graphics fascinated me, but the project was difficult to revive due to runtime segmentation faults and an, for me, complex and unfamiliar tech stack.

Another source of inspiration is the [Reactable](https://reactable.com/), a tangible music instrument powered by [reacTIVision](https://github.com/mkalten/reacTIVision). Its physical tokens are essentially a form of visual programming.

**HALLucy** aims to combine both worlds: **real-time music production + visual effects + visual programming**,\
with the long-term goal of supporting tangible tokens for hands-on creativity.

> [!NOTE]
> No code from both inspiration projects has been used. 

### The Project

To combine the visual programming, with the real-time music and visual processing,
**HALLucy** is build on two technologies:
- Python: for the graphical user interface and visual programming (using DearPyGui),
- Rust: for the high-performance engine, that must compute audio and visuals in (near) real-time.

This project is also my personal journey into learning Rust.

### Currently Supported Features

- Visual programming using a node-based graph editor
- Drag-and-drop node creation
- Node Explorer listing all available building nodes
- Basic nodes (no real computation yet)

### Roadmap
- Rust engine with real-time audio processing
- Binding-layer between Python-gui and Rust-engine
- Actual audio node processing
- More node types for audio
- Lucy: your guiding intelligence with how-to's, tricks and tutorials
- Extending to the vfx aspect with shader pipeline
- More node types for vfx
- ...
- (much later) Tangible Tokens

### Why HALLucy?

The name combines:
- **HALL**: a classic reverb type in audio
- **Hallucination**: surreal, dreamlike visual effects
- **Lucy**: the creative intelligence guiding you through the system

Forming **HALLucy** an environment where sound and vision blend into creative hallucinations.

## Contributors

[**cyrushumphries**](https://github.com/cyrushumphries)

## Licence

[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

**HALLucy**

Copyright &copy; 2026  **cyrushumphries**

Licensed under the EUPL-1.2 (the "Licence");\
You may not use this work except in compliance with the Licence.\
You may obtain a copy of the Licence, available in the 23 official\
languages of the European Union, at: <https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>
