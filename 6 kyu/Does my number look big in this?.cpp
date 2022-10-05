//
//DESCRIPTION:
//
//A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
//
//For example, take 153 (3 digits), which is narcisstic:
//
//    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
//and 1652 (4 digits), which isn't:
//
//    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
//The Challenge:
//
//Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.
//
//Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.
//

#include <cmath>
bool narcissistic( int value )
{
    int x_10=0;
    int value_copy2=value;
    int value_copy=value;
    int s=0;
    while (value_copy>0)
    {
        x_10++;
        value_copy=value_copy/10;
    }
    for(int i=0;i<x_10;i++)
    {
        s+= pow(value%10,x_10);
        value = value/10;
    }
    //Code away
    if (value_copy2==s)
    {
        return true;
    }
    return false;
}