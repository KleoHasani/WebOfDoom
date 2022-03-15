<div id="header" align="center">
  <img src="https://media.giphy.com/media/FayHP89OV4WUzYUfIZ/giphy.gif" width="200"/>
</div>


# WebOfDoom

## Description

Webpage and API endpoint brute forcer.

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Clone](#clone)
    - [VENV](#venv)
    - [Activate](#activate)
  - [Install](#install)
  - [Start](#start)
  - [Stop](#stop)
- [Build](#build)
- [Usage](#usage)
- [Test](#test)

---

## Getting Started

- ## Requirements

  - [x] Python3 v3.10
  - [x] Poetry v1.1

- ## Setup

  - Clone

  ```shell
  git clone https://github.com/KleoHasani/WebOfDoom.git
  ```

  - VENV

  ```shell
  poetry shell
  ```

  - Activate

    - Windows

    ```shell
    .\.venv\Scripts\activate
    ```

    - *nix

    ```shell
    source .venv/bin/activate
    ```

- ## Install

```shell
poetry install
```

- ## Start

```shell
poetry run start
```

- ## Stop

**Disable venv for the project.**

```shell
deactivate
```

---

## Build

```shell
poetry build
```

---

## Usage

<div align="center">
  <img src=""/>
</div>

---

## Test

```shell
poetry run pytest
```

| File         | Test             | Description | Status   |
| :----------- | :--------------- | :---------- | :------- |
| test_true.py | test_always_true | Mock test.  | &#10003; |