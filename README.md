# virtual-quantum-dawn-seq

SEQ Simulation Suite: TSTOEAO transmutes classical CPUs into virtual qubits – Willow confirmed, entropy cycled. (Preprint: zenodo.org/records/17446674)

Virtual Quantum Dawn: SEQ Sim



This shows how SEQ turns a regular computer into a virtual qubit shadow—no special hardware.



How to Run:

1\. Clone the repo: git clone https://github.com/tstoeao/virtual-quantum-dawn-seq.git

2\. cd virtual-quantum-dawn-seq

3\. pip install numpy matplotlib

4\. python src/simple\_mock\_evo.py



Output: Pure SEQ line flips (starts 1, dips 0, ends -1), mixed line flat at 0. Plot saves to outputs/coherence\_plot\_mock.png.



Tweak: Change line 6 to tlist = np.linspace(0, 2\*np.pi, 100) for full rebound to +1.



Based on TSTOEAO SEQ: Entropy as balance, not loss.

