from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

def get_qa_chain():
    model_name = "deepset/tinyroberta-squad2"  
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    # Hugging Face pipeline
    qa_pipeline = pipeline(
        "question-answering",
        model=model,
        tokenizer=tokenizer,
        device="cpu"  
    )

    hf_llm = HuggingFacePipeline(pipeline=qa_pipeline)

    return load_qa_with_sources_chain(hf_llm)