# assinment-1

# Insurance Claims Management Tool

## Setup
```bash
python -m venv venv
venv\Scripts\activate #Windows 
source venv/bin/activate  # Linux/macOS
pip install fastapi uvicorn
```
## install dependencies:
pip install fastapi uvicorn

## Run
```bash
uvicorn app.main:app --reload
```
## open browser 
http://127.0.0.1:8000/docs


## API Endpoints
- POST /add_policyholder
- POST /add_claim
