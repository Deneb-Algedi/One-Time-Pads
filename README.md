# One-Time Pads


## Table of contents
- [Description](#description)
- [Vulnerability](#vulnerability)
- [References](#references)

## Description
One-Time Pad is a symmetric encryption method that was proposed by Mauborgne in 1917. It requires the key to be truly random, to have zero correlation with the plaintext and to not be repeated. Since the key is random the resulting ciphertext can map into any plaintext. 

## Vulnerability
In this challenge the application was using one-time pads to encrypt plaintext messages but used the same key for all. Therefore, being able to encrypt my own message of the same length (knowing what the plaintext of one of the messages is) in the application allowed me to take advantage of the following calculation: 


![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;C1={P1xorKEY})
![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;C2={P1xorKEY})

![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;C1xorC2={(P1xorKEY)xor(P2xorKEY)})
![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;C1xorC2={P1xorP2xorKEYxKEY})
![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;C1xorC2={P1xorP2xor0})
![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;C1xorC2={P1xorP2})
![\Large C1= P1 xor KEY](https://latex.codecogs.com/svg.latex?\Large&space;P1={C1xorC2xorP2})

## References


