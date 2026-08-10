# 🤖 AI Engineering — From Scratch to Production

> A practical, structured roadmap for learning **AI Engineering from the fundamentals to building production-ready AI systems**.

This repository is a continuously evolving collection of **notes, concepts, code, projects, resources, and practical implementations** covering the modern AI Engineering ecosystem.

The goal is simple:

**Learn the fundamentals → understand the technology → build it yourself → use frameworks → build production systems.**

---

## 🗺️ Roadmap

```text
Programming Fundamentals
        ↓
Python
        ↓
Data Structures & Algorithms
        ↓
Git + Linux + CLI
        ↓
SQL + Databases
        ↓
Computer Science Fundamentals
        ↓
Mathematics for AI
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
PyTorch
        ↓
NLP
        ↓
Transformers
        ↓
LLMs
        ↓
Embeddings
        ↓
Vector Databases
        ↓
RAG
        ↓
LLM Applications
        ↓
AI Agents
        ↓
LangChain
        ↓
LangGraph
        ↓
MCP
        ↓
AI Evaluation
        ↓
AI Security
        ↓
FastAPI
        ↓
Docker
        ↓
Cloud
        ↓
MLOps / LLMOps
        ↓
System Design
        ↓
Production AI Systems
```

---

# 📚 Table of Contents

