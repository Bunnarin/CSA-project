# FileBatchTool

A powerful command-line utility for batch file management with customizable filters and operations. Built for efficiency, flexibility, and control over your file system tasks.

## ✨ Features

### 🔍 Selection Filters
Filter files based on:
- 📁 Path
- 📅 Date
- 🧩 Extensions
- 📦 File Size
- 📝 Name Pattern (Regex)

### 🛠️ Batch File Operations
Perform actions on multiple files at once:
- 🚚 Move
- 📄 Copy
- 🗑️ Delete
- 🔁 Find and Replace in file names

## 🧩 Modules

### `interface.py`
Handles terminal-based user interaction. It collects input parameters and delegates:
- Filter parameters to `filter.py`
- Operation parameters to `operation.py`

### `filter.py`
- Processes filters and returns a list of matching file paths.
- Builds a binary tree to visually represent the directory structure.

### `operation.py`
- Receives user-defined actions and performs them on the filtered file set.

### `main.py`
- Orchestrates all modules.
- Entry point of the program. Run this to start the application.