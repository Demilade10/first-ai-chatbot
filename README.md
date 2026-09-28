# First AI Chatbot

A simple command-line AI chatbot built with **Python**, the **OpenAI Python SDK**, and **OpenRouter**.

This project was created as my first hands-on AI Engineering project while learning the fundamentals of building applications powered by Large Language Models (LLMs).

## Project Goal

The goal was to understand the basic flow of an AI application:

```text
User Input
    ↓
Python Application
    ↓
LLM API
    ↓
AI Model
    ↓
Generated Response
```

Rather than starting with frameworks such as LangChain, RAG, agents, or a frontend, this project focuses on understanding the fundamentals first.

## How the Project Evolved

### 1. Basic User Input

The project started with:

```python
user_input = input("You: ")
print(user_input)
```

This introduced the basic idea of receiving input from a user and storing it inside a Python variable.

At this stage, there was no AI involved.

---

### 2. Connecting to an LLM

The chatbot was then connected to an LLM through an API.

OpenRouter is used as the API provider while the OpenAI Python SDK is used to communicate with it.

The application now follows this flow:

```text
User
  ↓
Python
  ↓
OpenRouter API
  ↓
LLM
  ↓
Python
  ↓
User
```

This introduced concepts such as:

* APIs
* API keys
* LLM requests
* Model responses
* Environment variables

The API key is stored outside the Python source code using an environment variable for security.

---

### 3. Continuous Conversation

Initially, the program could answer only one question.

The user had to run:

```bash
python main.py
```

again after every response.

A `while` loop was added so the chatbot could continue accepting questions until the user types:

```text
exit
```

This changed the chatbot from a one-request script into an interactive application.

---

### 4. Conversation Memory

Originally, every question was sent to the model independently.

For example:

```text
You: My favorite food is pizza.

You: What is my favorite food?
```

Without conversation history, the model would not necessarily know that the second message referred to information from the first.

To solve this, a `messages` list was introduced.

Example:

```python
messages = [
    {"role": "user", "content": "My favorite food is pizza"},
    {"role": "assistant", "content": "Nice!"},
]
```

Every new user message and AI response is added to this list.

The full conversation is then sent to the model with each request.

This gives the chatbot **short-term conversation memory**.

However, this memory originally existed only while the Python program was running.

---

### 5. System Prompt

A system prompt was added to control how the chatbot behaves.

Example:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI tutor. Explain answers simply and briefly."
    }
]
```

The system prompt provides instructions that guide the model's behavior throughout the conversation.

This introduced the idea that AI applications can control an LLM's behavior using instructions rather than changing the model itself.

---

### 6. Persistent Memory

The chatbot still had one major limitation.

When the terminal was closed or the Python program stopped, the `messages` list disappeared because it only existed in the computer's temporary memory.

That meant:

```text
Run chatbot
↓
Have conversation
↓
Close chatbot
↓
Conversation forgotten
```

To solve this, **persistent memory** was added using JSON.

The chatbot now saves the conversation to:

```text
memory.json
```

Using:

```python
json.dump(messages, file)
```

When the chatbot starts again, it checks whether `memory.json` exists.

If it does, the previous conversation is loaded using:

```python
json.load(file)
```

The flow becomes:

```text
Conversation
     ↓
messages list
     ↓
memory.json
     ↓
Program closes
     ↓
Program starts again
     ↓
memory.json loaded
     ↓
Conversation restored
```

This allows the chatbot to remember information even after the application has been restarted.

For example:

```text
You: My favorite food is pizza.
AI: Got it.

You: exit
```

After restarting the program:

```text
You: What is my favorite food?
AI: Your favorite food is pizza.
```

This demonstrated the difference between:

* **Temporary/in-session memory** — exists only while the application is running.
* **Persistent memory** — survives after the application closes.

---

## What is JSON?

JSON stands for **JavaScript Object Notation**.

Although it originated from JavaScript, JSON is now a language-independent format commonly used to store and exchange structured data.

Python dictionaries:

```python
{
    "role": "user",
    "content": "Hello"
}
```

can easily be stored as JSON.

This made JSON a simple choice for storing the chatbot's conversation history.

## Current Features

The chatbot currently supports:

* LLM-powered responses
* Command-line interaction
* Continuous conversations
* Exit command
* Conversation history
* System prompts
* Persistent memory
* Secure API key storage
* Free LLM access through OpenRouter

## Project Structure

```text
first-ai-app/
│
├── main.py
├── README.md
├── .gitignore
└── memory.json
```

`memory.json` is generated locally when conversations are saved.

It should **not be pushed to GitHub** because it can contain private conversation history.

The `.gitignore` file therefore contains:

```text
memory.json
.env
__pycache__/
```

## Technologies Used

* Python
* OpenAI Python SDK
* OpenRouter API
* JSON
* Git
* GitHub

## Concepts Learned

This project helped me understand:

* How Python applications receive user input
* How APIs connect applications to AI models
* How API keys work
* Environment variables
* Sending prompts to an LLM
* Reading model responses
* Python `while` loops
* Lists and dictionaries
* Conversation history
* System prompts
* Short-term memory
* Persistent memory
* Reading and writing JSON files
* Basic security practices for API keys

## Running the Project

Install the OpenAI Python SDK:

```bash
pip install openai
```

Create an OpenRouter API key and store it as an environment variable.

On Windows PowerShell:

```powershell
setx OPENROUTER_API_KEY "your_api_key_here"
```

Restart the terminal after setting the environment variable.

Then run:

```bash
python main.py
```

Start chatting:

```text
You: Explain machine learning simply.
AI: ...
```

To stop the chatbot:

```text
You: exit
```

## Current Limitations

This is intentionally a beginner-level AI Engineering project.

The chatbot currently does not include:

* A graphical user interface
* RAG
* Vector databases
* Tool use
* AI agents
* Web search
* User accounts
* Database-backed memory
* Memory summarization
* Production deployment

Conversation history is stored locally in a JSON file, which works well for learning but would not be ideal for a large production application.

## Key Takeaway

The biggest lesson from this project is that an AI application is more than just an LLM.

A basic AI application involves multiple components working together:

```text
User Interface
     ↓
Application Logic
     ↓
Prompt / Conversation History
     ↓
LLM API
     ↓
Model
     ↓
Response
```

Features such as memory, behavior control, security, and application logic are built **around the model**.

This project provided my first practical understanding of how those pieces fit together.
