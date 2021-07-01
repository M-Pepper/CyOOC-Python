#!/usr/bin/env python3

def vsm(txt,order=2):
    ngrams = {}
    for i in range(0,len(txt)-order+1):
        ngram = txt[i:i+order]
        if ngram not in ngrams:
            ngrams[ngram] = {}
        try:
            follows = txt[i+order]
        except:
            follows = ' '
        ngrams[ngram][follows] = 1 + ngrams[ngram].get(follows,0)
    return ngrams

def similarity(ng0,ng1):
    def vsm_norm(ngrams):
        total = 0
        for y in ngrams.values():
            total += sum([x*x for x in y.values()])
        return total**0.5

    dotproduct = 0
    for k in ng0:
        if k in ng1:
            a = ng0[k]
            b = ng1[k]
            for x in a:
                if x in b:
                    dotproduct += a[x] * b[x]
    return float(dotproduct) / (vsm_norm(ng0) * vsm_norm(ng1))


