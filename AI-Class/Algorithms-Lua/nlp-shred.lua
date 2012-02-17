
-- raw data is 19 strips of 8 rows of 2 characters
raw = [[
|de|  | f|Cl|nf|ed|au| i|ti|  |ma|ha|or|nn|ou| S|on|nd|on|
|ry|  |is|th|is| b|eo|as|  |  |f |wh| o|ic| t|, |  |he|h |
|ab|  |la|pr|od|ge|ob| m|an|  |s |is|el|ti|ng|il|d |ua|c |
|he|  |ea|of|ho| m| t|et|ha|  | t|od|ds|e |ki| c|t |ng|br|
|wo|m,|to|yo|hi|ve|u | t|ob|  |pr|d |s |us| s|ul|le|ol|e |
| t|ca| t|wi| M|d |th|"A|ma|l |he| p|at|ap|it|he|ti|le|er|
|ry|d |un|Th|" |io|eo|n,|is|  |bl|f |pu|Co|ic| o|he|at|mm|
|hi|  |  |in|  |  | t|  |  |  |  |ye|  |ar|  |s |  |  |. |
]]

-- processed data such that strip[4][1] = 'Cl'
strip = {}
for line in raw:gmatch('[^\r\n]+') do
  local i = 1
  for pair in line:gmatch('[^|]+') do
  	strip[i] = strip[i] or {}
  	strip[i][#strip[i]+1] = pair
  	i = i + 1
  end
end

-- digraph frequencies from
-- http://facultyfp.salisbury.edu/despickler/personal/M490/frequency_in_english.pdf
digraph = {
  ['th'] = 1.52,
  ['he'] = 1.28,
  ['in'] = 0.94,
  ['er'] = 0.94,
  ['an'] = 0.82,
  ['re'] = 0.68,
  ['nd'] = 0.63,
  ['at'] = 0.59,
  ['on'] = 0.57,
  ['nt'] = 0.56,
  ['ha'] = 0.56,
  ['es'] = 0.56,
  ['st'] = 0.55,
  ['en'] = 0.55,
  ['ed'] = 0.53,
  ['to'] = 0.52,
  ['it'] = 0.50,
  ['ou'] = 0.50,
  ['ea'] = 0.47,
  ['hi'] = 0.46,
  ['is'] = 0.46,
  ['or'] = 0.43,
  ['ti'] = 0.34,
  ['as'] = 0.33,
  ['te'] = 0.27,
  ['et'] = 0.19,
  -- starting letters (estimated)
  [' t'] = 0.19,
  [' o'] = 0.19,
  [' a'] = 0.19,
  [' w'] = 0.19,
  [' b'] = 0.19,
  [' c'] = 0.19,
  [' d'] = 0.19,
  [' s'] = 0.19,
  [' f'] = 0.19,
  [' m'] = 0.19,
  -- ending letters (estimated)
  ['e '] = 0.19,
  ['t '] = 0.19,
  ['d '] = 0.19,
  ['s '] = 0.19,
}
sum = 0
for i, f in pairs(digraph) do
  sum = sum + f
end
for i, f in pairs(digraph) do
  digraph[i] = f / sum
end

-- calculate score of joining strip i and strip j
-- based on digraph frequencies
function calcscore(stripi, stripj)
  local scoreij, scoreji = 0, 0
  for r, ri in ipairs(stripi) do
  	local rj = stripj[r]
  	local dij = ri:sub(#ri):lower() .. rj:sub(1, 1):lower()
  	local dji = rj:sub(#rj):lower() .. ri:sub(1, 1):lower()
  	if digraph[dij] then scoreij = scoreij + digraph[dij] end
  	if digraph[dji] then scoreji = scoreji + digraph[dji] end
  end
  return scoreij, scoreji
end

-- build a score table such that score[i][j] is the score
-- for strip[i] joined to strip[j]
score = {}
for i, stripi in ipairs(strip) do
  score[i] = {}
  for j, stripj in ipairs(strip) do
  	score[j] = score[j] or {}
    if i == j then
      score[i][j] = -1
    else
      score[i][j], score[j][i] = calcscore(stripi, stripj)
    end
  end
end

-- finds the best score in the table
function bestscore(t)
  local bestscore, besti, bestj = -1, -1, -1
  for i = 1, #t do
  	for j = 1, #t do
  	  if bestscore < t[i][j] then
  	  	bestscore, besti, bestj = t[i][j], i, j
  	  end
    end
  end
  return bestscore, besti, bestj
end

-- joins the strips using a greedy algorithm
join = {}
while true do
  local s, i, j = bestscore(score)
  if s == -1 then break end
  --for i = 1, #score do score[i][j] = -1 end
  --for j = 1, #score do score[i][j] = -1 end
  score[i][j] = -1
  join[#join+1] = { i, j }
  print('join:', i, j)
end

-- adds a join into a solution
function addtosolution(solution, i, j)
  local ifound, jfound = false, false
  for f, frag in pairs(solution) do
  	for _, n in ipairs(frag) do
  	  if n == i then ifound = true end
  	  if n == j then jfound = true end
  	end
  end
  if ifound and jfound then
  	return
  end
  for f, frag in pairs(solution) do
  	if frag[#frag] == i then
  	  table.insert(frag, j)
  	  print('expanded after', table.concat(frag, '.'))
  	  for of, ofrag in pairs(solution) do
  	  	if frag[#frag] == ofrag[1] then
  	      print('merging', table.concat(frag, '.'), table.concat(ofrag, '.'))
  	      for o = 2, #ofrag do
  	      	table.insert(frag, ofrag[o])
  	      end
  	      solution[of] = nil
  	  	  break
  	  	end
  	  end
  	  return
  	elseif frag[1] == j then
  	  table.insert(frag, 1, i)
  	  print('expanded before', table.concat(frag, '.'))
  	  for of, ofrag in pairs(solution) do
  	  	if ofrag[#ofrag] == frag[1] then
  	      print('merging', table.concat(ofrag, '.'), table.concat(frag, '.'))
  	      for o = #ofrag - 1, 1, -1 do
  	      	table.insert(frag, 1, ofrag[o])
  	      end
  	      solution[of] = nil
  	  	  break
  	  	end
  	  end
  	  return
  	end
  end
  if not ifound and not jfound then
    print('new frag', i .. '.' .. j)
    solution[#solution+1] = { i, j }
  end
end

solution = {}
for j, join in ipairs(join) do
  addtosolution(solution, join[1], join[2])
end
for f, frag in pairs(solution) do
	print('solution:', table.concat(frag, ' '))
end

for r = 1, #strip[1] do
  for f, frag in pairs(solution) do
  	for _, n in ipairs(frag) do
      io.write(strip[n][r])
    end
  end
  print()
end
