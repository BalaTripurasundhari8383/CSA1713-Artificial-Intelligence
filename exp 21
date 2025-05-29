% hanoi(N, Source, Target, Auxiliary)
% N: number of disks
% Source: initial peg
% Target: destination peg
% Auxiliary: helper peg

hanoi(1, Source, Target, _) :-
    format('Move disk from ~w to ~w~n', [Source, Target]).

hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Target),
    hanoi(1, Source, Target, _),
    hanoi(M, Auxiliary, Target, Source).
