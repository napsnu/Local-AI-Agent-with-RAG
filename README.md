# Local-AI-Agent-with-RAG
# 🍕 Pizza Restaurant Q&A Agent

A Python-based AI agent that answers questions about a pizza restaurant using real customer reviews.  
It features a conversational interface powered by [LangChain](https://www.langchain.com/) and [Ollama](https://ollama.com/), with a user-friendly web UI built on [Streamlit](https://streamlit.io/).

---

## Features

- Retrieves relevant reviews using vector search
- Answers natural language questions about the restaurant
- Simple Streamlit web interface for interaction
- Easily extensible and ready for Docker deployment

---

## Project Structure

```
c:\Local AI Agent
│
├── main.py                # CLI interface for Q&A
├── ui.py                  # Streamlit web UI
├── vector.py              # Vector store setup and review ingestion
├── restaurant_reviews.csv # Sample review data
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore rules
```

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/pizza-restaurant-agent.git
cd pizza-restaurant-agent
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment:

```sh
python -m venv agent
# Activate the environment (Windows)
agent\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Prepare Data

Ensure `restaurant_reviews.csv` is present in the project root.  
You can add more reviews to this file as needed.

---

## Running the Application

### Command-Line Interface

```sh
python main.py
```
- Enter your question at the prompt.
- Type `q` to quit.

### Web UI (Recommended)

```sh
streamlit run ui.py
```
- Open the provided local URL in your browser.
- Enter your question and view the AI's answer.

---

## Development & Customization

- **Add reviews:** Edit `restaurant_reviews.csv` to include more data.
- **Change model:** Update the model name in `main.py` and `ui.py` as needed.
- **Tune retrieval:** Adjust `search_kwargs` in `vector.py` for more or fewer reviews.

---

## Dockerization (Optional)

To containerize the app, create a `Dockerfile` and build the image.  
Example steps:

```Dockerfile
# Dockerfile example
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "ui.py", "--server.port=8501"]
```

Build and run:

```sh
docker build -t pizza-agent .
docker run -p 8501:8501 pizza-agent
```

---

## Best Practices

- The `.gitignore` file excludes your virtual environment (`agent/`).
- Do **not** commit sensitive files or large data to the repository.
- For production, consider environment variables for model configuration.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or support, please open an issue or contact [your.email@example.com](mailto:your.email@example.com).
