import pytest
from app.schemas.category import Category, CategoryOutput
from app.use_cases.category import CategoryUseCases

def test_category_schema():
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    assert category.model_dump() == {
        'name': 'Roupa',
        'slug': 'roupa'
    }


def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='roupa de cama'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='cão'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='Roupa'
        )

def test_list_categories(db_session, categories_on_db):
    uc = CategoryUseCases(db_session=db_session)

    categories = uc.list_categories()

    assert len(categories) == 4
    assert type(categories[0]) == CategoryOutput
    assert categories[0].id == categories_on_db[0].id
    assert categories[0].name == categories_on_db[0].name
    assert categories[0].slug == categories_on_db[0].slug