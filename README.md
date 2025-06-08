# CHEER-Ekman: Fine-grained Embodied Emotion Classification

Data released for [CHEER-Ekman paper](https://arxiv.org/abs/2506.01047). Also available on [Hugging Face](https://huggingface.co/datasets/menamerai/cheer-ekman).

## Usage: `count_labels.py`

Sample script interfacing the dataset. Counts the number of occurrences for each emotion label.

```shell
python count_labels.py <input_file> [--show-sentences] [--show-context]
```

Options:
- `<input_file>`: path to a JSON file containing a list of objects.
- `--show-sentences`: print each object’s reconstructed sentence from its `tokens` field.
- `--show-context`: print each object’s preceding context, joined from `preceding_context_tokens`.

Examples:
```shell
# just count labels
python count_labels.py data/dev.json

# count labels and show sentences
python count_labels.py data/dev.json --show-sentences

# count labels and show preceding context
python count_labels.py data/dev.json --show-context
```
