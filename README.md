# lib-version-remla25-team12

A lightweight utility library that exposes the version of the installed Python package. Designed for projects that need dynamic version resolution during development or deployment.

## Overview

This library provides a `VersionUtil` class that retrieves the package version using [PEP 621-compliant](https://www.python.org/dev/peps/pep-0621/) metadata or falls back to a `"dev"` string if not installed as a package.

## Project Structure

<pre>
lib-version/
├── lib_version/          # Main package implementation
│   └── version_util.py   # Contains VersionUtil class
├── tests/                # Unit tests (if any)
├── .github/              # GitHub Actions workflows
├── pyproject.toml        # Poetry configuration with dynamic versioning
├── .gitignore
└── README.md
</pre>

## Installation

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/)

### Install locally with Poetry

```bash
poetry install
```

## Usage

Import the utility and retrieve the current version:

```python
from lib_version.version_util import VersionUtil

print(VersionUtil.get_version())
```

If the package is not installed via Poetry or wheel:

```text
"dev"
```

If installed from a tagged release:

```text
"0.1.0"
```

## Dynamic Versioning

This project uses `poetry-dynamic-versioning` to derive the version from Git tags.

- Git tag format: `vX.Y.Z` (e.g., `v1.0.0`)
- The version is automatically injected at build time.

## Release Workflow

A GitHub Actions workflow builds the project on every version tag push:

```yaml
on:
  push:
    tags:
      - "v[0-9]+.[0-9]+.[0-9]+"
```

## License

MIT License