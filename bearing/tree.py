"""The step tree: a way of approaching a complex system built with an AI. Not a check.

The checks measure drift. This is the shape of the work they measure drift *from*, written
down after Janaan on 2026-11-05, when an agent ran a disciplined loop for an afternoon inside
the wrong frame and one plain sentence from the author ("when a cloth is longer than the
person, it falls onto the floor") replaced it.

What the afternoon showed about the agent, which the tree is built around:

- **What it reaches for depends on the frame.** It knew how cloth software is built and that
  cloth falls; nothing in "the hem's shape is wrong" called for either. Asked how the field
  builds the thing, it answers well; mid-task, it rarely volunteers it. Step 1 asks.
- **It makes locally coherent work fast, and volume reads as progress.** Every record that
  afternoon was true; three versions of a fix were pointed the wrong way. Step 4's pause asks.
- **The person's best lever is a question about the frame,** often from an intuition they
  cannot yet justify. The tree spends that where it pays: at the pauses, not at every step.

It is a hypothesis about how to work, not a result. Each step carries where it came from and
how sure that is; step 3 is the least tested. Whether the tree helps is measured the plain way:
does the next project, started with it, need fewer of the author's steering corrections than
this one did?

Read it:
    python -m bearing --tree
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Step:
    n: str
    name: str
    ask: str
    why: str
    sure: str            # how much it rests on: "seen", "seen once", "hypothesis"
    check: str | None = None


STEPS: list[Step] = [
    Step("0", "the destination",
         "What would you see if it failed? Name the target as something observable.",
         "a measure that cannot come back bad is a horoscope (the whole of checks.py)", "seen"),
    Step("1", "the expert's map",
         "How is the nearest solved system built, what are its laws, and where does it usually "
         "break? Ask the agent outright, before building.",
         "Janaan: the agent knew a pattern-and-simulate cloth tool never sculpts a hem's 3D "
         "shape, and built a pipeline that draws the hem and pins it; nothing asked it to look", "seen once"),
    Step("2", "the laws",
         "What must the work never do? Each law with what checks it, in LAWS.md.",
         "Janaan: two unwritten laws (simulate, don't draw; no cloth crosses cloth) were broken "
         "for weeks under process rules that caught every false claim", "seen once", "no_laws"),
    Step("3", "a crude whole first",
         "Every stage end to end, badly, before any one stage well.",
         "an engine tutorial built a whole FPS in a few episodes this way; Janaan went "
         "depth-first, one opt-in stage per defect, and the stages interacted unseen (the "
         "photo-fit drew, the relax pinned). Untested on research-shaped work, where the whole "
         "may wait on one hard part", "hypothesis"),
    Step("4", "the loop",
         "Predict, run, measure, then LOOK at the picture before believing the number.",
         "the predictions caught every failure honestly; the sheets showed the tiers and the "
         "shelf that the outline numbers did not", "seen"),
    Step("4a", "the pause triggers",
         "Stop when: a fix fails twice; patches pile up; the effect is smaller than the noise; "
         "the person's intuition disagrees with the numbers.",
         "--floor-front v1 -> v3; ~30 opt-in flags; fold differences under Marigold's own 0.03 "
         "spread; the author's sentence", "seen once", "same_fix_again"),
    Step("5", "the pause",
         "Re-ask step 1 for the sub-problem. Is the fix upstream (the input) or downstream (the "
         "output)? Change the input and run again before reshaping the result.",
         "the day's one gain that held on both designs and both seeds changed the pattern; the "
         "reshaping made tiers, a shelf, and nothing", "seen once"),
    Step("6", "promote",
         "Each lesson becomes a law or a check, carried to the next project, not another flag.",
         "lessons.py, LAWS.md: the scar tissue is the most portable thing a project owns", "seen"),
]

ROLES = ("the agent: breadth, recall, tireless execution inside a frame",
         "the person: noticing the frame is wrong, often before it can be argued; "
         "say it early, as a question, and let the agent check it")


def render() -> str:
    out = ["The step tree. A way of working, not a check; a hypothesis, not a result.", "=" * 72, ""]
    for s in STEPS:
        ind = "   " if "a" in s.n else ""
        out.append(f"{ind}{s.n:<3} {s.name}  [{s.sure}]" + (f"  · checked by {s.check}" if s.check else ""))
        out.append(f"{ind}    {s.ask}")
        out.append(f"{ind}    from: {s.why}")
        out.append("")
    out.append("roles")
    out.extend(f"    {r}" for r in ROLES)
    out.append("")
    out.append("Measured by: does the next project need fewer of the author's steering corrections?")
    return "\n".join(out)
