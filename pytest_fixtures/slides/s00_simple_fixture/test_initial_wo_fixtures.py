
def test_42_int():
    """
    The test reads a text file with some integer numbers at the line ends, and asserts there is 42 among them.
    """
    ints = []
    with open(r'data//text_file.txt', 'r') as file:
        for line in file:
            try:
                num = int(line.split()[-1])
                ints.append(num)
            except ValueError:
                pass
    assert 42 in ints
