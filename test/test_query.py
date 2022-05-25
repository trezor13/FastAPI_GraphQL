def test_create_product(client):
    query = """
    mutation {
        createProduct(productDetails: {
            id: 1
            name: "Dodo",
            price: 50,
            category: 1
        })
        {
            id
        }
    }
    """

    result = client.execute(query)
    assert result['data']['createProduct']['id'] == 1
    assert result['data']['createProduct']['name'] == "Test Product"


def test_get_product_list(client, product):
    query = """
    query {
        listProducts {
            name
            price
            category
        }
    }
    """

    result = client.execute(query)
    assert type(result['data']['listProduct']) == list


def test_get_single_product(client, product):
    query = """
    query {
        getSingleProduct(productId: %s){
            name
        }
    }
    """ % product.id
    result = client.execute(query)

    assert result['data']['getSingleProduct'] is not None
    assert result['data']['getSingleProduct']['name'] == product.name
