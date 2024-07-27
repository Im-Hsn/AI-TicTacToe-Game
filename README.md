<p align="center">
    <h1 align="center">AI-TICTACTOE-GAME</h1>
</p>
<p align="center">
    <em><code>► An unbeatable Tic-Tac-Toe game with Alpha-Beta Pruning and Minimax algorithms</code></em>
</p>
<p align="center">
	<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>

<br><!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Modules](#modules)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Project Roadmap](#project-roadmap)
- [Acknowledgments](#acknowledgments)

<hr>

## Overview

The AI-TicTacToe-Game project provides an unbeatable Tic-Tac-Toe game using advanced algorithms. The game can be run using two different algorithms:

- **Alpha-Beta Pruning**: Optimizes the Minimax algorithm to reduce the number of nodes evaluated in the search tree.
- **Minimax Algorithm**: A classic algorithm that minimizes the possible loss for a worst-case scenario.

---

## Features

- **Unbeatable Game**: Ensures that the game is impossible to beat using either algorithm.
- **Interactive CLI**: Run the game and choose your algorithm via the command line.
- **Two Algorithm Options**: Choose between Alpha-Beta Pruning and Minimax for your gameplay.

---

## Repository Structure

```sh
└── AI-TicTacToe-Game/
    ├── README.md
    ├── assets
    │   └── font.ttf
    ├── main.py
    └── src
        ├── __init__.py
        ├── __pycache__
        ├── alpha_beta.py
        ├── game.py
        ├── gui.py
        └── minimax.py
```

---

## Modules

| File                                 | Summary                                               |
| ------------------------------------ | ----------------------------------------------------- |
| [main.py](main.py)                   | Entry point for the Tic-Tac-Toe game.                |
| [alpha_beta.py](src/alpha_beta.py)   | Implements the Alpha-Beta Pruning algorithm.         |
| [gui.py](src/gui.py)                 | Contains the graphical user interface code.          |
| [__init__.py](src/__init__.py)       | Initialization for the package.                      |
| [minimax.py](src/minimax.py)         | Implements the Minimax algorithm.                    |
| [game.py](src/game.py)               | Core logic for the Tic-Tac-Toe game.                 |

---

## Getting Started

### Installation

To install and run the AI-TicTacToe-Game, follow these steps:

1. **Clone the Repository:**

   ```console
   $ git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```console
   $ cd AI-TicTacToe-Game
   ```

### Usage

Run the AI-TicTacToe-Game using the following command:

```console
$ python main.py
```

---

## Project Roadmap

- [X] Implemented Alpha-Beta Pruning algorithm.
- [X] Implemented Minimax algorithm.
- [X] Enhance GUI for a better user experience.

---

[**Return to Top**](#table-of-contents)

<p align="center">
  <img src="path/to/first-image.png" alt="First Image" width="400">
  <img src="path/to/second-image.png" alt="Second Image" width="400">
</p>
