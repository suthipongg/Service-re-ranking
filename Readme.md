<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Hey_Machine_Learning_Logo.png" alt="ml logo"></a>
</p>

<h3 align="center">Service Re-Ranking</h3>

---

<p align="center"> Improve Retrieval Augmented Generation (RAG) with Re-ranking Service
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting_started)
- [Running the tests](#tests)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [VERSION](#version)

## 🧐 About <a name = "about"></a>

**Improve Retrieval Augmented Generation (RAG) with Re-ranking Model** aims to enhance the relevance and quality of outputs in RAG systems. By integrating a re-ranking model, we refine the initial retrieval results, ensuring the most relevant information is used for generation.

### Key Objectives
- **Enhanced Retrieval Accuracy:** Select the most contextually appropriate documents.
- **Optimized Generation Quality:** Produce coherent and relevant responses.
- **Efficiency and Scalability:** Ensure the model is efficient for large-scale use.

### Approach
Our method involves:
1. **Document Retrieval:** Initial retrieval of relevant documents.
2. **Re-ranking:** Scoring and ranking these documents for relevance.
3. **Augmented Generation:** Using top-ranked documents for final response generation.

### Benefits
- **Improved Response Relevance**
- **Reduction in Noise**
- **Enhanced User Satisfaction**

This project is ideal for those in NLP looking to improve RAG systems.

## 🌟 Features

- **Re-rank Sentences:** Prioritizes the most contextually relevant sentences for improved accuracy.
- **Model Warm-up:** Enhances performance through an initial warm-up phase.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have the following software installed:

- [GitHub Project](https://github.com/suthipongg/Service-re-ranking.git)
- [Re-Ranking Model](https://huggingface.co/Pongsasit/mod-th-cross-encoder) (Pongsasit/mod-th-cross-encoder)
- [pm2](https://pm2.keymetrics.io/docs/usage/quick-start/)

### Installing

1. Clone this GitHub repository:
  ```bash
  git clone https://github.com/suthipongg/Service-re-ranking.git
  ```

2. Create a virtual environment:
  ```bash
  python3 -m venv venv
  ```

3. Activate the virtual environment:
  ```bash
  # For Linux
  source venv/bin/activate
  ```

4. Install the required packages from the requirements file:
  ```bash
  pip install -r requirements.txt
  ```

5. Download the re-ranking model:

Model Name | Type
---|---
[Pongsasit/mod-th-cross-encoder](https://huggingface.co/Pongsasit/mod-th-cross-encoder)| cross-encoder

## 🔧 Running the tests <a name = "tests"></a>

To run the automated tests for this system, follow these steps:

1. Navigate to the GitHub project directory:
  ```bash
  cd test_api
  ```

2. Run test for the GitHub project:
  ```bash
  bash test_api.bash 
  ```

## 🎈 Usage <a name="usage"></a>

To use the system, follow these steps:

1. **Run the application:**
  ```bash
  bash start_pm2.sh
  ```

2. **Access the application:**
    Open your browser and navigate to `http://localhost:8091`

This section provides clear instructions for running the UVicorn servers for this project. Adjust it as needed based on your project's specifics.

## 🚀 Deployment <a name = "deployment"></a>

1. **Server Setup**: Set up a server environment suitable for hosting your project. This typically involves choosing a cloud provider and provisioning a virtual machine instance.

2. **Software Installation**: Install the necessary software dependencies on your server, including Python. Follow the installation instructions provided by the respective software vendors.

3. **Clone Repository**: Clone the GitHub repository containing your project onto your server using the `git clone` command.

4. **Download Model**: Download the Re-Ranking Model from Hugging Face or self traning model.

5. **Environment Configuration**: Set up environment variables and configuration files as needed for your project. Ensure that sensitive information such as API keys and database credentials are securely stored.

6. **Build and Install**: Build your project and install any required dependencies using the appropriate package manager (e.g., pip for Python projects). You may also need to compile any frontend assets if applicable.

7. **Run Servers**: Start the necessary servers for your project, such as UVicorn for running your web application and any other backend services (e.g., Elasticsearch, MongoDB, Redis).

## ⛏️ Built Using <a name = "built_using"></a>

This project is built using the following technologies:

- [Python](https://www.python.org/) - Programming language
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building APIs with Python
- [Hugging Face](https://huggingface.co/) - Open Source libraries for Machine Learning

These technologies were chosen for their performance, scalability, and ease of use, enabling us to build a robust and efficient system for our project.

<details>
<summary>Version</summary>

# Version History

## [0.0.0] (2024-06-07)

- Release date: June 7, 2024

### Added
- Initial release of the project.

</details>