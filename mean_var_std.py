import numpy as np
import pprint

# The function that does the calculations
def calculate(input_list):
    # Check if the input list has exactly 9 elements
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Reshape the input list into a 3x3 matrix
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calculate required statistics and store them in a dictionary
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]
    }

    return calculations

# Test function to execute the tests
def run_tests():
    # Test 1: Correct input
    test_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    print("✅ Test Passed!")
    print("Output:")

    pprint.pprint(calculate(test_input))

    # Test 2: Error case - handling invalid input
    test_input_invalid = [1, 2, 3]  
    try:
        # This will raise a ValueError because there are not 9 numbers
        calculate(test_input_invalid)
    except ValueError as e:
      
        print("✅ Correctly raised ValueError:", e)

# Ensure the tests are only run when the script is executed directly
if __name__ == '__main__':
    run_tests()  
