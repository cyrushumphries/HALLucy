# MusicVFX

**MusicVFX** is a visual programming tool for creating real time music and real time music visualisations.

**MusicVFX** allows you to:
- create music,
- create visualisations and visual effects based on your created music or other music inputs.

All via an easy to use visual programming interface, by visualy chaining different types of building blocks together.

Idealy this visual programming can be extended to tangible programming using physical tokens.


## About

### Inspiration
Years ago, i discovered the (now archieved) vsxu project by [vovoid](https://github.com/vovoid/vsxu), but never had the time to actually do something with it. VSXU focus was creating visuals based on music using a visual programming language. I tried rewiving the project in my lab, but bumped quickly into runtime segmentation faults, which where to difficult for me to debug, due to lack of knowledge on the used tech stack.

Another inspiration is the Reactable project with tangible tokens to create music. This project also discontinued.
The Reactable focused on creating music only using tangible elements, whcih is still very similar to visual programming.

The idea of MusicVFX is to combine both, the music production and the visual effects production, in one visual programming environment which idealy, at a later stage, can use tangible tokens to create art.

> [!NOTE]
> No code from both inspiration projects has been used. 

### The Project

To combine the visual programming, with the real-time music and visualisation production aspect,
**MusicVFX** is build on two technologies:
- Python: for the graphical userinterface and visual programming, easy extendable and fast to setup using dearpygui,
- Rust: for the engine, due to its high performance requirments to compute in (near) real-time.

### Currently Supported Features

- Visual Programming using a Visual Graph Editor and drag-drop functionality
- Node Explorer to list all available building nodes
- Nodes:
  - Audio:
    - Osc


### Roadmap

## How to setup MusicVFX


## Contributors

(**cyrushumphries**) [https://github.com/cyrushumphries]

## Licence

[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

**MusicVFX**

Copyright &copy; 2026  **MusicVFX Contributors** (see [README.md](README.md))

Licensed under the EUPL-1.2 (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at: <https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>
