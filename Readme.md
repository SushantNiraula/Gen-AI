# Generative AI with LangChain — Learning Journey

A hands-on repository documenting my journey of learning **Generative AI, Large Language Models, LangChain, Retrieval-Augmented Generation (RAG), tool calling, and AI agents** by building small experiments and gradually combining them into larger AI systems.

The purpose of this repository is not to present a single finished application. Instead, it serves as my **Generative AI learning laboratory** where I practice concepts through code, understand how individual components work internally, and progressively build toward more capable AI applications.

---

# 🎯 Why I Built This Repository

When I started learning Generative AI, calling an LLM looked simple:

```text
Prompt → LLM → Response
```

But real AI applications require much more than sending text to a model.

A complete system may contain:

```text
User Input
     ↓
Prompt Template
     ↓
Language Model
     ↓
Structured Output
     ↓
Parser
     ↓
Chain / Workflow
     ↓
Retriever / Tools
     ↓
External Knowledge
     ↓
Agent
     ↓
Final Response
```

My goal with this repository has been to understand each of these pieces individually before combining them into larger applications.

---

# 🧠 What I Am Learning

This repository explores:

- Large Language Models
- Chat Models
- Embedding Models
- Prompt Engineering
- Prompt Templates
- Chat Messages and Conversation History
- Structured Outputs
- Pydantic and `TypedDict`
- Output Parsers
- LangChain Chains
- LCEL / Runnables
- Sequential Workflows
- Parallel Workflows
- Conditional Workflows
- Document Loaders
- Text Splitting
- Embeddings
- Vector Databases
- Semantic Search
- Retrieval-Augmented Generation
- Tool Calling
- Custom Tools
- AI Agents
- LangGraph basics
- RAG-powered applications

---

# 🗺️ My Learning Progression

The repository roughly follows this progression:

```text
Generative AI Fundamentals
          ↓
LLMs & Chat Models
          ↓
Embedding Models
          ↓
Prompt Engineering
          ↓
Structured Outputs
          ↓
Output Parsers
          ↓
Chains
          ↓
Runnables / LCEL
          ↓
Retrieval-Augmented Generation
          ↓
Document Loading & Chunking
          ↓
Embeddings + Vector Stores
          ↓
Semantic Retrieval
          ↓
Tool Calling
          ↓
Custom Tools
          ↓
AI Agents
          ↓
LangGraph
          ↓
Complete RAG Applications
```

Instead of jumping directly into agents, I wanted to understand the components from which agents are built.

---

# 📂 Repository Structure

```text
Gen-AI/
│
├── Models/
│   ├── Chat Models/
│   ├── LLms/
│   └── document_similarity.py
│
├── Prompts/
│
├── Structured_outputs/
│
├── Output_parsers/
│
├── Chains/
│
├── Runnables/
│
├── RAG/
│   ├── Documet_Loaders/
│   ├── Text_Splitters/
│   └── RAG.md
│
├── Agents/
│   ├── tool calling/
│   ├── Custom Tools/
│   └── Actual_Agent/
│
├── Langgraph/
│   └── Quickstart/
│
├── Youtube_Chat_Bot/
│
└── langchain_deeplearning_ai/
```

Each directory represents a stage in my learning.

---

# 1️⃣ Models

The `Models` directory contains my early experiments with different types of models used in Generative AI applications.

A useful mental model I learned is:

```text
                       Models
                         │
            ┌────────────┴────────────┐
            │                         │
     Language Models           Embedding Models
            │
       ┌────┴────┐
       │         │
      LLMs   Chat Models
```

---

## Language Models

Language models receive text and generate text.

Conceptually:

```text
Text Input
    ↓
Language Model
    ↓
Text Output
```

I experimented with different model interfaces and learned how LangChain provides a common abstraction around model providers.

---

## Chat Models

Chat models operate using messages rather than only plain strings.

Instead of:

```text
"Explain neural networks"
```

chat-based applications use structures resembling:

```text
System Message
Human Message
AI Message
```

This makes conversational applications easier to design.

I experimented with model providers including hosted and open-source models.

---

## Temperature

I also explored how **temperature** affects generation.

Lower temperature generally produces more deterministic responses:

```text
temperature → low
↓
more predictable output
```

Higher temperature allows more variation:

```text
temperature → high
↓
more creative / diverse output
```

This helped me understand that model behavior is influenced not only by prompts but also by generation parameters.

---

# 2️⃣ Embedding Models

One of the most important concepts I encountered was **embeddings**.

Unlike language models:

```text
Text → Text
```

embedding models perform:

```text
Text → Numerical Vector
```

For example:

