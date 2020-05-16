def matchingWords(sentence1,sentence2):
    words1=sentence1.strip().split(" ")
    words2=sentence2.strip().split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                score+=1
    return score
if __name__ == "__main__":
    sentences=["pyton.","hello i am python.","python is based on oops concept.","syntax for python is easy.","python is not a snake python."]
    query=input("Please enter the word to found.")
    scores=[matchingWords(query,sentence) for sentence in sentences]
    sortedsentences=[sentscore for sentscore in sorted(zip(scores,sentences),reverse=True)if sentscore[0]!=0]
    print(f"{len(sortedsentences)} results found!")
    for score,item in sortedsentences:
        print(rf"{item}:with a score of {score}.")