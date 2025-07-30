# RAG Evaluation with Ragas

This project provides a framework for evaluating Retrieval-Augmented Generation (RAG) pipelines using the [`ragas`](https://github.com/explodinggradients/ragas) library. It includes two notebooks to demonstrate evaluation with LLMs from AWS Bedrock and Google AI Platform.


## Data Preparation

The evaluation data is read from `questions_file.csv`. The `dataset.py` script contains the logic to parse this file and transform it into the format required by the `ragas` evaluation framework.

The notebooks import the `extract_rag_data` function from this script to load the data.

## How to Use

You can choose to evaluate your RAG implementation using either AWS or Google models by following the instructions below.

### Evaluating with AWS Bedrock (`eval_aws.ipynb`)

This notebook uses AWS Bedrock to provide the LLM for evaluation.

1.  **Configure AWS Credentials**:
    Ensure your AWS credentials are set up correctly. The notebook uses the `default` profile by default. If you haven't configured the AWS CLI, you can do so by running:
    ```bash
    aws configure
    ```

2.  **Run the Notebook**:
    Open and run the cells in `eval_aws.ipynb`. You can modify the configuration in the first cell to change the AWS region, profile name, or the models used for generation and embeddings.

### Evaluating with Google AI (`eval_google.ipynb`)

This notebook uses the Google Generative AI API for evaluation.

1.  **Set up API Key**:
    - Create a `.env` file by copying the example:
      ```bash
      cp env.example .env
      ```
    - Edit the `.env` file and add your Google AI API key:
      ```
      GOOGLE_API_KEY="your-secret-api-key"
      ```

2.  **Run the Notebook**:
    Open and run the cells in `eval_google.ipynb`. You can change the model and other parameters in the configuration cell at the top of the notebook.
