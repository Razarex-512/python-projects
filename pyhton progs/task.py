def happynum(n):
    past = set()			
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True
print([x for x in range(500) if happynum(x)][:30])
