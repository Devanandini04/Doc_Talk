## DOC-TALK
## RAG-Based Document Assistant

**DOC-TALK** is a Streamlit-based application that enables users to chat with a conversational AI over the content of multiple PDF documents.
It follows a **Retrieval-Augmented Generation (RAG)** approach, where relevant document context is retrieved and supplied to a large language model for grounded, context-aware responses.

🔗 Live Demo: 
<https://gmultichat.streamlit.app/>

<https://github.com/kaifcoder/gemini_multipdf_chat/assets/57701861/f6a841af-a92d-4e54-a4fd-4a52117e17f6>

## Features

- **Multi-PDF Upload** – Upload and process multiple PDF documents at once  
- **Text Extraction & Chunking** – Extracts and segments document text for efficient retrieval  
- **Vector-Based Retrieval** – Uses embeddings and similarity search to fetch relevant context  
- **Conversational AI** – Powered by Google Gemini for natural language interaction  
- **Interactive Chat Interface** – Simple and intuitive Streamlit-based UI  

## Getting Started

If you have docker installed, you can run the application using the following command:

- Obtain a Google API key and set it in the `.env` file.

   ```.env
   GOOGLE_API_KEY=your_api_key_here
   ```

```bash
docker compose up --build
```

Your application will be available at <http://localhost:8501>.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References

- [Docker's Python guide](https://docs.docker.com/language/python/)

## Project Structure

Docs_Talk/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── README.md              # Project documentation
├── Dockerfile             # Docker configuration
├── compose.yaml           # Docker Compose setup


## Local Development

Follow these instructions to set up and run this project on your local machine.

   **Note:** This project requires Python 3.10 or higher.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Docs_Talk.git
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google API Key:**
   - Obtain a Google API key and set it in the `.env` file.

   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Run the Application:**

   ```bash
   streamlit run main.py
   ```

5. **Upload PDFs:**
   - Use the sidebar to upload PDF files.
   - Click on "Submit & Process" to extract text and generate embeddings.

6. **Chat Interface:**
   - Chat with the AI in the main interface.

## Project Structure

- `app.py`: Main application script.
- `.env`: file which will contain your environment variable.
- `requirements.txt`: Python packages required for working of the app.
- `README.md`: Project documentation.

## Dependencies

- PyPDF2
- langchain
- Streamlit
- google.generativeai
- dotenv

## Planned Improvements

- [ ] Retrieval latency benchmarking
- [ ] Chunking strategy optimization
- [ ] Source-grounded answer enforcement
- [ ] Evaluation metrics for response relevance


## Acknowledgments

- [Google Gemini](https://ai.google.com/): For providing the underlying language model.
- [Streamlit](https://streamlit.io/): For the user interface framework.
