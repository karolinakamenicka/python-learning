def word_search(doc_list, keyword):
    #print(list(doc_list))
    i = []
    k=0
    for doc in doc_list:
        doc = doc.lower()
        print(doc)
        if (keyword in doc) != False:
            doc2 = doc.split()
            for d in doc2:
                #print(d)
                if d == keyword or d== (keyword + '.') or d== (keyword + ','):
                    i.append(k)
                    break
        k=k+1
    return i

doc_list=['The Learn Python Challenge Casino has a big casino full of casino games', 'They bought a car', 'Casinoville']
print(word_search(doc_list,'casino'))

def multi_word_search(doc_list, keywords):
    iter = []
    for key in keywords:
        iter.append((key,word_search(doc_list, key)))

    return dict(list(iter))

doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
print(multi_word_search(doc_list, keywords))
