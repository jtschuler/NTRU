## NTRU

Justin Baum and Jadon Schuler
Dec 2, 2020
NTRU Cryptosystem

List of Files:  
src/decrypt.py:         Decryption driver  
src/defaults.py:        NTRU Arguments  
src/encrypt.py:         Encryption driver  
src/gen_key.py:         Key generation driver  
src/ntru.py:            NTRU functions  
src/polynomials.py:     Polynomial functions  
src/utils.py:           Modular arithmetic helper functions  

Built in Python 3.9

Dependencies:  
sympy

## Testing
To test a module, run the following:  
`python3 src/module.py -v`

## Key Generation
To generate keys, run the following:  
`src/gen_key.py -pub <pubkeyfile> -pri <prikeyfile>`

This generates and places the public key in <pubkeyfile> and the private key
information in <prikeyfile>.

## Message Encryption
To encrypt a message file, run the following:  
`src/encrypt.py -pub <pubkeyfile> -m <messagefile> -o <outputfile>`

This uses the public key in <pubkeyfile> to encrypt the message in
<messagefile>, and writes the cipher text as space separated integers into
<outputfile>.

## Message Decryption
To encrypt a message file, run the following:  
`src/encrypt.py -pri <prikeyfile> -m <messagefile> -o <outputfile>`

This uses the private key information stored in <prikeyfile> to decrypt the
message in <cipherfile>, and writes the decrypted message into <outputfile>.

## IMPORTANT
This implementation of NTRU assumes messages are encoded as ASCII text. The
message is encrypted using blocks of degree N polynomials, where coefficients
are the ASCII values of each byte. As such, we recommend values of p be no less
than 257. Values of q should be larger than p. Values for df should be no more
than N/2 (ceiling), while values of dg should be no more than N/2 (floor).
