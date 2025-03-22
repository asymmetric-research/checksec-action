# Checksec Security Verification

[![](https://img.shields.io/badge/Marketplace-Checksec%20Security%20Verification-green.svg)](https://github.com/marketplace/actions/checksec-security-verification)

A GitHub Action to verify binary security mitigations using checksec.

## Description

This action scans ELF binaries to verify security mitigations such as RELRO, Stack Canary, NX, PIE, and more. It's useful for identifying potential security vulnerabilities in compiled binaries.

## Usage

```yaml
- name: Verify binary security
  uses: asymmetric-research/checksec-action@v1
  with:
    # Either directory or file must be specified
    directory: './build'    # Directory containing binaries to scan
    # OR
    file: './build/myapp'   # Single binary file to scan
    # Optional: Skip FORTIFY_SOURCE checks
    skip-fortify: 'true'    # Default is false
```

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `directory` | Directory to scan with checksec | No* | |
| `file` | File to scan with checksec | No* | |
| `skip-fortify` | Skip the FORTIFY_SOURCE check | No | `false` |

\* Either `directory` or `file` must be provided.

## Example Workflow

```yaml
name: Security Checks

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  checksec:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build application
        run: |
          # Your build commands here
          make
      
      - name: Verify binary security
        uses: asymmetric-research/checksec-action@v1
        with:
          directory: './build'
```

## How It Works

1. The action verifies that either a file or directory is specified
2. It sets up a cache for checksec to avoid downloading it on each run
3. If not cached, it downloads checksec version 3.0.2
4. It runs checksec against the specified file or directory
5. Results are processed by a Python script and presented in JSON format

The action shows security features present in your binaries and will fail if security issues are detected.

## Author

Asymmetric Research