* [1. Programming Fundamentals](#1-programming-fundamentals)
* [2. Python](#2-python)
* [3. Data Structures & Algorithms](#3-data-structures--algorithms)
* [4. Git & GitHub](#4-git--github)
* [5. Linux](#5-linux)
* [6. SQL & Databases](#6-sql--databases)
* [7. Computer Science Fundamentals](#7-computer-science-fundamentals)
* [8. Mathematics for AI](#8-mathematics-for-ai)
* [9. Machine Learning](#9-machine-learning)
* [10. Deep Learning](#10-deep-learning)
* [11. PyTorch](#11-pytorch)
* [12. NLP](#12-natural-language-processing)
* [13. Transformers](#13-transformers)
* [14. Large Language Models](#14-large-language-models)
* [15. Embeddings](#15-embeddings)
* [16. Vector Databases](#16-vector-databases)
* [17. RAG](#17-retrieval-augmented-generation)
* [18. LLM Applications](#18-llm-applications)
* [19. AI Agents](#19-ai-agents)
* [20. LangChain](#20-langchain)
* [21. LangGraph](#21-langgraph)
* [22. MCP](#22-model-context-protocol)
* [23. AI Evaluation](#23-ai-evaluation)
* [24. AI Security](#24-ai-security)
* [25. Backend Engineering](#25-backend-engineering)
* [26. Docker](#26-docker)
* [27. Cloud](#27-cloud)
* [28. MLOps & LLMOps](#28-mlops--llmops)
* [29. AI System Design](#29-ai-system-design)
* [30. Projects](#30-projects)
* [31. Production Checklist](#31-production-checklist)
* [32. How to Use This Repository](#32-how-to-use-this-repository)

---

# 1. Programming Fundamentals

Before working with AI systems, understand programming fundamentals.

### Topics

* Variables
* Data types
* Operators
* Conditional statements
* Loops
* Functions
* Recursion
* Error handling
* Input / Output
* Files
* Modules
* Packages
* Object-Oriented Programming
* Memory basics
* Debugging
* Testing
* Time & Space Complexity

### Goal

Be able to take a problem, break it into smaller pieces, design a solution, and implement it.

---

# 2. Python

Python is one of the primary languages used throughout modern AI/ML engineering.

### Fundamentals

* Variables
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* Loops
* Functions
* List comprehensions
* Lambda functions
* `*args` / `**kwargs`

### Intermediate

* OOP
* Decorators
* Iterators
* Generators
* Context managers
* Exception handling
* Type hints
* Dataclasses
* Modules and packages
* Virtual environments

### Advanced Python

* Async / Await
* Concurrency
* Multiprocessing
* Threading
* Logging
* Testing
* Dependency management
* Packaging

### Important Libraries

```text
NumPy
Pandas
Pydantic
Requests
HTTPX
Pytest
python-dotenv
```

---

# 3. Data Structures & Algorithms

DSA develops problem-solving ability and helps build strong programming fundamentals.

### Data Structures

* Arrays
* Strings
* Hashing
* Linked Lists
* Stack
* Queue
* Deque
* Trees
* Binary Search Trees
* Heaps
* Priority Queues
* Graphs
* Tries

### Algorithms

* Searching
* Sorting
* Binary Search
* Recursion
* Backtracking
* Greedy Algorithms
* Graph Algorithms
* Dynamic Programming

### Important Patterns

* Two Pointers
* Sliding Window
* Fast & Slow Pointers
* Prefix Sum
* Hash Map
* Binary Search on Answer
* Merge Intervals
* Monotonic Stack
* BFS
* DFS

### Recommended Practice

Solve problems by following:

```text
Understand
    ↓
Brute Force
    ↓
Analyze Complexity
    ↓
Optimize
    ↓
Implement
    ↓
Test
    ↓
Review
```

---

# 4. Git & GitHub

Learn how to manage and collaborate on software projects.

### Topics

* Git fundamentals
* Repository management
* Branches
* Commits
* Merge
* Rebase
* Pull Requests
* Merge conflicts
* `.gitignore`
* Tags
* Releases
* GitHub Actions
* CI/CD fundamentals

---

# 5. Linux

Production AI systems frequently run on Linux-based infrastructure.

### Learn

```text
Filesystem
Processes
Permissions
Environment variables
Networking
Ports
SSH
Services
Logs
Package management
Shell scripting
```

### Important Commands

```bash
pwd
ls
cd
mkdir
cp
mv
rm
cat
grep
find
chmod
ps
kill
curl
ssh
```

---

# 6. SQL & Databases

AI applications still rely heavily on traditional databases.

### SQL

* SELECT
* INSERT
* UPDATE
* DELETE
* JOIN
* GROUP BY
* ORDER BY
* Subqueries
* CTEs
* Window functions
* Indexes
* Transactions

### Databases

Start with:

```text
PostgreSQL
```

Then explore:

```text
MySQL
MongoDB
Redis
```

### Learn

* Database design
* Normalization
* Indexing
* Transactions
* Connection pooling
* Query optimization

---

# 7. Computer Science Fundamentals

Understand the foundations behind modern software systems.

### Topics

* Operating Systems
* Networking
* HTTP / HTTPS
* TCP/IP
* DNS
* Processes
* Threads
* Concurrency
* Memory
* Databases
* Distributed systems
* APIs
* Authentication
* Authorization

---

# 8. Mathematics for AI

You don't need advanced mathematics to start building AI applications, but understanding the fundamentals makes ML concepts much easier.

### Linear Algebra

* Scalars
* Vectors
* Matrices
* Matrix multiplication
* Dot product
* Norms
* Eigenvalues
* Eigenvectors

### Probability

* Probability
* Conditional probability
* Bayes theorem
* Random variables
* Probability distributions
* Expectation
* Variance

### Statistics

* Mean
* Median
* Variance
* Standard deviation
* Correlation
* Sampling
* Hypothesis testing

### Calculus

* Derivatives
* Partial derivatives
* Gradients
* Chain rule
* Gradient descent

---

# 9. Machine Learning

Understand traditional machine learning before going deep into modern AI systems.

### Fundamentals

* Supervised Learning
* Unsupervised Learning
* Semi-supervised Learning
* Reinforcement Learning

### Algorithms

* Linear Regression
* Logistic Regression
* Decision Trees
* Random Forest
* KNN
* SVM
* Naive Bayes
* K-Means
* PCA
* Gradient Boosting

### Core Concepts

* Features
* Labels
* Training
* Validation
* Testing
* Overfitting
* Underfitting
* Bias
* Variance
* Data leakage
* Feature engineering
* Hyperparameter tuning

### Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC
* MAE
* MSE
* RMSE
* R²

### Tools

```text
NumPy
Pandas
Matplotlib
Scikit-learn
```

---

# 10. Deep Learning

Understand how neural networks learn.

### Fundamentals

* Neurons
* Weights
* Bias
* Activation functions
* Forward propagation
* Loss functions
* Backpropagation
* Gradient descent
* Optimizers

### Architectures

* ANN
* CNN
* RNN
* LSTM
* GRU
* Autoencoders
* Transformers

---

# 11. PyTorch

Learn PyTorch for practical deep-learning development.

### Topics

* Tensors
* Datasets
* DataLoaders
* Models
* Training loops
* Loss functions
* Optimizers
* GPUs
* Checkpoints
* Model evaluation
* Saving/loading models

Build models from scratch instead of only using high-level abstractions.

---

# 12. Natural Language Processing

### Fundamentals

* Text preprocessing
* Tokenization
* Stemming
* Lemmatization
* Stop words
* N-grams
* TF-IDF
* Word embeddings
* Sentence embeddings
* Text classification
* Named Entity Recognition
* Sequence-to-sequence models

---

# 13. Transformers

Transformers are fundamental to modern LLM systems.

### Learn

* Tokenization
* Embeddings
* Positional encoding
* Self-attention
* Query
* Key
* Value
* Multi-head attention
* Feed-forward networks
* Residual connections
* Layer normalization
* Encoder
* Decoder

Understand the Transformer architecture rather than treating it as a black box.

---

# 14. Large Language Models

### Fundamentals

* Foundation models
* Pretraining
* Fine-tuning
* Instruction tuning
* RLHF
* Preference optimization
* Inference
* Sampling
* Temperature
* Top-p
* Context windows
* Tokens
* Tokenization

### LLM Concepts

```text
Prompt
    ↓
Tokenizer
    ↓
Model
    ↓
Logits
    ↓
Sampling
    ↓
Generated tokens
```

### Explore Model Ecosystems

* OpenAI
* Anthropic
* Google
* Meta
* Mistral
* Qwen
* Hugging Face

---

# 15. Embeddings

Embeddings convert information into numerical representations that capture semantic relationships.

```text
Text
  ↓
Embedding Model
  ↓
Vector
  ↓
Vector Database
```

### Learn

* Embedding models
* Vector dimensions
* Cosine similarity
* Dot product
* Euclidean distance
* Semantic similarity
* Dense representations

---

# 16. Vector Databases

Learn how vector search systems store and retrieve embeddings.

### Explore

* Qdrant
* Pinecone
* Weaviate
* Chroma
* Milvus
* FAISS

### Concepts

* Collections
* Vectors
* Metadata
* Payloads
* Indexes
* Similarity search
* Filtering
* Upsert
* Delete
* Retrieval

---

# 17. Retrieval-Augmented Generation

RAG connects external knowledge with LLM generation.

### Basic RAG

```text
Documents
    ↓
Load
    ↓
Clean
    ↓
Chunk
    ↓
Embed
    ↓
Vector Database
    ↓
Retrieve
    ↓
Context
    ↓
LLM
    ↓
Answer
```

### Learn

* Document loaders
* Chunking
* Embeddings
* Retrieval
* Metadata filtering
* Similarity search
* Reranking
* Hybrid search
* BM25
* Query rewriting
* Multi-query retrieval
* HyDE
* Context compression
* Parent-child retrieval
* Corrective RAG
* Agentic RAG
* Graph RAG

### RAG Evaluation

* Retrieval quality
* Context relevance
* Context recall
* Faithfulness
* Answer correctness
* Hallucination detection

---

# 18. LLM Applications

Learn how to build applications around language models.

### Concepts

* Prompt templates
* Structured outputs
* JSON outputs
* Function calling
* Tool calling
* Streaming
* Conversation history
* Context management
* Memory
* Model routing
* Fallback models
* Caching

---

# 19. AI Agents

An agent goes beyond simple prompt → response applications.

```text
User
 ↓
Agent
 ↓
Reason / Decide
 ↓
Select Tool
 ↓
Execute Tool
 ↓
Observe Result
 ↓
Continue / Finish
 ↓
Response
```

### Learn

* Tools
* Tool calling
* Agent loops
* State
* Planning
* Memory
* Human-in-the-loop
* Guardrails
* Tool permissions
* Error recovery
* Multi-agent systems

### Tools can include

```text
Web Search
Database
Calculator
APIs
File System
Code Execution
External Services
```

---

# 20. LangChain

Learn frameworks after understanding the underlying concepts.

### Topics

* Models
* Messages
* Prompts
* Structured output
* Tools
* Retrievers
* Document loaders
* Vector stores
* Agents
* Middleware
* Callbacks
* Context management

---

# 21. LangGraph

Learn graph-based agent workflows.

### Topics

* State
* Nodes
* Edges
* Conditional edges
* Loops
* Checkpoints
* Persistence
* Human-in-the-loop
* Agent workflows
* Error handling

Example:

```text
             START
               ↓
             Agent
            /     \
         Tool     Finish
           ↓
        Observe
           ↓
          Agent
```

---

# 22. Model Context Protocol

Learn how AI applications can interact with external tools and resources through standardized interfaces.

### Concepts

* MCP Client
* MCP Server
* Tools
* Resources
* Prompts
* Transport
* Permissions

Example:

```text
AI Application
      ↓
  MCP Client
      ↓
  MCP Server
   /   |    \
 DB   API   Files
```

---

# 23. AI Evaluation

A production AI system needs measurable quality.

Don't rely only on:

> "The answer looks good."

### Evaluate

```text
Accuracy
Relevance
Faithfulness
Hallucination
Retrieval quality
Latency
Token usage
Cost
Failure rate
```

### Explore

* Ragas
* DeepEval
* LangSmith
* Custom evaluation pipelines
* LLM-as-a-judge
* Human evaluation

---

# 24. AI Security

AI systems introduce a new security surface.

### Learn

* Prompt Injection
* Indirect Prompt Injection
* Jailbreaking
* Sensitive Information Disclosure
* System Prompt Leakage
* Insecure Tool Usage
* Excessive Agency
* Improper Output Handling
* RAG Poisoning
* Data Poisoning
* Model Extraction
* Model Inversion
* Adversarial Attacks
* Supply-chain risks

### Application Security

```text
Authentication
Authorization
RBAC
Rate Limiting
Input Validation
Output Validation
Secrets Management
Sandboxing
Audit Logging
Tool Permissions
```

---

# 25. Backend Engineering

AI systems need reliable backend infrastructure.

### Learn

```text
FastAPI
REST APIs
Async programming
Authentication
Authorization
JWT
OAuth
Streaming
WebSockets
Background jobs
Caching
Rate limiting
Logging
Error handling
```

### Typical Architecture

```text
Client
  ↓
API Gateway
  ↓
FastAPI
  ↓
Service Layer
  ↓
AI Agent
  ↓
LLM
  ↓
RAG / Tools
  ↓
Databases
```

---

# 26. Docker

Learn how to package AI applications for consistent deployment.

### Topics

* Images
* Containers
* Dockerfiles
* Volumes
* Networks
* Environment variables
* Docker Compose

Example:

```text
Docker
 ├── FastAPI
 ├── PostgreSQL
 ├── Redis
 └── Vector Database
```

---

# 27. Cloud

Learn one cloud platform deeply before exploring multiple platforms.

### AWS

Start with:

* EC2
* S3
* IAM
* VPC
* RDS
* ECR
* ECS
* Lambda
* CloudWatch
* Load Balancers
* Auto Scaling
* Secrets Manager

Later explore:

* Bedrock
* SageMaker

---

# 28. MLOps & LLMOps

Move AI systems from experiments into reliable production services.

### MLOps

* Data versioning
* Experiment tracking
* Model versioning
* Model registry
* Training pipelines
* Deployment
* Monitoring
* Model drift
* Retraining

### LLMOps

* Prompt versioning
* Model versioning
* Evaluation datasets
* Token monitoring
* Cost monitoring
* Latency monitoring
* Tracing
* Hallucination monitoring
* Production feedback
* Regression testing

---

# 29. AI System Design

Learn how to design AI systems that can handle real-world scale.

### Study

* Load balancing
* Caching
* Queues
* Workers
* Horizontal scaling
* Database scaling
* Connection pooling
* Rate limiting
* Circuit breakers
* Retries
* Timeouts
* Fault tolerance
* Observability

### AI-specific system design

* LLM gateways
* Model routing
* Model fallbacks
* Prompt caching
* Semantic caching
* Batch inference
* Streaming inference
* GPU utilization
* Inference optimization
* Cost optimization

---

# 30. Projects

Theory becomes valuable when it is turned into working systems.

## Beginner

### 01. LLM Chatbot

```text
Python
+
LLM API
+
FastAPI
+
Streaming
```

---

## 02. PDF Question Answering

```text
PDF
 ↓
Parser
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector DB
 ↓
Retriever
 ↓
LLM
```

---

## Intermediate

### 03. Research Agent

```text
User
 ↓
Agent
 ├── Search
 ├── Web Reader
 ├── Summarizer
 └── Source Evaluator
 ↓
Research Report
```

---

### 04. AI SQL Agent

```text
User
 ↓
Agent
 ↓
SQL Generation
 ↓
Validation
 ↓
Database
 ↓
Result
 ↓
Natural Language Response
```

Security and permission controls should be included.

---

## Advanced

### 05. Production RAG Platform

```text
FastAPI
+
PostgreSQL
+
Qdrant
+
LLM
+
Redis
+
Docker
+
LangGraph
+
Evaluation
+
Authentication
+
Logging
```

---

### 06. Multi-Agent Research Platform

```text
                 Supervisor
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    Research      Analyst       Reviewer
      Agent         Agent         Agent
        │            │            │
        └────────────┼────────────┘
                     ↓
                Final Output
```

---

# 31. Production Checklist

Before calling an AI application production-ready, consider:

### Reliability

* [ ] Error handling
* [ ] Retries
* [ ] Timeouts
* [ ] Fallbacks
* [ ] Circuit breakers

### Security

* [ ] Authentication
* [ ] Authorization
* [ ] Rate limiting
* [ ] Input validation
* [ ] Output validation
* [ ] Secrets management
* [ ] Tool permissions
* [ ] Audit logs

### AI Quality

* [ ] Evaluation dataset
* [ ] RAG evaluation
* [ ] Hallucination testing
* [ ] Prompt regression tests
* [ ] Model evaluation

### Performance

* [ ] Caching
* [ ] Streaming
* [ ] Async processing
* [ ] Database optimization
* [ ] Connection pooling

### Operations

* [ ] Logging
* [ ] Metrics
* [ ] Tracing
* [ ] Monitoring
* [ ] Alerts
* [ ] CI/CD
* [ ] Rollback strategy

### Cost

* [ ] Token monitoring
* [ ] Model selection
* [ ] Caching
* [ ] Batch processing
* [ ] Model routing

---

# 32. How to Use This Repository

This repository is designed to be followed progressively.

### Don't just read.

Use this learning cycle:

```text
Learn
  ↓
Understand
  ↓
Implement
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Build
  ↓
Deploy
  ↓
Evaluate
```

### Recommended approach

For every major topic:

```text
1. Learn the concept
2. Understand the architecture
3. Implement a small example
4. Build something practical
5. Study common failures
6. Learn the relevant framework
7. Build a production-oriented version
8. Document what you learned
```

---

# 🧱 Fundamental Principle

> **Don't learn frameworks before understanding the problem they solve.**

For example:

Don't start with:

```text
LangChain → RAG
```

Understand first:

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Search
 ↓
Retrieval
 ↓
Context
 ↓
LLM
```

Then learn how LangChain helps implement the system.

The same principle applies everywhere:

```text
Concept
  ↓
Manual Implementation
  ↓
Framework
  ↓
Production System
```

---

# 🛠️ Suggested Technology Stack

| Category        | Technologies                                     |
| --------------- | ------------------------------------------------ |
| Language        | Python                                           |
| DSA             | Python                                           |
| ML              | Scikit-learn                                     |
| Deep Learning   | PyTorch                                          |
| NLP             | Transformers                                     |
| LLMs            | OpenAI / Anthropic / Google / Open-source models |
| LLM Framework   | LangChain                                        |
| Agent Workflows | LangGraph                                        |
| Protocol        | MCP                                              |
| RAG             | LangChain / custom pipelines                     |
| Vector DB       | Qdrant / Pinecone / Weaviate / Chroma            |
| Database        | PostgreSQL                                       |
| Cache           | Redis                                            |
| API             | FastAPI                                          |
| Containers      | Docker                                           |
| Cloud           | AWS                                              |
| Evaluation      | Ragas / DeepEval / LangSmith                     |
| Version Control | Git / GitHub                                     |

---

# 📈 Learning Progress

Track your progress here:

### Programming

* [ ] Python
* [ ] Git
* [ ] Linux
* [ ] SQL
* [ ] Computer Science Fundamentals
* [ ] DSA

### AI / ML

* [ ] Mathematics
* [ ] Machine Learning
* [ ] Deep Learning
* [ ] PyTorch
* [ ] NLP
* [ ] Transformers
* [ ] LLMs

### Generative AI

* [ ] Prompt Engineering
* [ ] Embeddings
* [ ] Vector Databases
* [ ] RAG
* [ ] LLM Applications
* [ ] Agents
* [ ] LangChain
* [ ] LangGraph
* [ ] MCP

### Production

* [ ] FastAPI
* [ ] Docker
* [ ] Redis
* [ ] Cloud
* [ ] MLOps
* [ ] LLMOps
* [ ] Evaluation
* [ ] Monitoring
* [ ] AI Security
* [ ] System Design

### Projects

* [ ] LLM Chatbot
* [ ] PDF RAG
* [ ] Research Agent
* [ ] SQL Agent
* [ ] Production RAG
* [ ] Multi-Agent System

---

# 🌱 From Scratch → Production

The purpose of this repository is not to collect technologies.

It is to understand **how modern AI systems are actually built**.

```text
Programming
     ↓
Computer Science
     ↓
Machine Learning
     ↓
Deep Learning
     ↓
Transformers
     ↓
LLMs
     ↓
RAG
     ↓
Agents
     ↓
Backend
     ↓
Cloud
     ↓
MLOps / LLMOps
     ↓
Security
     ↓
Evaluation
     ↓
System Design
     ↓
Production AI
```

> **Learn the fundamentals. Build the systems. Break the systems. Fix them. Deploy them. Measure them. Improve them.**

---

## ⭐ Contributing

Contributions, corrections, resources, examples, and improvements are welcome.

If you find an error or have a useful resource:

1. Open an issue.
2. Suggest an improvement.
3. Submit a pull request.

Let's build a practical and continuously evolving **AI Engineering knowledge base** together.

---

## 📌 Disclaimer

This roadmap is continuously evolving. AI Engineering changes rapidly, so technologies, tools, models, and best practices will be updated as the ecosystem evolves.

**Learn concepts first. Tools change. Fundamentals remain.**

