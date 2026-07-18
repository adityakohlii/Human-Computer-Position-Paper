import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N = 20000

# Each stage modeled as a lognormal distribution (latency is always positive,
# right-skewed - occasional slow outliers). Parameters (median, spread) are
# set from published benchmarks / reasonable engineering estimates, cited in
# the paper text. This is a computational feasibility simulation, not a
# claim about a measured physical system.

def lognormal_from_median(median_ms, sigma):
    mu = np.log(median_ms)
    return rng.lognormal(mu, sigma, N)

# Stage 1+2: signal acquisition + edge preprocessing
# Basis: embedded-classifier inference times reported for small on-device
# CNN/phoneme classifiers are typically single-digit to low-tens of ms;
# EMG sampling/windowing adds a fixed ~20-30ms buffer.
stage_acquisition = lognormal_from_median(45, 0.25)

# Stage: transmission to backend (edge device -> server)
# Basis: typical mobile/WiFi network RTT to a nearby edge server, 20-60ms.
stage_transmission = lognormal_from_median(35, 0.35)

# Stage: LLM inference, time-to-first-token
# Basis: published low-latency LPU inference services report time-to-first-token
# in the 100-300ms range for mid-size instruction-tuned models under load.
stage_llm = lognormal_from_median(170, 0.30)

# Stage: TTS streaming start
# Basis: streaming neural TTS systems report first-audio-chunk latency
# typically 30-80ms.
stage_tts = lognormal_from_median(50, 0.30)

total = stage_acquisition + stage_transmission + stage_llm + stage_tts

stages = {
    "Signal acquisition + edge preprocessing": stage_acquisition,
    "Transmission to backend": stage_transmission,
    "LLM inference (time-to-first-token)": stage_llm,
    "TTS streaming start": stage_tts,
}

print("Per-stage median and 90th percentile (ms):")
for name, arr in stages.items():
    print(f"  {name}: median={np.median(arr):.1f}, p90={np.percentile(arr,90):.1f}")

percentiles = [10, 25, 50, 75, 90, 95, 99]
print("\nEnd-to-end total latency percentiles (ms):")
results = {}
for p in percentiles:
    val = np.percentile(total, p)
    results[p] = val
    print(f"  p{p}: {val:.1f} ms")

threshold = 350  # ms, from Section 3.1 proposed threshold ceiling
frac_under = np.mean(total <= threshold) * 100
print(f"\nFraction of trials under {threshold}ms proposed threshold: {frac_under:.1f}%")

mean_total = np.mean(total)
std_total = np.std(total)
print(f"\nMean total latency: {mean_total:.1f} ms, SD: {std_total:.1f} ms")

# Save numeric summary for the paper table
with open("/home/claude/paper/sim_results.txt", "w") as f:
    f.write(f"N_trials={N}\n")
    f.write(f"mean={mean_total:.1f}\n")
    f.write(f"sd={std_total:.1f}\n")
    for p in percentiles:
        f.write(f"p{p}={results[p]:.1f}\n")
    f.write(f"frac_under_{threshold}ms={frac_under:.1f}\n")

# Histogram figure
fig, ax = plt.subplots(figsize=(7, 4.2), dpi=200)
ax.hist(total, bins=80, color="#5DCAA5", edgecolor="#0F6E56", linewidth=0.3)
ax.axvline(threshold, color="#D85A30", linestyle="--", linewidth=1.5,
           label=f"Proposed threshold ceiling ({threshold} ms)")
ax.axvline(np.median(total), color="#185FA5", linestyle="-", linewidth=1.5,
           label=f"Median ({np.median(total):.0f} ms)")
ax.set_xlabel("End-to-end latency (ms)", fontsize=11)
ax.set_ylabel("Simulated trials", fontsize=11)
ax.set_title("Monte Carlo simulation of end-to-end pipeline latency (N=20,000)", fontsize=11)
ax.legend(fontsize=9, frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("/home/claude/paper/latency_simulation.png", dpi=200)
print("\nFigure saved.")
