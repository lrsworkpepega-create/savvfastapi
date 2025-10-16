from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import uvicorn


class SetPalletRequest(BaseModel):
	SSCC: str
	IDPoint: str
	Message: Literal["PalletOnID"]
	Weight: float


class SetPalletResponse(BaseModel):
	SSCC: str
	Status: Literal["Ok"]


app = FastAPI(title="Savv API", version="1.0.0")


@app.post("/api/setpallet", response_model=SetPalletResponse)
async def set_pallet(payload: SetPalletRequest) -> SetPalletResponse:
	return SetPalletResponse(SSCC=payload.SSCC, Status="Ok")


class GetCameraResRequest(BaseModel):
	SSCC: str


class GetCameraResResponse(BaseModel):
	IDPoint: str
	SSCC: str
	Status: Literal["PalletResult"]
	Probability: str
	Degree: str
	Result: str

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/getcamerares", response_model=GetCameraResResponse)
async def get_camera_res(payload: GetCameraResRequest) -> GetCameraResResponse:
	return GetCameraResResponse(
		IDPoint="ID1",
		SSCC=payload.SSCC,
		Status="PalletResult",
		Probability="98",
		Degree="3",
		Result="Not found",
	)
if __name__ == "__main__":
	uvicorn.run(
		"main:app",
		host="0.0.0.0",
		port=8000,
		reload=True

	)
