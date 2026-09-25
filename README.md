# Cryptography Toolkit

A command-line toolkit for exploring core cryptography concepts in Python.

## Features

- **File hashing** – generate a SHA hash of any file
- **Integrity check** – compare two files to detect tampering
- **AES encryption** – encrypt and decrypt messages with AES-GCM
- **RSA encryption** – encrypt with a public key, decrypt with a private key
- **Password manager** – check password strength, hash with bcrypt, and verify

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Choose an option from the menu. Files in `sample_files/` can be used to try out hashing and integrity checks.

## Project Structure

```
├── main.py            # Menu and entry point
├── modules/
│   ├── encryption.py  # AES and RSA
│   ├── hash.py        # File hashing and integrity checks
│   └── password.py    # Strength checking, hashing, verification
├── sample_files/      # Example files for testing
└── requirements.txt
```
