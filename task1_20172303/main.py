# import numpy, matplotlib, math
import numpy as np
import math

class RandomNumGenerator(object):


    def __init__(self, seed, distribution_type):
        self.seed = seed
        self.randState = np.random.RandomState(seed)
        self.distribution_type = distribution_type


    def generate(self, num_samples):
        packet = self.randState.rand(num_samples)
        return packet

    def generate_distribution(self, num_samples):
        if self.distribution_type.lower() == 'normal':
            # According to the Box-Muller Transformation,
            # which can be found in: http://mathworld.wolfram.com/Box-MullerTransformation.html
            uniform_packet_1 = self.generate(num_samples)
            uniform_packet_2 = self.generate(num_samples)
            packet = np.sqrt(-2 * np.log(uniform_packet_1)) * np.cos(2 * math.pi * uniform_packet_2)
        # elif self.distribution_type.lower() == 'triangular':
        # Throw an exception for distributions not implemented
        return packet



num_array = RandomNumGenerator(25, 'normal')
print(num_array.generate_distribution(1000))

# Create general random number generator (Class)
# Parameters: seed, number of samples, distribution_type

# Implement for a normal distribution (Class)
# Use Box-Muller

# Implement for any arbitrary distribution (Class)
# Parameters: distribution type, distribution parameters

# Plot results
# Plot for PDF
# Plot for CDF