```text
"I love robotics"

        ↓ embedding model

[0.23, -0.91, 0.41, ..., 0.72]
```

These vectors represent semantic meaning.

Texts with similar meanings tend to have nearby representations in embedding space.

---

## Document Similarity

I experimented with using embeddings to compare documents.

Conceptually:

```text
Document A → Embedding A ─┐
                          ├→ Similarity
Document B → Embedding B ─┘
```

This helped me understand the mathematical foundation behind:

- semantic search,
- vector databases,
- recommendation systems,
- RAG,
- information retrieval.

This was one of the important transitions from learning LLMs to understanding retrieval systems.

---

# 3️⃣ Prompts

The `Prompts` directory contains my experiments with how LangChain represents and manages prompts.

I explored:

- prompt templates,
- chat prompt templates,
- message objects,
- message placeholders,
- chat history,
- dynamic prompts,
- simple chatbot behavior.

---

## Prompt Templates

Instead of writing prompts manually every time:

```python
prompt = "Explain AI to a beginner"
```

templates allow prompts to contain variables:

```text
Explain {topic} to a {audience}
```

which can later become:

```text
Explain neural networks to a beginner
```

This makes prompts reusable and programmable.

---

## Chat Prompt Templates

For conversational applications, prompts can also contain multiple message roles.

Conceptually:

```text
System:
You are a helpful AI tutor.

Human:
Explain {topic}.
```

This helped me understand the distinction between simple text prompting and structured conversational prompting.

---

# 4️⃣ Conversation Messages & Chat History

I also experimented with different message types used by chat models.

Conceptually:

```text
SystemMessage
      ↓
HumanMessage
      ↓
AIMessage
      ↓
HumanMessage
      ↓
AIMessage
```

Keeping conversation history allows the model to understand previous turns rather than treating every request as an independent interaction.

This was my introduction to thinking about **state in conversational AI systems**.

---

# 5️⃣ Structured Outputs

LLMs normally generate free-form text.

For real applications, however, free-form text is often difficult for software to reliably process.

For example:

```text
"The movie was good. I would rate it around eight..."
```

is less useful programmatically than:

```json
{
  "sentiment": "positive",
  "rating": 8
}
```

The `Structured_outputs` section contains my experiments with converting LLM responses into predictable structures.

---

## TypedDict

I explored Python's `TypedDict` for defining expected dictionary structures.

Conceptually:

```python
class Review(TypedDict):
    sentiment: str
    rating: int
```

This makes expected data structures clearer.

---

## Pydantic

I also learned how Pydantic models provide stronger validation.

Conceptually:

```python
class Review(BaseModel):
    sentiment: str
    rating: int
```

Pydantic allows AI-generated outputs to behave much more like normal application data.

---

## `with_structured_output()`

I experimented with structured output capabilities where the expected schema is provided directly to the model interface.

This introduced an important idea:

> LLM output can become structured data that the rest of a software system can safely consume.

---

# 6️⃣ Output Parsers

The `Output_parsers` directory explores another major LangChain concept.

I experimented with:

- `StrOutputParser`
- JSON output parsing
- structured output parsing
- Pydantic output parsing

---

## Why Parsers Matter

An LLM often returns an object containing metadata around the actual generated text.

A parser can transform:

```text
Raw Model Response
       ↓
Output Parser
       ↓
Useful Application Data
```

Different applications need different formats.

For example:

```text
LLM
 ↓
String Parser
 ↓
Plain text
```

or:

```text
LLM
 ↓
JSON Parser
 ↓
Dictionary
```

or:

```text
LLM
 ↓
Pydantic Parser
 ↓
Validated Python Object
```

This helped me understand that **generation and parsing should often be treated as separate responsibilities**.

---

# 7️⃣ Chains

Once I understood prompts, models, and parsers individually, I started combining them.

A simple chain may look like:

```text
Prompt
  ↓
Model
  ↓
Parser
```

LangChain allows these components to form reusable processing pipelines.

---

## Simple Chains

I started with basic workflows:

```text
Input
  ↓
Prompt
  ↓
LLM
  ↓
Output
```

This helped establish how components communicate.

---

## Sequential Chains

Some AI tasks contain multiple dependent stages.

For example:

```text
Topic
  ↓
Generate Outline
  ↓
Generate Content
  ↓
Generate Summary
```

Each operation depends on the previous one.

This introduced me to **multi-step AI workflows**.

---

## Parallel Chains

Some tasks can be processed independently.

For example:

```text
                 ┌→ Generate Summary
Input ───────────┤
                 └→ Generate Questions
```

The outputs can later be merged.

