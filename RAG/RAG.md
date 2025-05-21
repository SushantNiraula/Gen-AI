RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.
Benefits of using RAG
1. Use of up-to-date information
2. Better privacy
3. No limit of document size


## Document Loader

1. load()
    -> Also known as eager loading.
    Definition: Loads all necessary data upfront when the application starts or when a request is made.
    **Advantages:**
1. Ensures fast access to all required data.
2. Reduces the number of database queries, improving efficiency.
3. Simplifies logic since all data is available immediately.
**Disadvantages:**
1. Can lead to higher memory usage if unnecessary data is loaded.
2. Slower initial load time due to fetching everything at once.


2. lazy_load()
    ->
    Definition: Loads data only when needed, delaying initialization until the resource is accessed.
**Advantages:**
1. Improves startup performance by loading only essential data.
2. Saves memory and bandwidth by fetching data on demand.
**Disadvantages:**
1. Can introduce delays when accessing data for the first time.
2. May result in multiple database queries, increasing overhead.


## Text-Splitters
Text splitting is the process of breaking large chunks of text (like articles, PDF's , HTML pages, or books) into smaller, manageble pieces(chunks) that an LLM can handle effectively. 


            ---------> Chunk 1

|Large Text|  -------> Chunk 2

            ---------> Chunk 3


* Overcoming model Limitations: Many embedding models and language models have maximum input size constraints.
* Splitting allows us to process documents that would otherwise exceed these limits.

* Downstream tasks: Text splitting improves nearly every LLM Powered task.

| Task | Why Splitting Helps |
|-----|----------|
|Embedding | Short chunks year more accurate vectors |
| Semantic Search | Search results point to focused info, not noise|
| Summerization | Prevents hallucination and topic drift |

* Optimizing computational resources : Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.

## Types of Text Splitters
1. Length Based
2. Text Structure Based
3. Document Structure Based
4. Semantic Meaning Based
