from functools import cache

mod = 10**9 + 7

@cache
def next_letter(letter):
    return chr((ord(letter) - ord('a') + 1) % 26 + ord('a'))

@cache
def trans(c: str, count: int):
    if count < 0:
        return 0

    if count == 1:
        if c == 'z':
            return 2
        else:
            return 1

    # count >= 2        
    if c == 'z':
        return (trans('a', count-1) + trans('b', count-1)) 
    
    # c is not z
    dist_to_z = ord('z') - ord(c)
    if count - dist_to_z <= 0:
        return 1

    return trans('z', count - dist_to_z) % mod


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        sum = 0
        for char in s:
            sum = (sum + trans(char, t)) % mod

        return sum