function Iprime = convolve(I, g)
	[m n] = size(I);
	I = [zeros(m, 1) I zeros(m, 1)];
	Iprime = zeros(m,n);

	for y = 1:n
		for x = 1:m
			for u = 1:length(g)
				Iprime(y, x) += I(y, x - 1 + u) * g(u);
			end
		end
	end
end