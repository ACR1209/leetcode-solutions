int reverse(int x) {
    // Initialize the reversed value to 0
    long long int reversed = 0;

    // Iterate over the digits of the input value
    while (x != 0) {
        // Extract the last digit of the input value
        int digit = x % 10;

        // Append the digit to the reversed value
        reversed = reversed * 10 + digit;

        // Remove the last digit from the input value
        x /= 10;
    }

    // Check if the reversed value is within the signed 32-bit integer range
    if (reversed < INT_MIN || reversed > INT_MAX) {
        return 0;
    }

    // Return the reversed value as a signed 32-bit integer
    return (int) reversed;
}
