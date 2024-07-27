Here's a revised version of your `README.md` with the requested changes:

```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">AI-TICTACTOE-GAME</h1>
</p>
<p align="center">
    <em><code>► An unbeatable Tic-Tac-Toe game</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

The AI-TicTacToe-Game project features an unbeatable Tic-Tac-Toe game using advanced algorithms. The game provides two options for running: 
- **Alpha-Beta Pruning** 
- **Minimax Algorithm**

These algorithms ensure that the game is impossible to beat, providing an optimal experience.

---

##  Features

- Unbeatable Tic-Tac-Toe game
- Two algorithm options: Alpha-Beta Pruning and Minimax
- Interactive command-line interface

---

##  Repository Structure

```sh
└── AI-TicTacToe-Game/
    ├── README.md
    ├── assets
    │   └── font.ttf
    ├── main.py
    └── src
        ├── __init__.py.py
        ├── __pycache__
        ├── alpha_beta.py
        ├── game.py
        ├── gui.py
        └── minimax.py
```

---

##  Modules

<details closed><summary>.</summary>

| File               | Summary                         |
| ---                | ---                             |
| [main.py](main.py) | Entry point of the game          |

</details>

<details closed><summary>src</summary>

| File                                 | Summary                         |
| ---                                  | ---                             |
| [alpha_beta.py](src/alpha_beta.py)   | Implements the Alpha-Beta Pruning algorithm |
| [gui.py](src/gui.py)                 | Contains GUI-related code        |
| [__init__.py.py](src/__init__.py.py) | Initialization for the package    |
| [minimax.py](src/minimax.py)         | Implements the Minimax algorithm |
| [game.py](src/game.py)               | Core game logic                  |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the AI-TicTacToe-Game repository:
>
> ```console
> $ git clone <repository-url>
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd AI-TicTacToe-Game
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run AI-TicTacToe-Game using the command below:
> ```console
> $ python main.py
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ pytest
> ```

---

##  Project Roadmap

- [X] Implemented Alpha-Beta Pruning algorithm
- [X] Implemented Minimax algorithm
- [ ] Enhance GUI for better user experience

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://local/AI-TicTacToe-Game/issues)**: Submit bugs found or log feature requests for the `AI-TicTacToe-Game` project.
- **[Submit Pull Requests](https://local/AI-TicTacToe-Game/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local/AI-TicTacToe-Game/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone <repository-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{/AI-TicTacToe-Game/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=AI-TicTacToe-Game">
   </a>
</p>
</details>

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---

<p align="center">
  <img src="path/to/first-image.png" alt="First Image" width="400">
  <img src="path/to/second-image.png" alt="Second Image" width="400">
</p>
```

### Notes:
1. Replace `<repository-url>` with the actual URL of your repository.
2. Replace `path/to/first-image.png` and `path/to/second-image.png` with the paths or URLs to your images.
