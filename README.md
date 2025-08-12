# CHEER-Ekman: Fine-grained Embodied Emotion Classification

Data released for [CHEER-Ekman paper](https://arxiv.org/abs/2506.01047) (ACL 2025). Also available on [Hugging Face](https://huggingface.co/datasets/menamerai/cheer-ekman).

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


## Citation

If you use this dataset, please cite us using:

```bibtex
@inproceedings{duong-etal-2025-cheer,
    title = "{CHEER}-{E}kman: Fine-grained Embodied Emotion Classification",
    author = "Duong, Phan Anh  and
      Luong, Cat  and
      Bommana, Divyesh  and
      Jiang, Tianyu",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-short.88/",
    doi = "10.18653/v1/2025.acl-short.88",
    pages = "1118--1131",
    ISBN = "979-8-89176-252-7",
}
```
