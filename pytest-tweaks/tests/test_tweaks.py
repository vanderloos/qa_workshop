import pytest

from selenium import webdriver

moon_phase = 'bad'

@pytest.fixture(scope='session')
def driver_session():
	wd = webdriver.Chrome(r'c:\Users\Admin\chromedriver.exe')
	yield wd
	wd.quit()

@pytest.fixture(scope='function')
def driver(driver_session):
	driver_session.get('http://kyivtesters.org/')
	yield driver_session
	driver_session.get('http://wukipedia.org')


@pytest.mark.parametrize(('my_lucky_number', 'num'), [[2,5], [5, 17], [42, 42]])
class TestClassParametrized:
		
	@pytest.mark.bad_test
	@pytest.mark.good_test
	def test_pass(self, my_lucky_number, num):
		print('OLOLOLO')
		assert my_lucky_number == num
		

class TestWorkshop:
	@pytest.mark.bad_test
	def test_pass0(self):
		assert 2 == 2
	
	@pytest.mark.skipif(moon_phase == 'bad', reason='bad moon phase!')
	def test_fail(self):
		print('OLOLOLO')
		assert 1 == 2

	def test_kyivtesters(self, driver):
		driver.find_element_by_css_selector('input.gsc-input1111111')		

	@pytest.mark.selenium	
	def test_kyivtesters_search(self, driver):
		driver.find_element_by_css_selector('input.gsc-input')	

	@pytest.mark.selenium
	def test_kyivtesters_search_input(self, driver):
		search = driver.find_element_by_css_selector('input.gsc-input')	
		search.send_keys('data')
		driver.find_element_by_css_selector('input.gsc-search-button').click()
		
	@pytest.mark.good_test	
	def test_pass1(self):
		assert 2 == 2