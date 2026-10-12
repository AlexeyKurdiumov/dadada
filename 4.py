def convert_string(s):
    if len(s) < 4:
        if s.isupper():
            return s.upper()
        else:
            return s
    else:
        first_four = s[:4]
        upper_count = sum(1 for char in first_four if char.isupper())
        if upper_count >= 3:
            return s.upper()
        else:
            return s
print(convert_string("PYTHon3"))
