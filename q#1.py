a = 1.0
b = "1"
c = "1.1"

# Print the outputs
print(a + float(b))
print(float(b) + float(c))
print(a + int(float(c)))
print(int(a) + int(float(c)))
print(a + int(c))  # This line cause  an error
print(2.0 * b)  # This line will also cause an error

