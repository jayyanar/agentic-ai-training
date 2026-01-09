#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
from consent_auditor import ConsentAuditor

def main():
    parser = argparse.ArgumentParser(description="Consent Evidence Auditor")
    parser.add_argument("--setup", action="store_true", help="Setup Pinecone index")
    parser.add_argument("--server", action="store_true", help="Run FastAPI server")
    parser.add_argument("--ui", action="store_true", help="Run Streamlit UI")
    parser.add_argument("--classify", type=str, help="Classify a single document")
    parser.add_argument("--test", action="store_true", help="Test against sample documents")
    parser.add_argument("--invoice-demo", action="store_true", help="Run invoice processing demo")
    
    args = parser.parse_args()
    
    # Load environment variables
    if Path(".env").exists():
        with open(".env") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
    
    if args.setup:
        from setup_pinecone import setup_pinecone_index
        setup_pinecone_index()
        
    elif args.server:
        import uvicorn
        from server import app
        uvicorn.run(app, host="0.0.0.0", port=8000)
        
    elif args.ui:
        os.system("streamlit run streamlit_app.py")
        
    elif args.test:
        from test_documents import test_sample_documents
        test_sample_documents()
        
    elif args.invoice_demo:
        # Setup invoice policies first
        from setup_invoice_policies import setup_invoice_policies
        setup_invoice_policies()
        
        # Run demo
        from demo_invoice_processing import main as demo_main
        demo_main()
        
    elif args.classify:
        auditor = ConsentAuditor(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            pinecone_api_key=os.getenv("PINECONE_API_KEY"),
            pinecone_index_name=os.getenv("PINECONE_INDEX_NAME", "consent-auditor")
        )
        
        with open(args.classify, "rb") as f:
            content = f.read()
        
        case_id = f"cli_{Path(args.classify).stem}"
        result = auditor.process_document(case_id, content)
        
        print(f"Classification Result for {args.classify}:")
        print(f"Label: {result['label']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Rationale: {result['rationale']}")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
