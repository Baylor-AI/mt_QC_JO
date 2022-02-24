import numpy as np

ket_0 = np.array([1,0])
ket_1 = np.array([0,1])
print("The dot product between two states: ",np.dot(ket_0,ket_1))
hadamard = 1/np.sqrt(2) * np.array([[1,1],[1,-1]])
print(hadamard * hadamard)
print(np.dot(hadamard,ket_0))
print(np.dot(hadamard,ket_1))