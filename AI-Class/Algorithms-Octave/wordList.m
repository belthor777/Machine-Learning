function l = wordList(list)
% This function will receive a cell string with multiple words in each row
% It will return a cell string of each word from the list on its own row

% iterate through second list and add unique words to dictionary
n = length(list);
l={};
count = 0;
for i = 1:n
	temp=strsplit(char(list(i)), " ");
	
	m = length(temp);
	
	for j = 1:m
		count = count + 1;
		l(count) = temp(j);
	end
end

end