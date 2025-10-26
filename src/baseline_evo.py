import qutip as qt
import numpy as np
import matplotlib.pyplot as plt  # For plot

tlist = np.linspace(0, np.pi, 100)  # Rotation period
sigma_x, sigma_z = qt.sigmax(), qt.sigmaz()

# SEQ Pure (virtual low-entropy)
psi0 = qt.basis(2, 0); rho_pure = psi0 * psi0.dag()
H = sigma_x
result_pure = qt.mesolve(H, rho_pure, tlist, [], [sigma_z])
expect_pure = result_pure.expect[0]
entropy_final_pure = qt.entropy_vn(result_pure.states[-1])
delta_rho = (result_pure.states[-1] - rho_pure).norm()

# Classical Mixed (high-entropy drag)
rho_mixed = qt.qeye(2) / 2
result_mixed = qt.mesolve(H, rho_mixed, tlist, [], [sigma_z])
expect_mixed = result_mixed.expect[0]
entropy_final_mixed = qt.entropy_vn(result_mixed.states[-1])

# Output metrics
print(f"Pure SEQ: <σ_z>_final = {expect_pure[-1]:.6f} | S_final = {entropy_final_pure:.2e} | Δρ = {delta_rho:.2e}")
print(f"Mixed Drag: <σ_z>_final = {expect_mixed[-1]:.6f} | S_final = {entropy_final_mixed:.3f}")

# Plot: Coherence vs. drag
plt.plot(tlist, expect_pure, label='SEQ Pure (Virtual Qubit)')
plt.plot(tlist, expect_mixed, label='Classical Mixed (Drag)')
plt.xlabel('Time'); plt.ylabel('<σ_z>'); plt.legend(); plt.savefig('../outputs/coherence_plot.png')
plt.show()  # Or comment for headless