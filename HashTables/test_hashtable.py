from hashtable import HashTable, BLANK
import pytest

def test_should_always_pass():
    assert HashTable(capacity = 100) is not None
    
def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100
    
def test_should_create_empty_value_slots():
    # assert HashTable(capacity=3).values == [None, None, None]
    #Given
    excepted_values = [BLANK, BLANK, BLANK]
    hash_table = HashTable(capacity=3)
    
    #when
    actual_values = hash_table.values
    
    #then
    assert actual_values == excepted_values
    
def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table['hola'] = 'Hello'
    hash_table[98.6] = 37
    hash_table[False] = True
    
    assert 'Hello' in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
    
    assert len(hash_table) == 100
    
@pytest.mark.skip
def test_should_not_shrink_removing_elements():
    pass

def test_should_not_contain_None_values():
    assert None not in HashTable(capacity=100).values
    
def test_should_insert_None_values():
    hash_table = HashTable(capacity=100)
    hash_table['key'] = None
    assert None in hash_table.values
    
@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data['hello'] = "hello"
    sample_data[3.15] = 315
    sample_data[False] = True
    return sample_data

def test_should_find_value_by_key(hash_table):
    assert hash_table['hello'] == "hello"
    assert hash_table[3.15] == 315
    assert hash_table[False] == True
    
# def test_should_raise_error_on_missing_keys():
#     hash_table = HashTable(capacity=100)
#     with pytest.raises(KeyError) as exception_info:
#         hash_table["missing_key"]
#     assert exception_info.value.args[0] == "missing_key"
    
def test_should_find_key(hash_table):
    assert 'hello' in hash_table

def test_should_not_find_key(hash_table):
    assert 'missing_key' not in hash_table
    
def test_should_get_value(hash_table):
    assert hash_table.get('hello') == 'hello'
    
def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get('missing_key') is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get('missing_key', 'default') == 'default'

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hello", 'default') == 'hello'
    
def test_should_delete_key_value(hash_table):
    assert 'hello' in hash_table
    assert 'hello' in hash_table
    assert len(hash_table) == 100
    
    del hash_table['hello']
    assert 'hello' not in hash_table
    assert 'hello' not in hash_table
    assert len(hash_table) == 100

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"
    
def test_should_update_value(hash_table):
    assert hash_table["hello"] == "hello"

    hash_table["hello"] = "hallo"

    assert hash_table["hello"] == "hallo"
    assert hash_table[3.15] == 315
    assert hash_table[False] is True
    assert len(hash_table) == 100