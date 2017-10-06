'''
Reddit r/dailyprogrammer Challenge #330
https://www.reddit.com/r/dailyprogrammer/comments/6yep7x/20170906_challenge_330_intermediate_check_writer/
'''

__author__ = 'Zack Allen'

def int_to_string(input_number):
    """
    Takes in an integer from between 0-999 and returns a string representation of the integer in english.
    """
    #Array indices match value that will be found from modulus
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    int_string = "" #English words will be appended to this string

    if input_number == 0:
        return "zero "
    #Hundred section
    if input_number > 99:
        int_string += ones[(input_number-input_number%100)/100] + " hundred "
        pass
    #Tens
    if input_number%100 > 19 or input_number%100 == 10:
        int_string += tens[input_number%100/10] + " "
    #Teens
    if input_number%100 > 10 and input_number < 20:
        int_string += teens[input_number%10] + " "
    #Ones place
    elif input_number%10 > 0:
        int_string += ones[input_number%10] + " "
        pass

    return int_string

input_string = str(input("Enter a dollar amount:\n")) #User prompt
output_string = "" #All ouput will be appended to this string

#separate dollars and cents and thousands
if '.' in input_string:
    split_values = input_string.split(".")
    dollars = int(split_values[0])
    cents = int(split_values[1])
#No cents value
else:
    dollars = int(input_string)
    cents = 0

if dollars >999999 or dollars <0 or cents >99 or cents <0: #Check that dollar value is in range
    print "Invalid dollar/cents amount."
    exit(1)

thousands = (dollars -dollars%1000)/1000
hundreds = dollars%1000

if thousands >0 and hundreds >0:
    output_string += int_to_string(thousands) + "thousand, "
    output_string += int_to_string(hundreds) + "dollars and "
elif thousands >0 and hundreds == 0:
    output_string += int_to_string(thousands) + "thousand dollars and "
elif thousands == 0:
    output_string += int_to_string(hundreds) + "dollars and "

output_string += int_to_string(cents) + "cents." #cents output
output_string = output_string[0].capitalize() + output_string[1:] #Fixes first letter of any string
print output_string
exit(0)