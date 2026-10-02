import requests
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from datetime import datetime
import models

load_dotenv()


class MarketDataService:
    def __init__(self):
        self.api_key = os.getenv("VNHGI639S85IS99U")
        self.api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={self.api_key}"

    def fetch_and_save_data(self, db: Session):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()

            time_series = data.get("Time Series (Daily)", {})
            added_sessions = 0

            for date_str, daily_data in time_series.items():
                session_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                new_session = models.MarketSession(
                    symbol="IBM",
                    session_date=session_date,
                    point_of_control=float(daily_data["4. close"]),
                    total_volume=float(daily_data["5. volume"])
                )
                db.add(new_session)
                added_sessions += 1

                if added_sessions >= 5:
                    break

            db.commit()
            return {"status": "success", "message": f"Successfully fetched and saved {added_sessions} sessions from Alpha Vantage."}

        except Exception as e:
            return {"status": "error", "message": str(e)}


market_service = MarketDataService()