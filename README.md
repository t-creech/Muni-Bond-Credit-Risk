# Muni‑Bond‑Credit‑Risk  

This project investigates machine‑learning techniques for modeling credit spreads in municipal (muni) bonds.  Understanding credit spreads helps investors assess default risk and relative value across issuers and maturities.  The project explores data acquisition, feature engineering, model training and evaluation.  

## Project goals  

- Collect and clean municipal bond data, including yields, credit ratings, and macroeconomic variables.  
- Build models to estimate credit spreads using machine learning algorithms (e.g., regression, tree‑based models, neural networks).  
- Evaluate model performance and interpret important drivers of credit risk.  
- Provide reproducible workflows through Jupyter notebooks and scripts.  

## Repository structure  

- `notebooks/` – exploratory analysis and model development in Jupyter Notebook format.  
- `src/credit_risk_ml/` – Python modules for data processing, feature engineering, modelling and evaluation.  
- `outputs/<date>/` – generated outputs such as figures and result tables.  
- `environment.yml` or `requirements.txt` – dependency lists.  
- `makefile` / `setup.py` – build and installation scripts.  

## Getting started  

1. Clone the repository and navigate into it:  
   ```bash  
   git clone https://github.com/t-creech/Muni-Bond-Credit-Risk.git  
   cd Muni-Bond-Credit-Risk  
   ```  

2. Create a conda environment:  
   ```bash  
   conda env create -f environment.yml  
   conda activate muni-bond-credit-risk  
   ```  
   or install dependencies with pip:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Explore the notebooks in the `notebooks/` directory or run scripts in `src/credit_risk_ml` to reproduce results.  

## Contributing  

This is a collaborative research project.  Contributions to data sources, feature ideas, or model improvements are welcome.  Please fork the repository and open a pull request.  

## License  

This project is released under the MIT License.