Parallel execution is useful when different tasks do not depend on each other's intermediate results.

---

## Conditional Chains

Not every input should follow the same execution path.

For example:

```text
                   ┌→ Positive Response
Sentiment ─────────┤
                   └→ Negative Response
```

Conditional workflows introduced me to the idea of **dynamic AI pipelines** where execution depends on data produced during runtime.

That concept later becomes important when learning agents and LangGraph.

---

# 8️⃣ Runnables and LCEL

The `Runnables` section helped me understand one of LangChain's most important architectural ideas.

LangChain components can implement a common **Runnable interface**.

Conceptually:

```text
Runnable
   │
   ├── invoke()
   ├── batch()
   └── stream()
```

Because components share compatible interfaces, they can be composed together.

---

## LCEL

LangChain Expression Language allows pipelines to be expressed using the pipe operator:

```python
chain = prompt | model | parser
```

Conceptually:

```text
Input
 ↓
PromptTemplate
 ↓
ChatModel
 ↓
OutputParser
 ↓
Result
```

Rather than thinking only about individual functions, I started thinking in terms of **composable AI pipelines**.

---

## Runnable Primitives

I also explored runnable primitives and built simplified/dummy versions to understand what was happening behind LangChain abstractions.

This was especially useful because it helped answer:

> What is LangChain actually doing when components are connected using `|`?

Understanding the abstractions rather than only memorizing syntax was an important part of this learning process.

---

# 9️⃣ Retrieval-Augmented Generation — RAG

The `RAG` section marks a major step in the repository.

A normal LLM primarily relies on knowledge available from its model and the information present in the prompt.

RAG introduces external knowledge.

```text
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Question + Retrieved Context
      ↓
LLM
      ↓
Grounded Answer
```

---

# Why RAG?

RAG can help AI systems:

- access information outside model training data,
- work with private documents,
- use more recent information,
- answer questions from large document collections,
- reduce unsupported answers by providing context.

---

# 🔟 Document Loaders

Before information can be retrieved, it first needs to enter the application.

I learned about document loaders and loading strategies such as:

```text
load()
```

and:

```text
lazy_load()
```

---

## Eager Loading

```text
load()
```

loads the required content upfront.

### Benefits

- simple processing,
- everything becomes immediately available.

### Trade-off

- potentially higher memory use.

---

## Lazy Loading

```text
lazy_load()
```

loads data progressively.

### Benefits

- lower initial memory requirements,
- useful for larger datasets.

This helped me understand that even in AI applications, ordinary software-engineering concerns such as **memory usage and data processing strategy still matter**.

---

# 1️⃣1️⃣ Text Splitting

Large documents cannot always be directly passed into an embedding model or LLM.

They first need to be divided into manageable pieces.

```text
Large Document
      │
      ├── Chunk 1
      ├── Chunk 2
      ├── Chunk 3
      └── Chunk 4
```

I learned about different strategies for splitting documents, including:

- length-based splitting,
- text-structure-based splitting,
- document-structure-based splitting,
- semantic splitting.

---

## Why Chunking Matters

Poor chunking can result in:

```text
irrelevant retrieval
        ↓
poor context
        ↓
poor LLM answer
```

while better chunking helps produce:

```text
focused chunks
      ↓
better embeddings
      ↓
better retrieval
      ↓
better answers
```

This helped me realize that the quality of a RAG system depends on much more than the LLM itself.

---

# 1️⃣2️⃣ Embeddings + Vector Stores

After splitting documents:

```text
Documents
    ↓
Chunks
    ↓
Embedding Model
    ↓
Vectors
```

The resulting vectors can be stored inside a vector database or vector index.

A user query goes through the same embedding process:

```text
Question
   ↓
Embedding
   ↓
Query Vector
```

The system can then compare the query vector against stored document vectors.

---

# 1️⃣3️⃣ Semantic Search

Traditional keyword search looks for matching words.

Semantic search instead looks for matching **meaning**.

For example:

```text
Query:
"How can I reduce power consumption?"
```

could retrieve a document saying:

```text
"Methods for improving energy efficiency..."
```

even when the exact words are different.

That became one of the main reasons embeddings made sense to me.

---

# 1️⃣4️⃣ Retrievers

Vector stores can be exposed through a retriever interface.

Conceptually:

```text
Question
   ↓
Retriever
   ↓
Top-k Relevant Chunks
```

The retrieved chunks can then be inserted into a prompt before sending the request to the language model.

This forms the core RAG pipeline.

---

# 1️⃣5️⃣ YouTube RAG Chatbot

The `Youtube_Chat_Bot` project brings together several concepts learned earlier in the repository.

