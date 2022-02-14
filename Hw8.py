#One control function defined...
def CyclicRedundancyCheck(message, PolDiv, remain='00000000'):
    #We first assume the remaining value as "00000000" so that the remaining value we want to reach is error-free.
    message = message + remain
    #The listing method was used to check each bit one by one.
    message = list(message) 
    PolDiv = list(PolDiv)

    #To check the message sent, we need to create two nested loops.
    for m in range(len(message)-len(remain)):
    #Each value of the sent message bit is checked. If the value is 1, Modulo 2 calculation is made.
        if message[m] == '1':
            for n in range(len(PolDiv)):
    #The modulo 2 function is useful for multiplying if there are binary values and then ignoring the remainder.
                message[m+n] = str((int(message[m+n])+int(PolDiv[n]))%2)

    #It sends back the last error portion of the message sent to us.
    return ''.join(message[-7:])


# For Genarator Polynomial G1(x) 
print('##### For Genarator Polynomial G1(x) #####')
message = '01010101010101010101010101010100'  #Error pattern not detected by the polynomial
message1 = '01110101010101010101010101010101' #2-Bits Error Message
message2 = '01110111010101011101010101010101' #4-Bits Error Message

G1 = '10101'# Given Divisor Polynom: x^4 + x^2 + 1

print('Input Message: ', message) 
print('2-bits Error Message: ', message1)
print('4-bits Error Message: ', message2)
print('Divisor:', G1)

#With the first message entered and later entered incorrect messages, the function is called to have the remainder.
remain = CyclicRedundancyCheck(message, G1)
remain1 = CyclicRedundancyCheck(message1, G1)
remain2 = CyclicRedundancyCheck(message2, G1)

print('Remainder Error Sequence For 2-bits: ', remain1)
print('Remainder Error Sequence For 4-bits: ', remain2)
print('Remainder For No Error Sequence: ', remain ,"\n")

# For Genarator Polynomial G2(x)
print('###### For Genarator Polynomial G2(x) #####')
message = '11000101110001011100010111000101'  #Error pattern not detected by the polynomial
message1 = '11010101110011011100010111001111' #2-Bits Error Message
message2 = '11010111110011011101010111001111' #4-Bits Error Message

G2 = '11000101'# Given Divisor Polynom: x^7 + x^6 + x^2 + 1


print('Input Message: ', message)
print('2-bits Error Message: ', message1)
print('4-bits Error Message: ', message2)
print('Divisor:', G2)

#With the first message entered and later entered incorrect messages, the function is called to have the remainder.
remain = CyclicRedundancyCheck(message, G2) 
remain1 = CyclicRedundancyCheck(message1, G2)
remain2 = CyclicRedundancyCheck(message2, G2)

print('Remainder Error Sequence For 2-bits: ', remain1)
print('Remainder Error Sequence For 4-bits: ', remain2)
print('Remainder For No Error Sequence: ', remain ,)

#The G2 polynomial has a higher error detection rate because its degree 
#is higher and can provide more bit control (8bits), but G1 provides less control (5bits).