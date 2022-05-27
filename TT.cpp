#include <iostream>
using namespace std;
int check(int x, int y)
{
    return (x % y) ? y * (x / y + 1) - x : 0;
}
int main()
{
    int keyLen, depth;
    cout << "Enter the length of the key : ";
    cin >> keyLen;
    int key[keyLen];
    cout << "Enter the sequence key : ";
    for (int i = 0; i < keyLen; ++i)
        cin >> key[i];

    int order[keyLen];
    for (int i = 1; i <= keyLen; ++i)
        for (int j = 0; j < keyLen; ++j)
            if (key[j] == i)
                order[i - 1] = j;

    cout << "Enter the depth : ";
    cin >> depth;

    int strLen;
    cout << "Enter the length of String without spaces : ";
    cin >> strLen;
    int temp = check(strLen, keyLen);
    int r = (strLen + temp) / keyLen;
    char str[strLen + temp];
    char string[r][keyLen];

    if (temp > 0)
        cout << "You need to enter "
             << temp << " bogus characters. So enter total "
             << (strLen + temp) << " characters : ";
    else
        cout << "Enter the string : ";

    for (int i = 0; i < (strLen + temp); ++i)
        cin >> str[i];

    int count = 0;
    while (depth > 0)
    {
        count = 0;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < keyLen; ++j)
            {
                string[i][j] = str[count];
                count = count + 1;
            }
        cout << "\n";
        for (int i = 0; i < r; ++i)
        {
            for (int j = 0; j < keyLen; ++j)
                cout << string[i][j] << " ";
            cout << "\n";
        }
        count = 0;
        for (int i = 0; i < keyLen; ++i)
            for (int j = 0; j < r; ++j)
            {
                str[count] = string[j][order[i]];
                count = count + 1;
            }
        cout << "\n";
        for (int i = 0; i < (strLen + temp); ++i)
            cout << str[i];
        cout << "\n";
        depth--;
    }
    return 0;
}

/* OUTPUT :
shiva@localhost:~/Project/src$ g++ TT.cpp -o TT && ./TT
Enter the length of the key : 5
Enter the sequence key : 1 2 3 4 5
Enter the depth : 2
Enter the length of String without spaces : 25
Enter the string : ThisIsTheOriginalMessage.

T h i s I 
s T h e O 
r i g i n 
a l M e s 
s a g e . 

TsrashTilaihgMgseieeIOns.

T s r a s 
h T i l a 
i h g M g 
s e i e e 
I O n s . 

ThisIsTheOriginalMessage.
shiva@localhost:~/Project/src$
*/
