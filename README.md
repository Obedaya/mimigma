# Mimigma

Mimigma is a modern and versatile Enigma machine emulator named after the Pokémon "Mimigma." This project is part of the "Software Engineering" course at my University.

## Changelog

*To be appended as updates and changes are made.*

## Introduction

Mimigma allows you to emulate different variants of the Enigma machine, including M1, M3, and Norway. With this tool, you can choose between various rotors and reflectors, set the rotors, ring settings, reflectors, and configure the plugboard. You also have the capability to save the state of your settings and import/export them for later use. Additionally, Mimigma supports user authentication and session state management. Users can be added or removed inside a configuration file, making it a collaborative and flexible solution.

## Installation

### Prerequisites

To use Mimigma, you need Docker and Docker Compose installed on your system.

---

Clone the repository:
```bash
git clone https://github.com/Obedaya/mimigma
```

Go into the directory:
```bash
cd mimigma
```

## Usage

```bash
docker-compose up --build
```

With testing enabled:
```bash
docker-compose --profile testing up --build
```

Then visit `http://localhost:8081` in your browser or the network address of your docker host.

The default username and password are `admin` and `password`. You should change it tho in the `user_config.json` file found at `backend/app/user_config.json`.