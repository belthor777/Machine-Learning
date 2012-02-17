function o = occurence(word, list)
% This function receives a list of words and a query word
% It then returns how many times the query word appears in the list

	o=sum(strcmp(word,list));

end