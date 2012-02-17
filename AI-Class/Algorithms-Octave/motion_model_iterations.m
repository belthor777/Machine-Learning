function [x, y, theta] = motion_model_iterations(x, y, theta, start_t, end_t, delta_t, v, w)

t = start_t;

while (t != end_t)
[x, y, theta] = motion_model_update(x, y, theta, delta_t, v, w);
t = t + delta_t;
endwhile