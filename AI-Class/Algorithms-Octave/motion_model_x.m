function [x1] = motion_model_x(x, theta, v, delta_t)
x1 = x + (v*delta_t*cos(theta));
end

