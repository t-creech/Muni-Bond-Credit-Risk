import hydra
from omegaconf import DictConfig
from pathlib import Path
from credit_risk_ml.data.make_dataset import clean_emma_filings


@hydra.main(version_base=None, config_path="../config", config_name="default")
def main(cfg: DictConfig) -> None:
    raw = Path(cfg.paths.raw)
    interim = Path(cfg.paths.interim)
    clean_emma_filings(raw, interim)


if __name__ == "__main__":
    main()
