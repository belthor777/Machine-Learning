function [theta1] = motion_model_theta(theta, w, delta_t)
theta1 = theta + (w * delta_t);
end