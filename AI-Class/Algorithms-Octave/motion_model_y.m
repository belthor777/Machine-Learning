function [y1] = motion_model_y(y, theta, v, delta_t)
y1 = y + (v*delta_t*sin(theta));
end
