import requests

URL = 'http://localhost:5001/graphql'

def test_get_electronics():
    query = '''
    query {
      electronics {
        id
        nombre
        precio
        stock
        disponible
      }
    }
    '''
    response = requests.post(URL, json={'query': query})
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert 'electronics' in data['data']
    assert isinstance(data['data']['electronics'], list)
    assert len(data['data']['electronics']) > 0

def test_update_stock_success():
    mutation = '''
    mutation {
      updateStock(id: "1", amount: 1) {
        success
        message
        electronic {
          id
          stock
          disponible
        }
      }
    }
    '''
    response = requests.post(URL, json={'query': mutation})
    assert response.status_code == 200
    data = response.json()
    update_result = data.get('data', {}).get('updateStock')
    assert update_result is not None
    assert update_result['success'] == True
    assert update_result['electronic']['id'] == "1"
    assert isinstance(update_result['electronic']['stock'], int)

def test_update_stock_fail():
    mutation = '''
    mutation {
      updateStock(id: "9999", amount: 1) {
        success
        message
        electronic {
          id
          stock
          disponible
        }
      }
    }
    '''
    response = requests.post(URL, json={'query': mutation})
    assert response.status_code == 200
    data = response.json()
    update_result = data.get('data', {}).get('updateStock')
    assert update_result is not None
    assert update_result['success'] == False
    assert update_result['message'] == "Producto no encontrado"
    assert update_result['electronic'] is None

if __name__ == '__main__':
    test_get_electronics()
    test_update_stock_success()
    test_update_stock_fail()
    print("All tests passed!")
