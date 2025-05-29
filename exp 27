% Define edges with costs
edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 8).
edge(c, e, 10).
edge(d, f, 6).
edge(e, f, 3).

% Best First Search
best_first_search(Start, Goal, Path) :-
    best_first([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

best_first([[Goal|Path]|_], Goal, [Goal|Path]).
best_first([[Node|Path]|Rest], Goal, FinalPath) :-
    findall([Next,Node|Path], (edge(Node, Next, _), \+ member(Next, [Node|Path])), NextPaths),
    append(Rest, NextPaths, NewPaths),
    sort(2, @=<, NewPaths, SortedPaths),
    best_first(SortedPaths, Goal, FinalPath).

% Query Example:
% ?- best_first_search(a, f, Path).
