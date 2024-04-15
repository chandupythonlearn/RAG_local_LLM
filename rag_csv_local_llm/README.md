# rag_csv_local_llm
This is to analyze your CSV data with RAG application using local LLM (Mixtral)

* First install the ollama in your local machine.
  * Ex: link to install ollama in local mac machine (https://ollama.com/download/mac)
* Start the ollama services using below command from your terminal window ...
    * ```ollama serve ```
      * If service already running then you will see below message
          * Error: listen tcp 127.0.0.1:11434: bind: address already in use
* Now Pull the required, open source LLM Model
    * EX: ```ollama run mixtral``` ( First time it will take some time to download the LLM package)

 ``` ruby
    git clone git@github.com:chandupythonlearn/RAG_local_LLM.git
    cd rag_csv_local_llm
    python3.10 -m venv env
    source ~/rag_csv_local_llm/env/bin/activate
    pip install -r requirements.txt
```
* Run below command to start the APP, which will open the app in your browser
    * ``` ruby
          streamlit run stremlite.py
      ```
 

Below is the output of my sample CSV analysis:
<img width="1136" alt="Screenshot 2024-04-14 at 10 48 27 PM" src="https://github.com/chandupythonlearn/RAG_local_LLM/assets/95510176/2c5b5916-b574-4b79-b9a6-e708aa956b3a">
