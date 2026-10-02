from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from services import market_service

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Market Data API", description="API for market session data analysis")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/sessions/", response_model=schemas.MarketSession)
def create_session(session: schemas.MarketSessionCreate, db: Session = Depends(get_db)):
    db_session = models.MarketSession(
        symbol=session.symbol,
        session_date=session.session_date,
        point_of_control=session.point_of_control,
        total_volume=session.total_volume
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session


@app.get("/api/v1/sessions/", response_model=list[schemas.MarketSession])
def read_sessions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sessions = db.query(models.MarketSession).offset(skip).limit(limit).all()
    return sessions


@app.post("/api/v1/fetch-latest")
def fetch_latest_market_data(db: Session = Depends(get_db)):
    result = market_service.fetch_and_save_data(db)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result