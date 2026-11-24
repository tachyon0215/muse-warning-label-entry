# muse-warning-label-entry

[![Competition](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/tachyon0215/muse-warning-label-entry/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![Reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/tachyon0215/muse-warning-label-entry/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the make.fun competition [Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

## The entry

> CAUTION: Human may appear calm while updating internally. Do not restart with sudden news, loud opinions, or the phrase 'we need to talk.'

## Why this line

Candidates: (A) contents under pressure since 1998, do not ask to pick brain before coffee, (B) may appear calm while updating internally, do not restart with 'we need to talk', (C) runs on snacks and sleep, advice voids the warranty. B won: exact printed-label rhythm, true of humans in general, turn held to the final phrase.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (length, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 2ff9216fd38b85a094e19157775f88f59124d6ee2c2fd7dc861fd56e8d002477).

## License

MIT - see [LICENSE](LICENSE).
