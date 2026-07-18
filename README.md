# Toward Seamless Cognitive Coupling

**A Phenomenological Framework for Non-Invasive, Real-Time Human–AI Knowledge Access**

Aditya Gurjar · Department of Mechanical Engineering, National Institute of Technology Jamshedpur

---

## Overview

This repository contains a research position paper proposing the **Latency-Threshold Model of Cognitive Ownership** — a framework arguing that the subjective sense of "already knowing" something is governed not by where information is stored, but by three engineerable factors: **response latency, contextual precision, and delivery modality**.

The paper proposes a six-layer, non-invasive system architecture that reframes an unsolved neuroscience problem (decoding complete thoughts from neural signal) into a tractable engineering problem (fusing a weak neural signal with contextual data to infer probable intent), and backs the design with:

- A literature grounding in the Extended Mind thesis (Clark & Chalmers), sense-of-agency research (Haggard), and predictive processing (Friston)
- A **Monte Carlo latency simulation** (20,000 trials) showing a median end-to-end pipeline latency of 306.5 ms, with 76.1% of trials within the proposed 350 ms threshold
- A complete, IRB-approvable **human evaluation protocol** for testing the model's core hypotheses (H1–H3)
- An explicit **ethical scope**, excluding covert use in adversarial/evaluative contexts (exams, interviews) and restricting proposed use to transparent, disclosed applications such as emergency legal/civic literacy access and accessibility support

## Status

This is a **position paper** — it proposes a theoretical framework, system architecture, and simulation-based feasibility analysis. No human-subject data has been collected yet; the evaluation protocol (Section 7) is proposed as the next research step, not reported as completed work.

## Contents

- `Cognitive_Coupling_Position_Paper.docx` — full paper
- `architecture_diagram.png` — Figure 1: six-layer system architecture, annotated by feasibility
- `latency_simulation.png` — Figure 2: Monte Carlo latency distribution
- `simulate_latency.py` — simulation source code (reproducible; parameters and citations documented in-line)

## Reproducing the Simulation

```bash
pip install numpy matplotlib
python3 simulate_latency.py
```

## Citation

If referencing this work, please cite as:

> Gurjar, A. (2026). *Toward Seamless Cognitive Coupling: A Phenomenological Framework for Non-Invasive, Real-Time Human–AI Knowledge Access.* Position paper, National Institute of Technology Jamshedpur.

## License

- Paper text and figures: [CC BY 4.0](LICENSE) — free to share and adapt with attribution.
- Simulation code (`simulate_latency.py`): [MIT License](LICENSE-CODE).

Before submitting to any conference (e.g. HCII 2027), check that venue's copyright/licensing policy, as publisher agreements can affect what remains openly licensed here.
