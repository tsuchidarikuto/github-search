# GitHub User Search Application

A Python application to search GitHub users and save the results as a CSV file.

## Features

- Search GitHub users using the GraphQL API
- Support for advanced query syntax (AND, OR, NOT, exact match, etc.)
- Save search results as CSV
- Docker support for easy containerized execution

## Requirements

- Python 3.8 or later
- Docker (optional)
- GitHub Personal Access Token

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/tsuchidarikuto/github-search.git
    cd github-search
    ```

2. **Get a GitHub Personal Access Token**:
    - Go to GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
    - Click **"Generate new token"**
    - Grant the necessary scope (e.g., `read:user`)
    - Copy and store the token securely

3. **Set environment variables**:
    - Create a `.env` file and add:
    ```env
    GITHUB_TOKEN=your_github_token_here
    ```

## Usage

### Run with Python

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the application**:
    ```bash
    python src/simple_github_search.py
    ```

### Run with Docker

1. **Build the Docker image**:
    ```bash
    docker compose build
    ```

2. **Run the application**:
    ```bash
    docker compose up
    ```

## Query Syntax Guide

- **Logical Operators**:
  - `OR`: Match either condition (e.g., `"python OR javascript"`)
  - `AND`: Match both conditions (e.g., `"python AND developer"`)
  - `NOT`: Exclude matches (e.g., `"python NOT java"`)

- **Exact vs. Partial Match**:
  - `"python developer"`: Exact phrase match
  - `python developer`: Partial match (contains both words)

- **Qualifiers**:
  - `in:bio`: Search in user's bio
  - `in:name`: Search in username
  - `followers:>1000`: Users with more than 1000 followers
  - `location:japan`: Users located in Japan

## Output

The results are saved as a CSV file in the `output` directory.  
Each file is timestamped to ensure uniqueness.