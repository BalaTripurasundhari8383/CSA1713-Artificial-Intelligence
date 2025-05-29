% Base Case: Empty list has 0 vowels
count_vowels([], 0).

% Recursive Case: If the head is a vowel, increment count
count_vowels([H|T], Count) :- 
    member(H, [a, e, i, o, u]), 
    count_vowels(T, C1), 
    Count is C1 + 1.

% Recursive Case: If the head is not a vowel, continue with the rest
count_vowels([_|T], Count) :- 
    count_vowels(T, Count).
