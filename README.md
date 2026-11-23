# A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/mitsukikun/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/mitsukikun/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun bounty "A Day of One-Line Pitches" — one
sentence, 240 characters at most, that would convince a friend who has
never coded to let an AI agent build their first app idea on make.fun.
The program writes the pitch to `/output/entry.txt` (pure Python 3
standard library, no network, fully deterministic).

> Type your app idea into make.fun in plain words, watch an AI agent build it live, and click around your own working app minutes later — no coding, no setup, just your idea.

## Run it

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise to
`/output`.

## Verify locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-pitches-1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out-pitches-2 python3 main.py
cmp /tmp/out-pitches-1/entry.txt /tmp/out-pitches-2/entry.txt
cat /tmp/out-pitches-1/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>
