#Author:Caner Yildirim
#caneryild163@gmail.com
#main
sizeofallAminoAcids=23
#Default is the same for l.c.s without this matrix applied to  similarityOfProteins function
aminoAcidSimilaritiesDefault= [[0 for size1 in range(sizeofallAminoAcids)] for size2 in range(sizeofallAminoAcids)] 
for index1 in range(0,sizeofallAminoAcids):
  for index2 in range(0,sizeofallAminoAcids):
    if index1==index2:
      aminoAcidSimilaritiesDefault[index1][index2]=1
      
#methods
def similarityOfProteins(protein1,protein2,aminoAcidSimilarities=aminoAcidSimilaritiesDefault):
  lcs=largestCommonSubsequence(protein1,protein2)
        ' find the first of largest common subseqence in each of them
        'and compare them from the first index through last one 
        'and compare them from the first index of L.C.S. to the ends.
        'the reverse for 2 two steps are repeated from end to start and from end of lcs.'s to start.
        'Total of m*n*2 comparisions are made.
    #
    similarities=0# will be similar to cosine distance similarity or jaccardt distance similarity 
  return similarities
