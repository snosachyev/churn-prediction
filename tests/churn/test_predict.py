from churn import build_features


def test_model_predict(trained_model, sample_df):
    X = build_features(sample_df)
    preds = trained_model.predict_proba(X)
    assert len(preds) == len(X)
