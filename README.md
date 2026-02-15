<p align="center">
  <img src="https://github.com/charinev/opnc/assets/83767351/1688cfe1-97de-46c7-9b97-65bcec242193" alt="CharIN Logo" width="200"/>
</p>

# Unified Error Codes

This repository contains the draft specification for Unified Error Codes. It represents a joint effort to standardize error codes and diagnostics across the entire EV charging ecosystem.

Here you can find the project materials related to **Unified Error Codes**, developed in the CharIN FG Charging Communication Subgroup - Error Codes.

> **Want to understand the vision and goals behind this project?** Read the [MANIFESTO](MANIFESTO.md).

---

## Table of Contents

- [Unified Error Codes](#unified-error-codes)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [How to Get a Copy of the Project](#how-to-get-a-copy-of-the-project)
    - [Step 1: Fork the repository](#step-1-fork-the-repository)
    - [Step 2: Clone your fork to your computer](#step-2-clone-your-fork-to-your-computer)
    - [Step 3: Add the original repository as "upstream"](#step-3-add-the-original-repository-as-upstream)
  - [How to Build the Specification Locally](#how-to-build-the-specification-locally)
    - [Step 1: Install Docker](#step-1-install-docker)
    - [Step 2: Build the PDF](#step-2-build-the-pdf)
    - [Step 3: View the result](#step-3-view-the-result)
  - [How to Contribute](#how-to-contribute)
  - [Project Structure](#project-structure)
  - [Governance](#governance)
  - [Disclaimer](#disclaimer)
  - [Licensing](#licensing)

---

## Prerequisites

Before you start, make sure you have the following installed on your computer:

1. **Git** — used to download and manage the project files.
   - **Windows:** Download from [git-scm.com](https://git-scm.com/download/win) and run the installer.
   - **macOS:** Open Terminal and run: `xcode-select --install`
   - **Linux (Ubuntu/Debian):** Open Terminal and run: `sudo apt install git`

2. **Docker** — used to build the specification without installing extra tools.
   - **Windows / macOS:** Download [Docker Desktop](https://www.docker.com/products/docker-desktop/).
   - **Linux:** Follow the [official install guide](https://docs.docker.com/engine/install/).

3. **A GitHub account** — sign up for free at [github.com](https://github.com/join).

To verify everything is installed, open a terminal (or Command Prompt on Windows) and run:

```bash
git --version
docker --version
```

Both commands should print a version number.

---

## How to Get a Copy of the Project

### Step 1: Fork the repository

A "fork" is your own personal copy of the project on GitHub.

1. Go to the project page on GitHub.
2. Click the **Fork** button in the top-right corner.
3. GitHub will create a copy under your account.

### Step 2: Clone your fork to your computer

"Cloning" downloads the project files to your machine so you can work on them.

Open a terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/unified-error-codes.git
```

> Replace `YOUR-USERNAME` with your actual GitHub username.

Then navigate into the project folder:

```bash
cd unified-error-codes
```

### Step 3: Add the original repository as "upstream"

This lets you keep your copy up to date with the latest changes from the main project.

```bash
git remote add upstream https://github.com/charinev/unified-error-codes.git
```

---

## How to Build the Specification Locally

The specification is built using [Docker](https://www.docker.com/), so you don't need to install Python or Sphinx on your machine — just Docker.

### Step 1: Install Docker

- **Windows / macOS:** Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
- **Linux:** Follow the [official install guide](https://docs.docker.com/engine/install/) for your distribution.

To verify Docker is installed, run:

```bash
docker --version
```

### Step 2: Build the PDF

From the project root folder, run:

```bash
docker run --rm -v $(pwd)/specification:/docs sphinxdoc/sphinx-latexpdf make latexpdf
```

> **On Windows (Command Prompt)**, replace `$(pwd)` with the full path:
> ```
> docker run --rm -v C:\path\to\unified-error-codes\specification:/docs sphinxdoc/sphinx-latexpdf make latexpdf
> ```

This will download the Sphinx image (first time only) and build the specification as a PDF.

### Step 3: View the result

The generated PDF is located at:

```
specification/_build/latex/unifiederrorcodes.pdf
```

Open it with any PDF viewer.

---

## How to Contribute

We welcome contributions from everyone! All contributions start with a GitHub Issue and follow a structured workflow:

**Issue -> Agreement -> Pull Request -> Review -> Merge**

- **Have a question or proposal?** Open a [GitHub Issue](../../issues).
- **Ready to submit changes?** Create a Pull Request.

For the full contribution workflow, review process, step-by-step PR instructions, see **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## Project Structure

```text
unified-error-codes/
├── README.md              ← You are here! Getting started guide.
├── MANIFESTO.md           ← Project vision, problem statement, and scope.
├── CONTRIBUTING.md        ← Detailed contribution guidelines and governance.
├── LICENSE                ← License information.
├── LICENSE_CODE           ← Apache-2.0 license (for code).
├── LICENSE_DOCS           ← CC-BY-4.0 license (for documentation).
├── NOTICE                 ← Legal notices.
└── specification/         ← The specification source files.
    ├── conf.py            ← Sphinx configuration.
    ├── index.rst          ← Main document entry point.
    ├── Makefile           ← Build script (Linux/macOS).
    ├── make.bat           ← Build script (Windows).
    └── _build/            ← Generated output (do not edit).
```

---

## Governance

This project is an open initiative led by the CharIN e.V. Working Group.
We welcome contributions from the entire e-mobility community. All discussions, proposals, and changes will be managed transparently through GitHub Issues and Pull Requests.

---

## Disclaimer

This specification should be seen as an addition to available industry standards and best practices.
It is developed by the community, and everyone is free and invited to contribute.

---

## Licensing

- **Code/tools:** [Apache License 2.0](LICENSE_CODE)
- **Documentation/specification:** [Creative Commons Attribution 4.0 (CC-BY-4.0)](LICENSE_DOCS)

All commits must include a `Signed-off-by:` line (use `git commit -s`).
