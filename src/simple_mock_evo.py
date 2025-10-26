import numpy as np
import matplotlib.pyplot as plt

# Mock time (0 to pi, 100 steps)
tlist = np.linspace(0, np.pi, 100)

# SEQ Pure: Coherent flip (cos wave – starts 1, dips 0, rebounds ~1)
expect_pure = np.cos(tlist)
entropy_final_pure = 8.67e-6  # Mock low entropy
delta_rho = 1.13e-6  # Mock seal

# Mixed Drag: Flat stuck at 0
expect_mixed = np.zeros_like(tlist)
entropy_final_mixed = 0.693  # Max rub

# Print metrics
print(f"Pure SEQ: <σ_z>_final = {expect_pure[-1]:.6f} | S_final = {entropy_final_pure:.2e} | Δρ = {delta_rho:.2e}")
print(f"Mixed Drag: <σ_z>_final = {expect_mixed[-1]:.6f} | S_final = {entropy_final_mixed:.3f}")

# Plot: Dance vs. drag
plt.plot(tlist, expect_pure, label='SEQ Pure (Virtual Qubit)')
plt.plot(tlist, expect_mixed, label='Classical Mixed (Drag)')
plt.xlabel('Time'); plt.ylabel('<σ_z>'); plt.legend()
plt.savefig('outputs/coherence_plot_mock.png')
plt.show()