# Voice AI Evaluation Pipeline

## Overview

This project implements a Python-based evaluation pipeline for Voice AI systems.
The system evaluates the quality of speech-to-text outputs using multiple metrics and generates a structured JSON report.

## Pipeline Architecture

Audio Input → Whisper Transcription → Evaluation Metrics → LLM-based Judgement → JSON Report

## Technologies Used

* Python
* OpenAI Whisper (speech-to-text transcription)
* Ollama with Phi-3 (LLM evaluation)
* SentenceTransformers (semantic similarity)
* JiWER (Word Error Rate calculation)

## Evaluation Metrics

The following metrics are used:

1. **Latency**
   Measures the time taken to process each audio sample.

2. **Word Error Rate (WER)**
   Measures transcription accuracy by comparing the original text with the AI-generated transcript.

3. **Semantic Similarity**
   Uses sentence embeddings to measure how similar the meanings of the original text and transcript are.

4. **Hallucination Rate**
   Flags outputs where semantic similarity is below a defined threshold.

5. **LLM Similarity Evaluation**
   A local LLM is used to judge semantic similarity between sentences.

## Project Structure

voice_ai_eval
│
├── main.py
├── metrics.py
├── transcriber.py
├── llm_evaluator.py
├── dataset.json
├── report.json
├── audio1.wav
├── audio2.wav

## Running the Evaluation

Run the evaluation pipeline using:

python main.py

The program will process the dataset and generate an evaluation report.

## Output

Results are saved in **report.json**, which includes:

* Original text
* Transcribed text
* Word Error Rate
* Semantic similarity
* LLM similarity score
* Hallucination flag
* Latency

## Deterministic Evaluation

The LLM evaluation uses temperature = 0 to ensure deterministic outputs across runs.

## Example Output

{
"audio_file": "audio1.wav",
"original_text": "what is the capital of japan",
"transcript": "what is the capital of japan",
"wer": 0.0,
"semantic_similarity": 1.0,
"llm_similarity": 1.0,
"hallucination": 0,
"latency": 0.85
}
