import pytest

from candidates import Candidate

@pytest.mark.parametrize('cid', range(82,100))
def test_candidate_status_code_get(cid):
    assert Candidate().get(cid).status_code == 200
    
def test_candidate_status_code_post():
    assert Candidate().post('Marina', 'VP Director Senior Automation QA Architect').status_code == 201
    
    
    
    