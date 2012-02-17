function [p_query] = naiveBayes(l1, l2, query, k)

% Function to calculate and provide various aspects of naive bayes

% initialize returned values to be safe
p_query = 0;

% Make sure that l1, l2, and query are Cell arrays
l1 = cellstr(l1);
l2 = cellstr(l2);
query = cellstr(query);

% The first and simplest step will be calculating the probability of the Lists using Laplacian Smoothing via k
p_l1 = (length(l1) + k) / (length(l1) + length(l2) + 2);
p_l2 = (length(l2) + k) / (length(l1) + length(l2) + 2);

% Print to screen the results
fprintf('P(List_1): %f\n', p_l1);
fprintf('P(List_2): %f\n', p_l2);

% Prepare Dictionary
% First We gather our word lists for each group using the wordList Function
l1_words = wordList(l1);
l2_words = wordList(l2);
size_l1 = length(l1_words);
size_l2 = length(l2_words);

dict = union(l1_words,l2_words); % Then a union is preformed on each list to find unique words
size_dict = length(dict); % add variable for size of dictionary

% Prepare Query For Calculations
query_ind = strsplit(char(query), " "); % break up query into individual words
size_query = length(query_ind); % get size of query
pq_gl=zeros(size_query,2);

%Set probabilities for query | lists
pq_top = [p_l1;p_l2];

% Calculate Probability of words inmovi query for each list
for i = 1:size_query
	pq_gl(i,1) = (occurence(query_ind(i),l1_words) + k) / (size_l1 + size_dict);
	pq_gl(i,2) = (occurence(query_ind(i),l2_words) + k) / (size_l2 + size_dict);
	fprintf('%s | List_1 = %f\n', query_ind{i}, pq_gl (i,1));
	fprintf('%s | List_2 = %f\n', query_ind{i}, pq_gl (i,2));
	pq_top(1) = pq_top(1) * pq_gl(i,1);
	pq_top(2) = pq_top(2) * pq_gl(i,2);
end

pq_l1 = pq_top(1) / (pq_top(1) + pq_top(2));
pq_l2 = pq_top(2) / (pq_top(1) + pq_top(2));

fprintf('List_1 | %s = %f\n', query{1}, pq_l1);
fprintf('List_2 | %s = %f\n', query{1}, pq_l2);
	
end