% Facts: Defining relationships
parent(john, mary).
parent(mary, alice).
parent(alice, sophie).

% Rule: Defining ancestor relationship using backward chaining
ancestor(X, Y) :- parent(X, Y).                % Direct parent
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y). % Recursive rule (grandparent, etc.)
