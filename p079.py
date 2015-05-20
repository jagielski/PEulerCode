def iskeylog(passcode, a):
    if len(a) == 0:
        return True
    for i in range(len(passcode)):
        if passcode[i] == a[0]:
            return iskeylog(passcode[i+1:],a[1:])
    return False

possibles = {}