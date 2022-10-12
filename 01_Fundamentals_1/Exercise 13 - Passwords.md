# [Passwords]
[Understanding how passwords work, hashing and salting.]

## Key terminology
[Hashing: The process of encrypting a given text by it into another fixed-length value that represents it. Hashing is done using algorithms. Hashing has many implementations. Storing passwords is one of the most important implementations of hashing.

Salting: The process of adding extra characters at the end of the password before hashing it, in order to make it even more secure and more difficult to crack.

Peppering: An additional step before hashing and beside salting that aimes to strengthen the password by adding extra characters to it. Pepper, unlike salt, is generaly added at the begining of a password.

Rainbow Table: A database where the hashed values for common and possible passwords are stored in order to use them to crack passwords later in what's known as "Rainbow Table Attack".

Bruteforce attack: a cyber attack that depends on analyzing the hash functions stored, generating hash values and comparing it to the hash values stored on the system being attacked.

MD5: MD5 Message-Digest Algorithm, is a commonly used hashing algorithm. It produces a 128-bit hash. Other commonly used hashing algorithms are for example; SHA-1, SHA-2 and LANMAN]

## Exercise
1. Hashing is considered more secure than symmetric encryption since it's a one-way process, while symmetric encryption is reversible, meaning that the cipher text can be transformed back into plain text using the right key.

2. A Rainbow table attack works by using stored hashed values of common and possible passwords and trying to gain access to a system using those values.

3. Tried to crack the passwords mentioned in the exercise as well as the password for my new user on the Linux VM. (See results in "Results" section)
### Sources
[1. https://www.techtarget.com/searchdatamanagement/definition/hashing

2. https://en.wikipedia.org/wiki/Salt_(cryptography)

3. https://www.geeksforgeeks.org/understanding-rainbow-table-attack/

4. https://www.sciencedirect.com/topics/computer-science/hashing-algorithm#:~:text=Some%20common%20hashing%20algorithms%20include,very%20commonly%20used%20hashing%20algorithm.

5. https://nordpass.com/blog/pepper-password/]

### Overcome challenges
[]

### Results
![Well_done](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ccc5879df578a287305a9c61c6cd2b6f7e4eb27f/00_includes/Security/Well_done.png)
![Not_found](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ccc5879df578a287305a9c61c6cd2b6f7e4eb27f/00_includes/Security/Not_found.png)
![Salted](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ccc5879df578a287305a9c61c6cd2b6f7e4eb27f/00_includes/Security/Salted.png)
![etc_shadow(1)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ccc5879df578a287305a9c61c6cd2b6f7e4eb27f/00_includes/Security/etc_shadow(1).png)
![etc_shadow(2)](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/ccc5879df578a287305a9c61c6cd2b6f7e4eb27f/00_includes/Security/etc_shadow(2).png)