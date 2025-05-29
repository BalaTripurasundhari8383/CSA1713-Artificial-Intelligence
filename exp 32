% Base Case: Pattern matches the head of the list
match([Pattern|_], Pattern).

% Recursive Case: Check the rest of the list
match([_|Tail], Pattern) :- match(Tail, Pattern).
