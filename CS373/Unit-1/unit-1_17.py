# Uniform-Probability-Quiz 
# Robot Localization

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z)
	q=[]
	n=len(p)
	for i in range(n):
		hit = Z == world[i])
		q.append(p[i] * (hit * pHit + (1-hit) * pMiss) )
	return q

print sense(p, Z)


