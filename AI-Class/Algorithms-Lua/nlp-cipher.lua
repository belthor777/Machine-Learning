
-- input sentence (rotation cipher)
sentence = 'Esp qtcde nzyqpcpynp zy esp ezatn zq Lcetqtntlw Tyepwwtrpynp hld spwo le Olcexzfes Nzwwprp ty estd jplc'
sentence = sentence:lower()

-- English letter frequencies from
-- http://en.wikipedia.org/wiki/Letter_frequency
freq = {
  a =  0.08167,
  b =  0.01492,
  c =  0.02782,
  d =  0.04253,
  e =  0.12702,
  f =  0.02228,
  g =  0.02015,
  h =  0.06094,
  i =  0.06966,
  j =  0.00153,
  k =  0.00772,
  l =  0.04025,
  m =  0.02406,
  n =  0.06749,
  o =  0.07507,
  p =  0.01929,
  q =  0.00095,
  r =  0.05987,
  s =  0.06327,
  t =  0.09056,
  u =  0.02758,
  v =  0.00978,
  w =  0.02360,
  x =  0.00150,
  y =  0.01974,
  z =  0.00074,
}

-- rotates the non-space letters of a sentence by n letters
function rotate(s, n)
  local r = ''
  local abyte, spbyte = string.byte('a'), string.byte(' ')
  for i = 1, #s do
    local b = s:byte(i)
    if b ~= spbyte then
      b = abyte + (((b - abyte) + n) % 26)
    end
    r = r .. string.char(b)
  end
  return r
end

-- returns the non-space letter frequencies (e.g. freq['a'] = 0.0097)
function letterfreq(s)
  local f = {}
  for i = 1, #s do
    local l = s:sub(i, i)
    if l ~= ' ' then
      f[l] = f[l] and f[l] + 1 or 1
    end
  end
  for l, count in pairs(f) do
  	f[l] = count / #s
  end
  return f
end

-- scores a candidate solution based on letter frequencies
function score(solution)
  local diff = 0
  for l, f in pairs(freq) do
  	if solution.letterfreq[l] then
      diff = diff + math.abs(solution.letterfreq[l] - f)
    end
  end
  solution.score = 1 - diff
end

-- solves the cipher
solution = {}
bestn, bestscore = 0, 0
for n = 1, 25 do
  solution[n] = { n = n }
  solution[n].sentence = rotate(sentence, n)
  solution[n].letterfreq = letterfreq(solution[n].sentence)
  score(solution[n])
  print('candidate rotation: ' .. n)
  print(solution[n].sentence)
  print('score: ' .. solution[n].score)
  if bestscore < solution[n].score then
  	print('BEST!!!')
    bestn, bestscore = n, solution[n].score
  end
  print()
end
print('best rotation: ' .. bestn)
print(solution[bestn].sentence)
print('score: ' .. bestscore)
