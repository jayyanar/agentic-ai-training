# Add this cell BEFORE the workflow nodes:

# Load and inspect all PDFs first
data_dir = Path("data")
pdf_files = list(data_dir.glob("invoice_*.pdf"))

print(f"📁 Found {len(pdf_files)} PDF files")
print("=" * 50)

pdf_metadata = []

for pdf_file in sorted(pdf_files):
    print(f"\n📄 Loading: {pdf_file.name}")
    
    try:
        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()
        
        if docs:
            full_text = "\n".join([doc.page_content for doc in docs])
            file_size = pdf_file.stat().st_size
            
            metadata = {
                'filename': pdf_file.name,
                'file_size_kb': round(file_size / 1024, 1),
                'pages': len(docs),
                'text_length': len(full_text),
                'text_preview': full_text[:150].replace('\n', ' ').strip() + '...',
                'full_text': full_text
            }
            
            pdf_metadata.append(metadata)
            
            print(f"✅ {len(docs)} pages, {len(full_text)} chars, {metadata['file_size_kb']} KB")
            print(f"Preview: {metadata['text_preview']}")
        else:
            print("❌ No content extracted")
            
    except Exception as e:
        print(f"❌ Error loading {pdf_file.name}: {e}")

print(f"\n✅ Successfully loaded {len(pdf_metadata)} PDFs")

# Update the PDF loader node to use pre-loaded data:
def pdf_loader_node(state: InvoiceState) -> InvoiceState:
    filename = state['filename']
    pdf_data = next((pdf for pdf in pdf_metadata if pdf['filename'] == filename), None)
    
    if pdf_data:
        state["doc_text"] = pdf_data['full_text']
        print(f"✅ Using pre-loaded: {pdf_data['pages']} pages, {pdf_data['file_size_kb']} KB")
    else:
        state["doc_text"] = "File not found"
        print(f"❌ No data for {filename}")
    
    return state

# Update the results table to include metadata:
# In the results display cell, add these columns:
display_df = pd.DataFrame({
    'Invoice File': df['filename'],
    'Pages': [next((pdf['pages'] for pdf in pdf_metadata if pdf['filename'] == f), 0) for f in df['filename']],
    'Size (KB)': [next((pdf['file_size_kb'] for pdf in pdf_metadata if pdf['filename'] == f), 0) for f in df['filename']],
    'Vendor Name': df['vendor_name'].str[:20],
    'Invoice Number': df['invoice_number'],
    'Date': df['date'],
    'Amount': df['amount'],
    'Validation': df['validation_result'],
    'Reasoning': df['reasoning'].str[:30] + '...'
})
