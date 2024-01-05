import pytest
from app.schemas.product import Product


def test_product_schema():
  product = Product(
    name='Camisa Mike',
    slug='camisa-mike',
    price=10.0,
    stock=10,
  )

  assert product.model_dump() == {
    "name":'Camisa Mike',
    "slug":'camisa-mike',
    "price":10.0,
    "stock":10,
  }

def test_product_schema_invalid_slug():
  with pytest.raises(ValueError):
    product = Product(
      name='Camisa Mike',
      slug='camisa mike',
      price=10.0,
      stock=10,
    )

  with pytest.raises(ValueError):
    product = Product(
      name='Camisa Mike',
      slug='cão',
      price=10.0,
      stock=10,
    )

  with pytest.raises(ValueError):
    product = Product(
      name='Camisa Mike',
      slug='Camisa-mike',
      price=10.0,
      stock=10,
    )

def test_product_schema_invalid_price():
  with pytest.raises(ValueError):
    product = Product(
      name='Camisa Mike',
      slug='Camisa-mike',
      price=-10.0,
      stock=10,
    )