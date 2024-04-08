import os
import time
import logging
from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from .models import Sentence
from .keyword_extractor import keyword_extractor
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


app = FastAPI(
    title="Keyword Extractor API",
    description="Extract keywords from a sentence",
    version="1.0.0",
    docs_url="/"
)

gunicornLogger = logging.getLogger('gunicorn.error')
logger.handlers = gunicornLogger.handlers
logger.setLevel(gunicornLogger.level)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("ALLOW_ORIGINS")
    ],
    allow_methods=[
        "POST"
    ],
    allow_headers=["*"]
)

tokenizer = AutoTokenizer.from_pretrained("transformer3/H1-keywordextractor")
model = AutoModelForSeq2SeqLM.from_pretrained("transformer3/H1-keywordextractor")


@app.post("/api/v1/extract-keywords")
def extract_keywords(sentence: Sentence):
    now = time.perf_counter()
    extracted_keywords =  keyword_extractor(sentence.text, tokenizer, model)
    gunicornLogger.info(f"Took {time.perf_counter() - now:.2f}s to extract keywords: {extracted_keywords}")
    return [
        {
            "summary_text": extracted_keywords
        }
    ]
