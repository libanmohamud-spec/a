#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EX_DIR = ROOT / "exercises"
RESULTS_DIR = ROOT / "results"


def discover(pool_name: str) -> list[str]:
    pool_dir = EX_DIR / pool_name
    if not pool_dir.exists():
        return []
    return sorted([p.name for p in pool_dir.iterdir() if p.is_dir()])


def pick_items(rng: random.Random, items: list[str], k: int) -> list[str]:
    if k > len(items):
        raise ValueError(f"Not enough items in pool: need {k}, have {len(items)}")
    return rng.sample(items, k)


def main():
    ap = argparse.ArgumentParser(description="Initialize participant session and select exercises")
    ap.add_argument("participant_id", help="Unique participant identifier")
    ap.add_argument("experience", choices=["yes", "no"], help="Programming experience answer")
    ap.add_argument("--rounds", type=int, default=2, help="Number of rounds (default 2)")
    args = ap.parse_args()

    pid = args.participant_id.strip()
    experienced = args.experience == "yes"

    # Seed RNG by stable hash of participant id
    seed = int(hashlib.sha256(pid.encode("utf-8")).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)

    pools = {
        "easy": discover("easy"),
        "medium": discover("medium"),
        "hard": discover("hard"),
    }

    if experienced:
        # Y: Round1 M+H, Round2 M+H
        need = [
            ("round1", [("medium", 1), ("hard", 1)]),
            ("round2", [("medium", 1), ("hard", 1)]),
        ]
    else:
        # N: Round1 E+M, Round2 E+M
        need = [
            ("round1", [("easy", 1), ("medium", 1)]),
            ("round2", [("easy", 1), ("medium", 1)]),
        ]

    # We must ensure no replacement across rounds for each pool
    chosen: dict[str, list[str]] = {k: [] for k in pools}
    rounds: dict[str, list[dict]] = {}

    for round_name, specs in need:
        round_picks = []
        for pool_name, k in specs:
            available = [x for x in pools[pool_name] if x not in chosen[pool_name]]
            picks = pick_items(rng, available, k)
            chosen[pool_name].extend(picks)
            for p in picks:
                round_picks.append({"pool": pool_name, "exercise": p})
        rounds[round_name] = round_picks

    meta = {
        "participant_id": pid,
        "experienced": experienced,
        "pools_sizes": {k: len(v) for k, v in pools.items()},
        "assignments": rounds,
        # Round 2 enables LLM
        "allow_llm": {"round1": False, "round2": True},
        "seed": seed,
        "version": 1,
    }

    out_dir = RESULTS_DIR / pid
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "assignment.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print(f"Wrote assignment plan to {out_dir / 'assignment.json'}")
    print("Round 1 selections:")
    for e in meta["assignments"]["round1"]:
        print(f"  - {e['pool']}/{e['exercise']}")
    print("Round 2 selections:")
    for e in meta["assignments"]["round2"]:
        print(f"  - {e['pool']}/{e['exercise']}")


if __name__ == "__main__":
    main()

