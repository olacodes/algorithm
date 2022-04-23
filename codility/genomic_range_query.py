def solution(S: str, P: list, Q: list) -> list:

  dna = {'A': 1, 'C': 2, 'G': 3, 'T': 4 }

  zipped = list(zip(P, Q))
  result = []
  for i in range(len(zipped)):
    min_num = 100000;
    first_elem = zipped[i][0]
    second_elem = zipped[i][1]+1

    for j in range(first_elem, second_elem):
      current_dna = S[j]
      current_dna_value = dna[current_dna]
      if current_dna_value < min_num:
        min_num = current_dna_value
    result.append(min_num)
    min_num = 100000;

  return result


p = [2, 5, 0]
q = [4, 5, 6]
s = 'CAGCCTA'
print(solution(s, p, q)) # [2, 4, 1]

