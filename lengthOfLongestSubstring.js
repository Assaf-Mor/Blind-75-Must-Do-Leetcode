/* Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 */

/**
 * @param {string} 
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
    let map = new Map();
    let currentIndex = 0;
    let maxLength = 0;
    for (i in s){
        if(!map.has(s[i])){
            map.set(s[i],currentIndex);
            currentIndex++;
            maxLength ++;
        }  
        else{
            let indexOfExisting = map.get(s[i]);
            if (indexOfExisting == currentIndex-1){
                map.clear();
                map.set(s[i], currentIndex);
                currentIndex ++;
                maxLength = 1;
            }
            else{
                map.delete(s[i]);
                map.set(s[i], currentIndex);
                currentIndex ++;
            }
        }
    }
    console.log(map);
    return maxLength;
};


console.log(lengthOfLongestSubstring("abcaabcdaba"));