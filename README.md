# Personal virtual assistant

🚧 This project is under construction.

## Introduction

This project aims to create an open-source personal AI assistant based on ChatGPT and other large language models (LLMs). The goal is to develop a complete workflow and toolchain that allows AI to assist humans in various tasks. The project is currently under active development, and we welcome contributors and feedback from the community.

## Getting Started

### Prerequisites

Make sure you have `python`, `poetry`, and `git` installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/al002/virtual-assistantt-backend.git
cd virtual-assistant-backend
```

2. Set up a virtual environment using poetry:
```bash
poetry install
poetry shell
```

3. Run the development server:
```bash
python web/manage.py migrate

// create super user first
python manage.py createsuperuser

python web/manage.py runserver
```

Now, the Django development server should be running at http://127.0.0.1:8000/. 

## Vision
Our vision is to build an open-source personal AI assistant that utilizes the power of ChatGPT and other LLMs to improve the way people work, communicate, and interact with technology. Our main goals are:

1. Develop a comprehensive workflow and toolchain to assist users in various tasks, such as programming, change the way to interact with internet, and personal stuff like writing emails etc.
2. Ensure privacy and security by implementing best practices and allowing users to host their instances.

## Acknowledgments

We would like to express our gratitude to the researchers and developers at OpenAI for creating ChatGPT and other large language models that inspire this project.