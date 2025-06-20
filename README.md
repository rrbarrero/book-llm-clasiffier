# 📚 Book Classifier

This is a lightweight Python CLI tool that helps you **automatically classify your digital books** (PDF/EPUB) by analyzing their file names and inferring the main topic using a **Large Language Model (LLM)** via API.

It provides suggestions for organizing your library into thematic folders, making it easier to navigate and maintain.

---

## 🚀 Features

- Scans a directory for `.pdf` and `.epub` files.
- Uses a **Large Language Model (LLM)** API Gemini to infer the main topic from each book title.
- Outputs a clean classification table.
- Suggests an optimized folder structure based on consolidated topics.

---

## 🧪 Example Usage

```bash
uv run src/main.py ~/user/ebooks/folder
```

✅ Sample Output:

```
Okay, here is a classification of your books based on their titles, suggesting a main topic for each to help you organize them into folders.

| File Name                                                             | Main Topic / Suggested Folder Name         |
|----------------------------------------------------------------------|--------------------------------------------|
| The Road to Kubernetes by Justin Mitchell.pdf                        | Kubernetes                                 |
| Software Architecture: The Hard Parts.pdf                            | Software Architecture                      |
| Programming Rust (2nd Edition).pdf                                   | Rust Programming                           |
| Foundations of Scalable Systems by Ian Gorton.pdf                    | Distributed Systems & Scalability          |
| Designing Event-Driven Systems.pdf                                   | Event-Driven Architecture                  |
| Clean Architecture by Robert C. Martin.pdf                           | Software Architecture                      |
| Hands-On Machine Learning with Scikit-Learn and TensorFlow.pdf       | Machine Learning                           |

...

**Suggested Folder Structure (consolidated topics):**

You could create folders like:

*   API Design & Microservices
*   Cloud Computing
*   Cybersecurity
*   Data Engineering & Data Quality
*   Databases
*   DevOps & Continuous Delivery
*   Distributed Systems & Scalability
...
```

# 📦 Installation

This project uses uv for Python environment management. If you don’t have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then clone the repo, configure your API key and run the tool:

```bash
cp env-example .env

# Configure your API key inside .env

uv run src/main.py /path/to/your/books
```

🧠 Powered by LLMs
This project relies on a Large Language Model (LLM) API to semantically classify book titles.

You can plug in your own API provider (e.g. OpenAI, Google Gemini, Anthropic, etc.) by configuring the backend used in the code. The current version supports simple text classification via prompts.


🔮 Roadmap
Next version will include:
📂 Automatic folder creation and file moving
