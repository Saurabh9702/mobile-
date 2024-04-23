import numpy as np
import matplotlib.pyplot as plt
# Set the parameters
n_bits = 1000000 # Number of bits to be transmitted
SNRdBs = np.arange(-10, 11, 1) # SNR range in dB
SNRs = 10**(SNRdBs/10) # SNR range in linear scale
# Generate random bits
bits = np.random.randint(0, 2, n_bits)
# Loop over SNR values
BERs = []
for SNR in SNRs:
 # BPSK modulation
 symbols = 2*bits - 1
 # Add noise
 noise_power = 1/SNR
 noise = np.sqrt(noise_power)*np.random.randn(n_bits)
 received = symbols + noise
 # BPSK demodulation
 decoded_bits = (received >= 0).astype(int)
 # Calculate the bit error rate
 BER = np.sum(bits != decoded_bits) / n_bits
 BERs.append(BER)
# Plot the results
plt.semilogy(SNRdBs, BERs)
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate')
plt.title('Bit Error Rate vs. SNR for BPSK modulation with AWGN')
plt.grid(True)
plt.show()





