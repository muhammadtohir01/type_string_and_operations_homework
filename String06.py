def main(s,n):
    """
    s string is given. repeat it n times and return the resulting string.
    Args:
        s: str
        n: int
    Returns:
        str: return answer.
    """
    answer=str(s)*int(n)
    return str(answer)
print(main(str('salom'),int(4)))