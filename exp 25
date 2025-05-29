% Possible actions the monkey can take

% Grasping the banana (only possible if on the box and at the middle)
move(state(middle, on_box, middle, has_not), grasp, state(middle, on_box, middle, has)).

% Climbing onto the box (only if at the same position as the box)
move(state(P, on_floor, P, H), climb, state(P, on_box, P, H)).

% Pushing the box to a new position (monkey and box must be at same initial position)
move(state(P1, on_floor, P1, H), push(P1, P2), state(P2, on_floor, P2, H)).

% Walking to a new position (only monkey moves, box stays in place)
move(state(P1, on_floor, B, H), walk(P1, P2), state(P2, on_floor, B, H)).

% Goal state: Monkey has the banana
can_get(state(_, _, _, has)).

% Recursive rule: Try different moves to reach the goal
can_get(State1) :- 
    move(State1, Action, State2),
    write('Monkey performs: '), write(Action), nl, % Debugging step
    can_get(State2).
