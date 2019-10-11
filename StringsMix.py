"""
4 kyu - Strings Mix

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

https://www.codewars.com/kata/strings-mix/train/python
"""

# Todo : implement code for this problem :p

def mix(s1, s2):
    pass
    # your code

if __name__ == "__main__":
    print("Mix")
    print("Basic Tests")
    print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
    print(mix("looping is fun but dangerous", "less dangerous than coding"),
                       "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    print(mix(" In many languages", " there's a pair of functions"),
                       "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
    print(mix("codewars", "codewars"), "")
    print(mix("A generation must confront the looming ", "codewarrs"),
                       "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")