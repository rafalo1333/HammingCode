'''
Hamming module contains the Code class, that allows the user to count the
Hamming codes for their binary messages.

Made by Rafal Kaczor aka rafalo1333.
Lublin @ 2016.
'''

import math
import random


class CodeException(Exception):
    pass


class Code(object):
    '''Code class provides basic set of methods to count the Hamming code
    for binary message.
    '''

    def __init__(self, message):
        '''Class init method needs the message argument.'''
        if len(message) != 4:
            raise Exception('Hamming Code implementation supports only 4-digit messages!')
        self.message = message


class D3Code(Code):
    '''Class representing the Hamming code with d=3.'''

    def get_k(self):
        '''Returns the message's length.'''
        return len(self.message)

    def get_r(self):
        '''Returns the message's r number.'''
        k = self.get_k()
        return math.ceil(math.log(k, 2)) + 1

    # def get_message_matrix(self):
    #     '''Returns the message in the list format.'''
    #     return [int(i) for i in str(self.message)]

    def get_codes_matrix(self):
        '''Returns the matrix needed to calculate the Hamming Code for the
        message.'''
        codes_matrix = (
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1]
        )
        return codes_matrix

    def get_message_code(self):
        '''Returns the message's Hamming additional 3-digits code.'''
        codes_matrix = self.get_codes_matrix()
        msg_matrix = list(self.message)
        code = [0, 0, 0]

        for i in range(len(codes_matrix)):
            for j in range(len(msg_matrix)):
                code[i] = (codes_matrix[i][j] * msg_matrix[j] + code[i]) % 2

        return code

    def get_wrong_message(self):
        '''Returns the wrong message as list needed to test the Hamming Code.'''
        msg = list(self.message)
        index = random.randint(0, len(msg)-1)
        msg[index] = int(not msg[index])
        return msg

    def get_corrected_message(self, wrong_message):
        '''Returns the fixed message for a given wrong_message.'''
        msg_matrix = wrong_message
        code = self.get_message_code()
        new_code = [0, 0, 0]
        codes_matrix = self.get_codes_matrix()

        # get the comparison matrix

        for i in range(len(codes_matrix)):
            for j in range(len(msg_matrix)):
                new_code[i] = (codes_matrix[i][j] * msg_matrix[j] + new_code[i]) % 2

        rest = 0
        rev_code = list(reversed(code))
        rev_new_code = list(reversed(new_code))

        for i in range(len(code)):
            nr = (rev_code[i] + rev_new_code[i] + rest) % 2
            if rev_code[i] == 1 and rev_new_code[i] == 1:
                rest = 1
            else:
                rest = 0
            rev_code[i] = nr

        code = list(reversed(rev_code))


        index = None

        # find the index of error

        for i in range(len(codes_matrix)+1):
            _code = [codes[i] for codes in codes_matrix]
            if _code == code:
                index = i
                break

        # fix the error

        msg_matrix[index] = int(not msg_matrix[index])

        return msg_matrix

class D4Code(D3Code):
    '''Class representing the Hamming code with d=4.'''

    def get_r(self):
        '''Returns the message's r number.'''
        k = self.get_k()
        return math.ceil(math.log(k, 2)) + 2

    def get_codes_matrix(self):
        '''Returns the matrix needed to calculate the Hamming Code for the
        message.'''
        msg_matrix = (
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 0]
        )
        return msg_matrix

    def get_message_code(self):
        '''Returns the message's Hamming additional 3-digits code.'''
        codes_matrix = self.get_codes_matrix()
        msg_matrix = list(self.message)
        code = [0, 0, 0, 0]

        for i in range(len(codes_matrix)):
            for j in range(len(msg_matrix)):
                code[i] = (codes_matrix[i][j] * msg_matrix[j] + code[i]) % 2

        return code

    def get_corrected_message(self, wrong_message):
        '''Returns the fixed message for a given wrong_message.'''
        msg_matrix = wrong_message
        code = self.get_message_code()
        codes_matrix = self.get_codes_matrix()

        # get the comparison matrix

        for i in range(len(codes_matrix)):
            for j in range(len(msg_matrix)):
                code[i] = (codes_matrix[i][j] * msg_matrix[j] + code[i]) % 2

        index = None

        # find the index of error

        for i in range(len(codes_matrix)):
            _code = [codes[i] for codes in codes_matrix]
            if _code == code:
                index = i
                break

        # fix the error

        msg_matrix[index] = int(not msg_matrix[index])

        return msg_matrix

if __name__ == '__main__':
    # tests area
    c = D4Code((0, 0, 0, 1))
    print c.message, c.get_message_code()
    msg = c.get_wrong_message()
    print 'Wrong message: %s' % msg
    print c.get_corrected_message(msg)
