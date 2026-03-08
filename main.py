import json
import time

from transcriber import transcribe
from metrics import calculate_wer, semantic_similarity, hallucination_rate
from llm_evaluator import llm_similarity


with open("dataset.json") as f:
    dataset = json.load(f)

results = []

for item in dataset:

    audio = item["audio_file"]
    original = item["original_text"]

    start = time.time()

    transcript = transcribe(audio)

    wer_score = calculate_wer(original, transcript)

    semantic_score = semantic_similarity(original, transcript)

    llm_score = llm_similarity(original, transcript)

    hallucination = hallucination_rate(semantic_score)

    latency = time.time() - start

    result = {
        "audio_file": audio,
        "original_text": original,
        "transcript": transcript,
        "wer": wer_score,
        "semantic_similarity": semantic_score,
        "llm_similarity": llm_score,
        "hallucination": hallucination,
        "latency": latency
    }

    results.append(result)


with open("report.json", "w") as f:
    json.dump(results, f, indent=4)

print("Evaluation complete. Report saved to report.json")