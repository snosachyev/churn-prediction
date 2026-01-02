from churn import (
    build_features,
    train,
    create_model,
)

def test_public_api_contract():
    assert callable(build_features)
    assert callable(train)
    assert callable(create_model)
