import matplotlib.pyplot as plt
import numpy as np

# Generate stress-strain data for stainless steel (representative)
strain = np.linspace(0, 0.25, 500)
stress = np.piecewise(
    strain, 
    [strain <= 0.005, (strain > 0.005) & (strain <= 0.02), strain > 0.02],
    [lambda x: 200000 * x,  # Linear elastic region
     lambda x: 1000 + (x - 0.005) * 10000,  # Yield plateau
     lambda x: 1200 + (x - 0.02) * 5000]  # Strain hardening
)

# Plotting the curve
plt.figure(figsize=(10, 6))
plt.plot(strain, stress, label="Stress-Strain Curve", color="blue")
plt.axvline(x=0.005, linestyle="--", color="gray", label="Elastic Limit")
plt.axvline(x=0.02, linestyle="--", color="red", label="End of Yield Plateau")
plt.title("Stress-Strain Curve for Stainless Steel")
plt.xlabel("Strain (mm/mm)")
plt.ylabel("Stress (MPa)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()
