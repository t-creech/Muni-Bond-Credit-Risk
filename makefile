.PHONY: build_features train test lint

build_features:
	python -m credit_risk_ml.pipeline.01_build_features

train:
	python -m credit_risk_ml.pipeline.02_train

test:
	pytest -q

lint:
	ruff src tests && black --check src tests