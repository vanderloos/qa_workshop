import pytest
from random import randint

@pytest.fixture(autouse=True, scope='class')
def my_preconditions():
    print('Conduct my preparations.')
    file=open(r'data//text_file.json', 'a')
    file.writelines(f'Line {str(randint(1,1000))}\n')
    print('End of preparations')
	
    yield
	
    file = open(r'data//text_file.json', 'w')
    file.writelines('')
    file.close()
    
