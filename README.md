# Python-Coding-Assignment-

The Antique Comedians of Malidinesia prefer comedies to tragedies. Unfortunately, most of the
ancient plays are tragedies. Therefore, the dramatic advisor of ACM has decided to transform
some tragedies into comedies. Obviously, this work is very hard. The basic sense of the play must
be kept intact, but all the elements of the play change to their opposites. For example, the
numbers: if any number appears in the tragedy, it must be converted to its reversed form before
being accepted into the comedy play.
A reversed number is a number written in Arabic numerals but the order of digits is reversed. The
first digit becomes last and vice versa. For example, if the main hero had 1245 strawberries in the
tragedy, he has 5421 of them now. Note that all the leading zeros are omitted. That means if the
number ends with a zero, the zero is lost by reversing (e.g. 1200 gives 21, not 0021). Also note that
the reversed number never has any trailing zeros (e.g. 0021 gives 12, not 12.00).


ACM needed to calculate with reversed numbers. The task was to add two reversed numbers and
output their reversed sum. Of course, the result was not unique, because any particular number is
a reversed form of several numbers (e.g. 21 could be 12, 120 or 1200 before reversing). It was
assumed that no zeros were lost by reversing (e.g. assumed that the original number was 12).
Regrettably, ACM hired the world’s first programming fish to complete the task. Although it saved
ACM some money, the fish was not a very good programmer and left some bugs in its code. Your
task is to identify and resolve these bugs, so ACM can finally produce its comedies.
Input
The input consists of N cases (equal to about 10000). The first line of the input contains only
positive integer N. Then follow the cases. Each case consists of exactly one line with two integers
separated by space. These are the reversed numbers you are to add.