Instead of asking an LLM to answer from its existing knowledge, the chatbot retrieves information related to the video content first.

The architecture is approximately:

```text
YouTube Video / Transcript
          ↓
       Documents
          ↓
      Text Splitting
          ↓
        Chunks
          ↓
 Azure OpenAI Embeddings
          ↓
        FAISS
          ↓
      Retriever
          ↓
User Question
          ↓
Similarity Search
          ↓
Relevant Video Context
          ↓
         LLM
          ↓
       Response
```

For retrieval, I experimented with **FAISS** and similarity-based search.

The retriever returns relevant chunks that can be supplied to the language model as context.

---

## What This Project Helped Me Understand

This was important because the components I had previously studied independently finally started fitting together:

```text
Loader
   +
Splitter
   +
Embeddings
   +
Vector Store
   +
Retriever
   +
Prompt
   +
LLM
   =
RAG Application
```

Instead of treating RAG as a single feature, I began understanding it as a pipeline of several engineering components.

---

# 1️⃣6️⃣ Tools

Another important step was learning that LLMs do not need to rely only on generating text.

They can be provided with **tools**.

A tool is essentially a capability the model can request.

Examples could include:

```text
Calculator
Weather API
Currency Converter
Database Search
Web Search
Python Function
```

Conceptually:

```text
User
 ↓
LLM
 ↓
Need external capability?
 ↓
Tool
 ↓
Tool Result
 ↓
LLM
 ↓
Answer
```

This is an important difference between a chatbot and a more capable AI system.

---

# 1️⃣7️⃣ Tool Calling

The `Agents/tool calling` section contains experiments with connecting tools to models.

I also experimented with a currency-conversion tool.

Tool calling helped me understand the distinction between:

```text
LLM saying what should happen
```

and:

```text
software actually executing the action
```

The model determines which tool is appropriate and generates the required arguments, while application code performs the real execution.

---

# 1️⃣8️⃣ Custom Tools

I also explored building my own tools rather than relying only on prebuilt ones.

Conceptually:

```python
def my_tool(input):
    ...
```

can be described and exposed to the language model.

This means ordinary Python functions can become capabilities available to an AI application.

This is one of the major building blocks behind agents.

---

# 1️⃣9️⃣ AI Agents

After learning:

```text
Models
+
Prompts
+
Chains
+
Tools
```

I moved toward agents.

An ordinary chain usually follows a known path:

```text
A → B → C
```

An agent behaves differently.

```text
User Request
     ↓
    LLM
     ↓
Choose Action
     ↓
Use Tool
     ↓
Observe Result
     ↓
Reason Again
     ↓
Final Answer
```

The key idea is that the model participates in deciding **what should happen next**.

---

# Chain vs Agent

A useful distinction I learned is:

### Chain

```text
Developer determines workflow
```

### Agent

```text
Model dynamically chooses actions within
the capabilities provided by the developer
```

This transition was important for understanding modern Agentic AI systems.

---

# 2️⃣0️⃣ LangGraph Quickstart

I also started exploring **LangGraph**.

LangGraph takes workflow orchestration further by representing AI applications as graphs.

A simplified graph can look like:

```text
START
  ↓
Agent
  ↓
Decision
 /      \
Tool    Answer
 ↓
Agent
 ↓
END
```

The `Langgraph/Quickstart` section contains my early experimentation with:

- state graphs,
- graph execution,
- agent-style workflows.

I maintain more focused LangGraph experiments separately as I continue going deeper into graph-based Agentic AI.

---

# 🧩 What I Learned From This Repository

The biggest change in my understanding has been moving through several different mental models.

At first:

```text
AI App = LLM
```

Then:

```text
AI App = Prompt + LLM
```

Then:

```text
AI App = Prompt + Model + Parser
```

Then:

```text
AI App =
Prompt
+ Model
+ Parser
+ Chain
+ Retrieval
```

And finally:

```text
AI System =
Models
+ Prompts
+ Structured Data
+ Runnables
+ Retrieval
+ External Knowledge
+ Tools
+ State
+ Decision Making
```

That progression is the main purpose of this repository.

---

# 🧠 Important Engineering Lessons

While working through these examples, several ideas became especially important to me.

### LLMs are only one component

The quality of an AI application depends on:

```text
data
retrieval
prompt design
workflow design
tool quality
output validation
model selection
```

—not just the underlying language model.

### Structure matters

Applications need predictable data.

This is why concepts such as:

```text
TypedDict
Pydantic
JSON
Output Parsers
Structured Outputs
```

are important.

### Retrieval matters

