function [x1, y1, theta1] = motion_model_update(x, y, theta, delta_t, v, w)
x1 = motion_model_x(x, theta, v, delta_t);
y1 = motion_model_y(y, theta, v, delta_t);
theta1 = motion_model_theta(theta, w, delta_t);
end