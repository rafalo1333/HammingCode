from hamming import D3Code, D4Code

print 'Welcome to the Hamming Code CLI tester.'
print 'Please hit ENTER to enter your 4-digit message.'
message = raw_input()
message = [int(i) for i in message]
print 'Thanks. Your message is %s.' % message
print 'Select the Hamming Code mode: 0 for d=3, 1 for d=4.'
mode = input()
if mode == 0:
    print 'Running Hamming Code for d=3.'
    code = D3Code(message)
    print 'Code details: k=%s, r=%s, message additional code=%s.' % (code.get_k(), code.get_r(), code.get_message_code())
    wrong_message = code.get_wrong_message()
    print 'Wrong message is: %s' % wrong_message
    print 'Fixing message...'
    print 'Fixed message: %s.' % code.get_corrected_message(wrong_message)
elif mode == 1:
    print 'Running Hamming Code for d=4.'
    code = D4Code(message)
    print 'Code details: k=%s, r=%s, message additional code=%s.' % (code.get_k(), code.get_r(), code.get_message_code())
    wrong_message = code.get_wrong_message()
    print 'Wrong message is: %s' % wrong_message
    print 'Fixing message...'
    print 'Fixed message: %s.' % code.get_corrected_message(wrong_message)
else:
    print 'Wrong option. Run the program again, please.'