When the correct information isn't present in model context, prompt engineering alone cannot solve the problem.

The system needs retrieval.

### Deterministic code still matters

An LLM should not replace ordinary programming when a deterministic solution is better.

For example:

```text
Arithmetic → Python
Knowledge Retrieval → Retriever
Natural Language Reasoning → LLM
```

Understanding where **not** to use an LLM is also part of learning AI engineering.

---

# 🛠️ Technologies Explored

The repository contains experiments involving technologies such as:

- Python
- LangChain
- LangGraph
- Azure OpenAI
- OpenAI-compatible chat models
- Hugging Face models
- Together AI
- Pydantic
- `TypedDict`
- FAISS
- Embedding models
- Vector search
- Jupyter Notebook
- RAG pipelines
- Tool calling
- AI agents

---

# ⚙️ Getting Started

Clone the repository:

```bash
git clone https://github.com/SushantNiraula/Gen-AI.git
cd Gen-AI
```

Create a virtual environment:

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

# Install Dependencies

Different experiments use different LangChain packages.

A typical environment may require packages such as:

```bash
pip install langchain
pip install langchain-core
pip install langchain-community
pip install langchain-openai
pip install langgraph
pip install faiss-cpu
pip install pydantic
pip install python-dotenv
pip install jupyter
```

Additional integrations may require their own packages.

---

# 🔐 Environment Variables

Some examples require API credentials.

I keep credentials outside Git and load them using environment variables.

A `.env` file may contain values such as:

```env
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment
AZURE_OPENAI_API_VERSION=your_api_version
```

Never commit real API credentials to a public repository.

---

# 📚 How I Recommend Exploring This Repository

If you are learning these concepts too, I would roughly explore them in this order:

```text
1. Models
      ↓
2. Prompts
      ↓
3. Structured Outputs
      ↓
4. Output Parsers
      ↓
5. Chains
      ↓
6. Runnables
      ↓
7. RAG
      ↓
8. Document Loaders
      ↓
9. Text Splitters
      ↓
10. Embeddings & Retrieval
      ↓
11. YouTube RAG Chatbot
      ↓
12. Tools
      ↓
13. Tool Calling
      ↓
14. Custom Tools
      ↓
15. Agents
      ↓
16. LangGraph
```

The later topics become much easier once the earlier abstractions make sense.

---

# 🚀 Where I Am Going Next

This repository is still part of an active learning journey.

Topics I want to keep developing include:

- [ ] Production-quality RAG pipelines
- [ ] Better chunking strategies
- [ ] Metadata filtering
- [ ] Hybrid retrieval
- [ ] Reranking
- [ ] Query rewriting
- [ ] Multi-query retrieval
- [ ] RAG evaluation
- [ ] LangSmith tracing
- [ ] Tool-using agents
- [ ] Agent memory
- [ ] LangGraph
- [ ] Human-in-the-loop systems
- [ ] Multi-agent architectures
- [ ] MCP
- [ ] AI application evaluation
- [ ] Guardrails
- [ ] Local/open-source LLMs
- [ ] Deployment
- [ ] Production monitoring

My goal is to gradually move from educational experiments toward **complete, reliable Generative AI and Agentic AI applications**.

---

# 📖 Learning Philosophy

I am using this repository to learn by **building rather than only watching tutorials or reading documentation**.

For every topic, I try to answer questions such as:

```text
What problem does this component solve?

Why does this abstraction exist?

What is happening internally?

When should I use it?

When should I NOT use it?

How does it connect to the other parts
of an AI system?
```

My objective is not simply to learn LangChain syntax.

The deeper goal is to understand the architecture behind modern Generative AI applications.

---

# 📌 Repository Status

> 🚧 **Active Learning Repository**

The code in this repository represents experiments created while learning.

Some examples are intentionally simple because their goal is to isolate and understand one concept at a time rather than provide production-ready implementations.

The repository will continue changing as my understanding improves.

---

# 👨‍💻 Author

**Sushant Niraula**

Electronics, Communication and Information Engineering

Interested in:

- Robotics
- Artificial Intelligence
- Generative AI
- Agentic AI
- Computer Vision
- Autonomous Systems

GitHub: [SushantNiraula](https://github.com/SushantNiraula)

---

## ⭐ Final Note

This repository documents my transition from simply using language models toward understanding how **complete AI systems are engineered**.

```text
Models
   ↓
Prompts
   ↓
Structured Outputs
   ↓
Chains
   ↓
Runnables
   ↓
Retrieval
   ↓
Tools
   ↓
Agents
```

Every folder represents another step in that journey.

If you are learning Generative AI as well, feel free to explore the code and follow along.
