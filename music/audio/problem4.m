%% Problem 4
% Calculate the velocities and heights of the joints
clear m g theta1(t) t1_dot t1 I L;
syms m M g theta1(t) t1_dot x_dot t1 I L x1(t) x x2 x3 x4 T;

%%
% Calculate the kinetic and potential energies
[vel,height] = calcVel;

K = 1/2 * m * (vel.'*vel) + 1/2 * I * diff(theta1(t),t)^2 + 1/2 * M * diff(x1,t)^2;
P = m * g * height;


%%
% Calculate the Lagrangian equation.
Lagrangian = K + P;

%%
% Calculate the first half of the torque
Lag_sub1 = subs(Lagrangian,[diff(theta1(t),t),diff(x1(t),t)],[t1_dot,x_dot])
firstHalf1 = jacobian(Lag_sub1,[t1_dot;x_dot])
Lag_sub1 = subs(firstHalf1,[t1_dot,x_dot],[diff(theta1(t),t),diff(x1(t),t)])
firstHalf1 = diff(Lag_sub1,t)


%%
% Calculate the second half of the torque
Lag_sub1 = subs(Lagrangian,[theta1(t),x1(t)],[t1,x])
second_half1 = jacobian(Lag_sub1,[t1,x])
second_half1 = subs(second_half1,[t1,x],[theta1(t),x1(t)])


%%
% Finally, subtract the second half of the calcualtion from the first half
% to get the torque for the three joints.
torques = firstHalf1 - second_half1;
torques = simplify(torques);

%%
% Put Torques into appropriate format
torques = collect(torques,[diff(theta1(t),t,t),diff(theta1(t),t),theta1(t)])

%%
% Derive State Space model: d_x = f(x,u)
syms dd_t dd_x
temp = subs(torques,[diff(theta1(t),t,t),diff(theta1(t),t),theta1(t),diff(x1,t,t),diff(x1,t)],[dd_t x4 x3 dd_x x2]);

% x = [q1;q2;d_q1;d_q2]
outputX(1) = x2;
temp2 = solve(temp == T,dd_x);
outputX(2) = temp2.dd_x;
outputX(3) = x4;
temp2 = solve(temp == T,dd_t);
outputX(4) = temp2.dd_t;
outputX = outputX.'

%%
% The derivative of x is equal to d_x (dx/dt = d_x) which is the
% state-space model