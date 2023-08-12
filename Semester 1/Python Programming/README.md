# Python-Assignments

This repository Contains the following Questionares / Problem statements. The key for these Question are uploaded once I complete my code which are indexed at bottom

<H1>PROBLEM STATEMENTS</H1>

1.	Write a function def check_cipher (plain, cipher) which when given a plain text and a possible cipher text, the function returns True if the cipher text can be formed from the plain text using the above mentioned scheme otherwise False. Assume that all the strings are in uppercase.
For example:
plain = 'PYTHON'
cipher = 'TDMSUY'
print(check_cipher(plain, cipher))
should output: True
HINT: The alphabets are enumerated as A = 0, B = 1, C = 2, … , Z = 25. Consider an encryption scheme where a character with value C[i] in the plaintext is replaced by another character with value C[j] using the formula C[j] = (C[ i ] + 5) % 26. After replacement, the resulting string is shuffled (permuted) at random to obtain the cipher text. 

<hr>

2.	Write a function stud_rank(details) which performs the following actions:
	 Details is a dictionary given as input argument.
	Calculates the total internal marks for each student. Total internal marks is simply the cumulative summation of all subject marks obtained in ass1 and ass2.
	Calculates the rank for each student based on the total internal marks.
	Sorts the elements in ascending order based on the computed rank.
	Test the function by creating a dictionary as given below
For example,
Input:	
details={20201010: {'name':'Khan','age':18,‘ass1':{'phy':88,'chem':99,'mat':99,'py':99},'ass2':{'phy':88,'chem':99,'mat':99,'py':99},'imark':0,'rank':0}, 20201011: {'name':'Sam','age':18,'ass1':{'phy':81,'chem':79,'mat':99,'py':89},'ass2':{'phy':80,'chem':89,'mat':79,'py':79},'imark':0,'rank':0},
20201012: {'name':'Ram','age':18,'ass1':{'phy':68,'chem':79,'mat':89,'py':99},'ass2':{'phy':58,'chem':69,'mat':79,'py':99},'imark':0,'rank':0}}

OUTPUT:
	[(20201012,  {'name': 'Ram',   'age': 18,    'ass1': {'phy': 98, 'chem': 99, 'mat': 99, 'py': 99},'ass2': {'phy': 98, 'chem': 99, 'mat': 99, 'py': 99},
   'imark': 790,'rank': 3}),
 (20201010, {'name': 'Khan', 'age': 18,'ass1': {'phy': 88, 'chem': 99, 'mat': 99, 'py': 99}, 'ass2': {'phy': 88, 'chem': 99, 'mat': 99, 'py': 99},
   'imark': 770, 'rank': 1}),
 (20201011,{'name': 'Sam', 'age': 18,'ass1': {'phy': 81, 'chem': 79, 'mat': 99, 'py': 89}, 'ass2': {'phy': 80, 'chem': 89, 'mat': 79, 'py': 79},
   'imark': 675, 'rank': 2})]

<hr>

3.	Write a function coprimenumber(a,b),when given a pair of numbers returns, if the pair of number are coprime or not.
Co-Prime Numbers are a set of Numbers where the Common factor among them is 1. It implies that the HCF or the Highest Common Factor should be 1 for those Numbers.
Example:
14 and 15
Factors of 14 are 1, 2, 7 and 14.
 
Factors of 15 are 1, 3, 5 and 15.
The Common factor of 14 and 15 is only 1. So, 14 and 15 are Co-Prime Numbers.

<hr>

4.	Write a menu driven program for the following :
The function calc (f, a, b) to take as input arguments a function f, operand a, operand b and applies the f on a, b as f (a, b) using lambda functions. Demonstrate using a test program for all the arithmetic operations.

<hr>

5.	Write a function paragraph_stats(paragraph) which performs on the below paragraph:
paragraph = "There is no strife, no prejudice, no national conflict in outer space as yet. Its hazards are hostile to us all. Its conquest deserves the best of all mankind, and its opportunity for peaceful cooperation many never come again. But why, some say, the moon? Why choose this as our goal? And they may well ask why climb the highest mountain? Why, 35 years ago, fly the Atlantic? Why does Rice play Texas? We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organise and measure the best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too. -- John F Kennedy"

Determines the following:
	vowels - number of vowels in the paragraph
	consonants - number of consonants in the paragraph
	words - number of words in the paragraph
	sentences - number of sentences in the paragraph
	digits - number of digits in the paragraph
	symbols - number of special symbols or characters in the paragraph
	frequency - frequency of each distinct word in the paragraph
	palindrome - number of palindrome words in the paragraph
	anagrams - number of anagrams in the paragraph (anagrams are different words formed with same alphabets)

<hr>

6.	Write a Menu driven program using list to perform Matrix Rotation such as 90, 180, 270 & 360.

<hr>

7.	Write a program for the following:

a.	Get “N” number of Bike details in nested list. (N > 5)
b.	Insert “Color” at index “3” of every list.
c.	Add “Yamaha” bike details with different color.
d.	Add 1 more new Bike details using extend( ).
e.	Sort the list based on Mileage of the bike.
f.	Print the original and sorted list.
g.	Insert “S.No” at index “0” of every list.
h.	Print the unique bike details.

<hr>

8.	Implement the concept of Supermarket Billing System using OOPs concept.

<hr>

<H1>Answer key</H1>

<table>
    <thead>
        <tr>
            <th>Q.NO.</th>
            <th>Shortname</th>
            <th>Progress</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>1</th>
            <td>Cipher Checker Function</td>
            <td>Not Started</td>
        </tr>
        <tr>
            <th>2</th>
            <td>Calculate Student Rank</td>
            <td>Done</td>
        </tr>
        <tr>
            <th>3</th>
            <td>Coprime</td>
            <td>Done</td>
        </tr>
        <tr>
            <th>4</th>
            <td>Arithmatic Operations</td>
            <td>Not Started</td>
        </tr>
        <tr>
            <th>5</th>
            <td>Paragraph Analysis Function</td>
            <td>Done</td>
        </tr>
        <tr>
            <th>6</th>
            <td>Python Matrix Rotation</td>
            <td>Done</td>
        </tr>
        <tr>
            <th>7</th>
            <td>Bike Details and Color.</td>
            <td>Not Started</td>
        </tr>
        <tr>
            <th>8</th>
            <td>Supermarket Billing System</td>
            <td>Not Started</td>
        </tr>
    </tbody>
</table>
