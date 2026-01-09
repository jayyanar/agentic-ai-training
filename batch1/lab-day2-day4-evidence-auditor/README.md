# 🧪 Invoice Processing Lab Exercise
## Technology Stack Demonstration: LangGraph + LangChain + OpenAI + Pinecone

An end-to-end AI system demonstrating modern document processing technologies for automated invoice classification and validation.

## 🎯 Lab Objectives

This lab demonstrates the integration of cutting-edge AI technologies:
- **LangGraph**: Workflow orchestration and state management
- **LangChain**: Document parsing and text processing
- **OpenAI**: Vision-based extraction and embeddings
- **Pinecone**: Vector storage and retrieval

## 📋 Business Rules & Validation

**Invoice Validation Logic:**
- ✅ **Valid**: All required fields present (vendor name, invoice number, date, amount)
- ❌ **Invalid**: Missing any required field

**Validation Process:**
1. Extract structured data from PDF using GPT-4 Vision
2. Validate against business rules
3. Classify as Valid/Invalid with detailed rationale
4. Store results with validation metadata

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install langgraph langchain langchain-openai langchain-pinecone pinecone PyMuPDF pandas
```

### 2. Setup Environment
```bash
cp .env.example .env
# Add your API keys:
# OPENAI_API_KEY=your_openai_key
# PINECONE_API_KEY=your_pinecone_key
```

### 3. Run the Lab Exercise

**Jupyter Notebook (Recommended)**:
```bash
jupyter notebook invoice_processing_lab.ipynb
```

The notebook will:
1. Convert PDFs to markdown and display content
2. Validate invoices based on business rules
3. Store markdown content in Pinecone vector database
4. Execute test queries with validation context

## 📊 Workflow Pipeline

```
PDF Files → LLM Vision → Markdown Display → Invoice Validation → Vector Storage → RAG Queries
```

### Step-by-Step Process:
1. **Load PDFs**: Discover invoice files in data directory
2. **Convert to Markdown**: Use GPT-4 Vision to extract and format content
3. **Display Content**: Show all markdown content on screen for review
4. **Validate Invoices**: Apply business rules and classify as Valid/Invalid
5. **Store in Vector DB**: Save markdown content with validation metadata
6. **Test Queries**: Execute RAG queries with validation context

## 🔧 Technology Integration

### LangGraph Orchestration
- **State Management**: TypedDict for workflow state
- **Node-based Processing**: Modular workflow components
- **Error Handling**: Comprehensive error tracking and reporting

### LangChain Document Processing
- **PDF Processing**: PyMuPDF for high-quality image conversion
- **Text Splitting**: Intelligent document chunking
- **Vector Operations**: Seamless Pinecone integration

### OpenAI Integration
- **Vision Processing**: GPT-4 Vision for image-based PDF reading
- **Structured Extraction**: JSON-formatted data extraction
- **Embeddings**: text-embedding-3-small for vector storage

### Pinecone Vector Database
- **Serverless Architecture**: AWS-based vector storage
- **Metadata Filtering**: Rich metadata for contextual search
- **Similarity Search**: Semantic document retrieval

## 📁 Project Structure

```
├── invoice_processing_lab.ipynb    # Main lab exercise notebook
├── data/                          # Sample invoice PDFs
│   ├── invoice_1.pdf
│   ├── invoice_2.pdf
│   └── ...
├── markdown_output/               # Generated markdown files
├── requirements.txt              # Python dependencies
├── .env.example                 # Environment template
└── README.md                   # This file
```

## 📊 Expected Outcomes

### 1. PDF to Markdown Conversion
- Clean, structured markdown from image-based PDFs
- Preserved formatting and important details
- Visual display of all processed content

### 2. Invoice Validation Results
```
📊 INVOICE VALIDATION RESULTS
Filename        Status    Vendor Name    Invoice Number    Date        Amount
invoice_1.pdf   Valid     Acme Corp      INV-001          2024-01-15  $1,250.00
invoice_2.pdf   Invalid   Missing        INV-002          2024-01-16  Missing
```

### 3. Vector Search with Validation Context
- Semantic search across all invoice content
- Results include validation status and extracted fields
- Contextual retrieval based on business rules

## 🔍 Test Queries

The lab includes comprehensive test queries:
- "Show me valid invoices with vendor information"
- "Find invoices with missing required fields"
- "What are the invoice amounts and dates?"
- "Which invoices have complete vendor details?"
- "Show me invalid invoices and reasons"

## 📈 Performance Metrics

- **Processing Speed**: Instant PDF to markdown conversion
- **Validation Accuracy**: Rule-based classification with detailed rationale
- **Search Relevance**: Semantic similarity with validation context
- **Scalability**: Vector database handles large document collections

## 🛠️ Customization

### Modify Business Rules
Edit the `validate_invoice()` function in the notebook to change validation criteria.

### Add New Query Types
Extend the `test_queries` list to include domain-specific searches.

### Adjust Vector Storage
Modify metadata fields in `store_in_vector_db()` for custom document attributes.

## 🔒 Environment Variables

```bash
OPENAI_API_KEY=your_openai_key      # Required for GPT-4 Vision and embeddings
PINECONE_API_KEY=your_pinecone_key  # Required for vector storage
```

## 📚 Learning Outcomes

After completing this lab, you will understand:
- **LangGraph workflow orchestration** for complex AI pipelines
- **Vision-based document processing** using GPT-4 Vision
- **Vector database integration** for semantic search
- **Business rule validation** in AI systems
- **RAG implementation** with contextual metadata

## 🎓 Advanced Features

- **State-driven Processing**: LangGraph manages complex workflow state
- **Rich Metadata Storage**: Validation results stored with vector embeddings
- **Interactive Display**: Jupyter notebook shows all processed content
- **Comprehensive Testing**: Multiple query types with structured results
- **Professional Output**: Pandas DataFrames for business reporting

## 🔧 Troubleshooting

**PDF Processing Issues**: Ensure PDFs are readable and not password-protected
**API Errors**: Check API keys and rate limits
**Pinecone Connection**: Verify index name and API key
**Validation Accuracy**: Review business rules and adjust extraction prompts

---

This lab exercise demonstrates production-ready AI document processing with modern tools and best practices.
