# main.py - Clash Royale Backend API (EC2)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from clash_royale import Config, DeckSelector, create_comparator

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://ved-clash.s3-website.ap-south-1.amazonaws.com",
        "http://localhost:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Clash Royale Backend API running on EC2"}

@app.get("/api/data")
def get_clash_royale_data(deck_type: int = 1):
    """Fetch all Clash Royale data and deck selection as JSON."""
    config = Config(
        token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFhYmMyNmI0LWRjNTQtNDc1ZC05MjQwLTMzMmMwYTc3Mzg5NiIsImlhdCI6MTc3MzQyMTY4MCwic3ViIjoiZGV2ZWxvcGVyL2VhYjQ5OTQ3LWNiYjMtZWJlZC1mNzViLTgzNGFlODliMGFmZiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI2NS4yLjgyLjYwIl0sInR5cGUiOiJjbGllbnQifV19.Doj4jiELAtrA43rs_AdjkiG8H7vp2BN28u7arDzCjuqVZx6gGHiBvL9OZd7Lh9ZX06MtzsNwnDVpt-73hN2VGQ",
        boosted_cards=("megaminion", "zap"),
    )
    selector = DeckSelector(config)
    selector.load_cards()

    cards = [
        {
            "name": c.name,
            "badge_level": c.badge_level,
            "badge_max_level": c.badge_max_level,
            "badge_progress": c.badge_progress,
            "badge_target": c.badge_target,
            "level": c.level,
            "temp_level": c.temp_level,
            "card_type": c.card_type.name if c.card_type else None,
            "cr_card_type": c.clash_royale_card_type.name if c.clash_royale_card_type else None,
            "rarity": c.rarity.name if c.rarity else None,
            "elixirs": c.elixirs,
            "has_evolution": c.has_evolution,
            "count": c.count,
            "id": c.id,
            "achievement_lefts": c.achievement_lefts,
        }
        for c in selector.cards
    ]

    comparator = create_comparator('achievements_rarity_level')
    sorted_cards = selector.get_sorted_cards(comparator, include_low_achievements=True)
    deck = selector.select_deck(sorted_cards, 6)
    deck_data = [c.name for c in deck]

    return JSONResponse({
        "cards": cards,
        "deck": deck_data,
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
