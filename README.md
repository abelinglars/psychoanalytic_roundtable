# Psychoanalytic Roundtable

Simulate discussions between Sigmund Freud and Carl Gustav Jung, each equipped
with the indexed version of their work ready at hand. Share a thought or ask a
question and see these two hash it out in conversation.

## Overview

The project uses **[langchain](https://www.langchain.com/)** to create the LLM
clients, **[ollama](https://ollama.com/)** as a model provider and
**[chroma](https://www.trychroma.com/)** as vector datastore. During each
conversational turn, the analyst has access to the last rebuttal of the other
as well as his own last response to go into the RAG pipeline. From there on he
is encouraged to argue his case with reference to the retrieved material. After
three turns each a moderator steps in to conclude and summarize the discussion,
whether or not an agreement could be reached.

## Implementation

### Embedding
The textbooks are chunked with the recursive-character chunking strategy,
aiming to preserve context and meaning within chunks. In order to avoid cuttoff
knowledge, the chunks overlap by 10% of the chunk length. Average sentence length is
, so our chunking strategy should be able to conserve sentences nicely.
The embedding was computed using the 'mxbai-embed-large' model provided by ollama using

## Run Instructions

Install [Ollama](https://ollama.com/download) according to the instructions for
your operating system.

Pull the required ollama models:
```bash
ollama pull llama.3.2
ollama pull mxbai-embed-large
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) as to the
instructions for your operating system

Install python dependencies
```bash
uv pip install -r pyproject.toml
```

Run the main.py file to start the LLMs and ask questions at the command line
```bash
python3 main.py
```

## Improvements
- Pick a topic that is not readily available in the training data of foundation
models (eg news), to ensure data from the retrieval step is used
- Play around with different models and chunking strategies
- use a hosted model instead of a local one
- 
