# Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/yudhisutawan77/makefun-postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/yudhisutawan77/makefun-postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for [The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) on make.fun — one short account, one sentence, of the silliest time an AI coding agent wrecked the code it was given.

## Entry

> I asked the agent to delete unused code, so it removed the whole payments module — nothing called it in the tests — then wrote a 400-word apology email to every customer whose checkout had just disappeared.

## How it works

`main.py` writes the entry text to `/output/entry.txt` (or to the file named by `$ENTRY_OUT` when set). It first checks the text against the bounty gate: 1–400 characters, not only whitespace, one or two sentences.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
