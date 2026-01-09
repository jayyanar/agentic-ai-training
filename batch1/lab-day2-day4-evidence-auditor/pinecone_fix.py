# Fixed Pinecone initialization code
# Replace the problematic cell with this code:

# Initialize components with proper vector setup
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create or connect to index
existing_indexes = [idx.name for idx in pc.list_indexes()]
if PINECONE_INDEX_NAME not in existing_indexes:
    print(f"Creating new vector index: {PINECONE_INDEX_NAME}")
    from pinecone import ServerlessSpec
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print("⏳ Waiting for index to be ready...")
    import time
    time.sleep(10)  # Wait for index to initialize
else:
    print(f"Using existing vector index: {PINECONE_INDEX_NAME}")

index = pc.Index(PINECONE_INDEX_NAME)
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY, model="text-embedding-3-small")
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini", temperature=0)

print(f"✅ Vector database ready: {index.describe_index_stats()}")
