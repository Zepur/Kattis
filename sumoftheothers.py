import sys

for s in sys.stdin:
    nums = [int(i) for i in s.split()]
    negatives = [n for n in nums if n < 0]
    negatives.sort()
    positives = [p for p in nums if p > 0]
    positives.sort()
    _nsum = 0
    for n in negatives:
        _nsum += n
    _psum = 0
    for p in positives:
        _psum += p
    diff = _psum + _nsum

    if int(diff / 2) in positives:
        print(str(int(diff / 2)))
    elif int(diff / 2) in negatives:
        print(str(int(diff / 2)))
else:
    quit()
