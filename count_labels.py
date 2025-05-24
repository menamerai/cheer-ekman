#!/usr/bin/env python3
import json
import argparse
from collections import Counter


def count_labels(data):
    """Count occurrences of each label in the list of objects."""
    counter = Counter()
    for obj in data:
        label = obj.get("label")
        if label is not None:
            counter[label] += 1
    return counter


def tokens_to_sentence(obj):
    """Join the list of tokens into a single sentence string."""
    tokens = obj.get("tokens", [])
    return " ".join(tokens)


def preceding_context_to_text(obj):
    """Join nested preceding_context_tokens lists into a combined text string."""
    contexts = obj.get("preceding_context_tokens", [])
    sentences = [" ".join(sent) for sent in contexts]
    return " ".join(sentences)


def main():
    parser = argparse.ArgumentParser(
        description="Count labels in a JSON file and optionally display sentences from tokens."
    )
    parser.add_argument(
        "input_file", help="Path to the input JSON file (list of objects)"
    )
    parser.add_argument(
        "--show-sentences", action="store_true",
        help="Also print a sentence per object by joining its tokens"
    )
    parser.add_argument(
        "--show-context", action="store_true",
        help="Also print preceding context sentences for each object"
    )
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of objects.")

    if args.show_sentences and args.show_context:
        print("\nSentences with preceding context:")
        for idx, obj in enumerate(data, start=1):
            ctx = preceding_context_to_text(obj)
            sent = tokens_to_sentence(obj)
            print(f"{idx}: {ctx} | {sent}")
    elif args.show_sentences:
        print("\nSentences:")
        for idx, obj in enumerate(data, start=1):
            sent = tokens_to_sentence(obj)
            print(f"{idx}: {sent}")
    elif args.show_context:
        print("\nPreceding contexts:")
        for idx, obj in enumerate(data, start=1):
            ctx = preceding_context_to_text(obj)
            print(f"{idx}: {ctx}")

    counts = count_labels(data)
    print("\nLabel counts:")
    for label, count in counts.items():
        print(f"{label}: {count}")


if __name__ == "__main__":
    main()
