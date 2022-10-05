//
// Given the triangle of consecutive odd numbers:
//
//             1
//          3     5
//       7     9    11
//   13    15    17    19
//21    23    25    27    29
//...
//Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
//
//1 -->  1
//2 --> 3 + 5 = 8
//
long long rowSumOddNumbers(unsigned n){
    int sum=0,l=1,r=1;
    int l2=2,r2=4;
    for (int i=1;i<n;i++)
    { l+=l2;
        r+=r2;
        l2+=2;
        r2+=2;
    }
    if (n==1){return 1;};
    while(l!=r)
    {
        sum+=l;
        l+=2;
    }
    return sum+r;
    //your code here
}
