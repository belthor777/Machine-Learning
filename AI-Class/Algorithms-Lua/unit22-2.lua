-- grammar
S,NP,VP,N,D,V = 'S','NP','VP','N','D','V'
G = {
  S  = { {NP,VP} },
  NP = { N, {D,N}, {N,N}, {N,N,N} },
  VP = { {V,NP}, V, {V,NP,NP} },
  N  = { 'interest', 'Fed', 'rates', 'raises' },
  V  = { 'interest', 'rates', 'raises' },
  D  = { 'the', 'a' }
}

-- sentences to match
sentence = {
  { 'the', 'Fed', 'raises', 'interest', 'rates' },
  { 'the', 'Fed', 'raises', 'raises' },
  { 'raises', 'raises', 'interest', 'raises' },
}
-- count of matches
count = {}

-- naive table copy
function tcopy(t)
  local tc = {}
  for i,v in ipairs(t) do tc[i] = v end
  return tc
end

-- naive table equality
function tequals(t1, t2)
  if #t1 ~= #t2 then return false end
  for i = 1, #t1 do
    if t1[i] ~= t2[i] then return false end
  end
  return true
end

-- check for matches against target sentences
function check(t)
  for i, s in ipairs(sentence) do
    if tequals(s, t) then
      count[i] = count[i] and count[i] + 1 or 1
    end
  end
end

-- recursively enumerate sentences from grammar
function generate(t)
  local expanded = false
  for i, sym in ipairs(t) do
    if G[sym] then
      expanded = true
      for j, prod in ipairs(G[sym]) do
        if type(prod) ~= 'table' then prod = {prod} end
        local tc = tcopy(t)
        table.remove(tc, i)
        for k = #prod, 1, -1 do
          table.insert(tc, i, prod[k])
        end
        generate(tc)
      end
      break
    end
  end
  if not expanded then
    print(table.concat(t, ' '))
    check(t)
  end
end

-- generate all possible sentences
generate({S})

-- print resulting counts
for i = 1, #count do
  print(count[i], table.concat(sentence[i], ' '))
end
