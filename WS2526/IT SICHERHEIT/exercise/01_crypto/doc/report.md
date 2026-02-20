1-
a)Confidentiality: preventing unauthorised reading/access/disclosure to resouces
-Mallory broke in, meaning she had access to all the resources of the home including private information

Integrity: preventing unauthorised changing resources
-Mallory could have changed whatever she pleases inside Alice's home

Availability: protection from unauthorised disruption of resources

b)
Prevention: change lock, better lock, put belongings in a secure safebox, hide the items well.
Detection: cameras, AI auto detection systems with notifying in case of intrusions.
Analysis: Figure out weak points in the house which were potentially used to break in, for example using a detective.


2-
vigenere cipher with a known key length of n.

since repetition is allowed

say we have 26 letters

then it is 26*26... n times which means 26^n



AES with a 256 bit key. now how does AES work? irrelevant i do know it is round based work including both substitution and permutations with the rounds scaling based on keysize. but the keyspace of a 256 bit key is simply 2^256



monoalphabetic substitution cipher with k letters.

in monoalphabetic no repetition

so k*k-1*k-2*..1

so k!





3- XOR is commutative. we have c0 and c1. and either m0 or m1.

since c0 = m0 xor k and we have m0 or m1. if we have m0 we do c0 xor m0 and receive k 
and since xor is self inverse 

m0 xor c0 =  m0 xor m0 xor k = k  = r0
m0 xor c1 = m0 xor m1 xor c1 = r1

and since we dont know whether what we have is m0 or m1 we just test the result on both and when both give the same result we know this is the right key.

we do c0* r0 and c0 * r1 and then also c1 * r0 and c0*r1 and then whenever one matches with the m we have this would be the correct r (result)






