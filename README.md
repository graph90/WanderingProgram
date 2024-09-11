# WanderingProgram

## Overview

**WanderingProgram** is an experimental Python script (`wander.py`) designed to explore the concept of a self replicating and self muting program. This script continuously moves around different directories in Linux, replicates itself, and mutates its own code. It demonstrates a persistent process that evolves and propagates within a file system.

## Features

- **Encryption/Decryption:** Uses XOR encryption to secure its files.
- **File Replication:** Copies itself to various directories.
- **Code Mutation:** Randomly alters its own code to introduce variations.
- **Directory Selection:** Dynamically chooses directories based on current context.
- **Self Appending:** Appends content to `.txt` files in the target directory.

## How It Works

1. **Encryption/Decryption:** Reads the file, encrypts or decrypts it using XOR with a generated key.
2. **File Replication:** After copying itself to a new location, it encrypts the copy and appends content to `.txt` files in the target directory.
3. **Code Mutation:** Applies random mutations to its code to alter its behavior.
4. **Directory Selection:** Chooses directories to move to based on the current directory context and avoids directories where a similar program is already present.

## Running the Program

### Prerequisites

- Python 3.x
- A virtual machine (VM) environment for testing

### Setup

1. **Create a VM:**
   - Use VirtualBox or VMware.
   - Install a Linux based OS (Ubuntu) for easier directory management.

Testing Environment: It’s highly recommended to run the program in a VM or isolated environment to prevent unintended effects on your main system.

Safety: This program is for experimental purposes only. It performs actions like file encryption and deletion, which can be disruptive. Use with caution and ensure you have backups of important files.
