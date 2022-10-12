# [Symmetric encryption]
[Getting to know symmetric encryption techniques and methods and apply it with teammates.]

## Key terminology
[Data at rest: A data that's stored on a computer and (temporarily) not being transfered or processed.

Data in motion: A data that's being trasfered between different locations. Also called, data in transit or data in flight.

Data in use: A data that's being accessed, modified or processed. That data is usually stored on a computer's RAM, and is considered the most vulnerable state of data.

Cipher: Any technique that's used to encrypt and decrypt data. 

Cryptography: The discipline and the practice of encrypting plain text into cipher text and decrypting it back.

Symmetric encryption: The type of cryptography where one secret key is used to both encrypt as well as decrypt data.

Caesar cipher: Is an ancient technique for encrypting that's traced back to the Roman empire, where Julius Caesar used to use that technique to communicate sensitive data with his officials. Caeser cipher depends on shifting each letter in a text a certain number of positions forward and replacing it with the letter in that position when encrypting, and moving it backwards for the same number of positions to get the original text back while decrypting. That number of positions is called "the shift" and should be agreed on as the key to encrypt or decrypt between the involved parties. The shift is determined based on numbering the alphabets in order from A to Z. For example; shift 2 for the letter A means that it'd be replaced with the letter C in the encrypted text.

Aberti cipher: An encryption technique that's traced back to middel age Italy. It's another technique that depends on replacing letters with others, but this time based on what's called "cipher disk", which is two concentric disks. The outer disk is called "stationary disk" and contains the upper case alphabets and the numbers from 1 to 4, and the inner disk is called "movable disk" and contains the lower case alphabets.

Morse code: A relatively old and a quite famous electrical telegraphic encrypting technique that's traced back to the begining of the 19th century in the United States, and is named after one of its developers, Samuel Morse. It can be considered as a language that replaces letters and numbers with electrical telegraphic signals as dots and dashes, also called "dits" and "dahs".

Block cipher: A digital data encoding method that works by breaking down the data into fixed size chunks which then get encrypted by applying a key to each chunk.

Stream cipher: A digital data encoding method that works by applying a bit key to each individual bit in the data in order to encrypt it.

DES: Data Encryption standard, is a block cipher algorithem developed by IBM in 1970. It applies mathmatical operations on blocks of plain text in order to encrypt it into a bitstring of the same length as the original block. It is considered not secure enough for modern day communications due to its too short key length of 56-bit.

IDEA: International Data Encryption Algorithm, is a block cipher algorithem developed in Zurich 1991. It applies a 128-bit key on each 64-bit block of data on 8 and a half rounds of operations. It is generaly considered secure and is commonly used till nowadays.]

## Exercise
1. and 2. (See "Key Terminology" section above).

3. Using asymmetric encryption from assignment SEC-05 (corresponds to "Fundamentals/ Exercise 11" in this repository), together with my teammates Jaya and Wim were able to encrypt our symmetric keys asymmetrically, and therefore each one of us was able to share their encrypted secret key in public without any risk of it being exposed as plain text, since only the intended receiver can decrypt it with their private key that correlates with the public key with which the secret symmetric key was encrypted. (See results in "Results" section at the end of this document)

### Sources
[1. https://www.cryptomathic.com/news-events/blog/symmetric-key-encryption-why-where-and-how-its-used-in-banking

2. https://www.comparitech.com/blog/information-security/famous-codes-and-ciphers-through-history-and-their-role-in-modern-encryption/

3. https://www.hypr.com/security-encyclopedia/symmetric-cipher

4. https://www.techtarget.com/searchdatamanagement/reference/states-of-digital-data

5. https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

6. https://en.wikipedia.org/wiki/Alberti_cipher

7. https://en.wikipedia.org/wiki/Morse_code

8. https://www.thesslstore.com/blog/block-cipher-vs-stream-cipher/#:~:text=A%20block%20cipher%20breaks%20down,into%20ciphertext%20using%20key%20bits.

9. https://en.wikipedia.org/wiki/Data_Encryption_Standard#Description

10. https://en.wikipedia.org/wiki/International_Data_Encryption_Algorithm

11. https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:data-encryption-techniques/a/public-key-encryption

12. https://www.devglan.com/online-tools/aes-encryption-decryption]

### Overcome challenges
[In the begining I wasn't quite sure how to accomplish the exercise the way it was meant to be accomplished (by sharing the the sercret key in a public enviroment while keeping it secret), but starting with the next assignment about asymmetric encryption first, based on my learning coach's advice, cleared up the way.]

### Results
![Asymmetrically_encrypted_symmetric_key](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/2ecd3f57f7900de3a97b67f9534340814333fe58/00_includes/Security/Asymmetrically_encrypted_symmetric_key.png)
![Symmetric_encryption](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/2ecd3f57f7900de3a97b67f9534340814333fe58/00_includes/Security/Symmetric_encryption.png)
![Wims_decrypted_message](https://github.com/Techgrounds-Cloud-9/cloud-9-Atalla90/blob/2ecd3f57f7900de3a97b67f9534340814333fe58/00_includes/Security/Wims_decrypted_message.PNG)