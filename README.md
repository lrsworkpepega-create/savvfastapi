# savvfastapi
FastAPI service for IHS server integration

## Requirements
- Python 3.10+

## Setup (Windows PowerShell)
```powershell
# (optional) create and activate venv
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt
```

## Run
```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Test Endpoints

### 1) Прибытие паллеты на ID точку
- POST `/api/setpallet`

PowerShell example (Invoke-RestMethod):
```powershell
$body = @{ SSCC = "148102689000000010"; IDPoint = "ID1"; Message = "PalletOnID"; Weight = 123.45 } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/setpallet" -ContentType "application/json" -Body $body
```
$body = @{ SSCC = "148102689000000010"; IDPoint = "ID1"; Message = "PalletOnID"; Weight = 123.45 } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "https://savvfastapi.vercel.app//api/setpallet" -ContentType "application/json" -Body $body

Expected response:
```json
{ "SSCC": "148102689000000010", "Status": "Ok" }
```

### 2) Получение результатов исследования аномалий
- POST `/api/getcamerares`

PowerShell example (Invoke-RestMethod):
```powershell
$body = @{ SSCC = "148102689000000010" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/getcamerares" -ContentType "application/json" -Body $body
```

Sample response:
```json
{
  "IDPoint": "ID1",
  "SSCC": "148102689000000010",
  "Status": "PalletResult",
  "Probability": "98",
  "Degree": "3",
  "Result": "Not found"
}
```

## Deploy to Vercel

### One-time setup
```powershell
# Install Vercel CLI
npm i -g vercel

# Login (follow prompts)
vercel login
```

### Deploy
```powershell
# From the project root
vercel

# Production deploy
vercel --prod
```

This repo includes `vercel.json` and an ASGI entry `api/index.py` that imports `app` from `main.py`. All routes are proxied to this ASGI app, so the endpoints are available at the deployed URL:
- `POST /api/setpallet`
- `POST /api/getcamerares`
