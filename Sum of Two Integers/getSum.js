/* Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5
 */

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
 var getSum = function(a, b) {
    let result = a ^ b; // XOR both integers to get the sum without the carry
    let carry = a & b; // AND both integers to get the carry 
    while (carry != 0){ 
        let shift = carry << 1; // shift the carry by one to get the shifted carry
        carry = result & shift; // 
        result = result ^ shift;
    }
    return result;
};