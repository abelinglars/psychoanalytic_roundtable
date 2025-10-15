# Psychoanalytic Roundtable

Simulate discussions between Sigmund Freud and Carl Gustav Jung, each equipped
with the indexed version of their work ready at hand. Share a thought or ask a
question and see these two hash it out in conversation.

## Implementation
The project uses **langchain** to create the LLM clients, **ollama** as a model
provider and **chroma** as vector datastore. During each conversational turn, the
analyst has access to the last rebuttal of the other as well as his own last
response to go into the RAG pipeline. From there on he is encouraged to argue
his case with reference to the retrieved material. After three turns each a
moderator steps in to conclude and summarize the discussion, whether or not an
agreement could be reached.

## Improvements
- Pick a topic that is not readily available in the training data of foundation
models (eg news), to ensure data from the retrieval step is used
- Play around with different models and chunking strategies
- use a hosted model instead of a local one
- 
