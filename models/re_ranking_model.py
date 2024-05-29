from pydantic import BaseModel
from fastapi import HTTPException

class ReRankingModel(BaseModel):
    question: str = ''
    content: list = None
    top_k: int = 5

    def __init__(self, **data):
        super().__init__(**data)
        if self.content is None:
            raise HTTPException(status_code=404, detail="content Not Found.")
        if not isinstance(self.content, list):
            raise HTTPException(status_code=404, detail="content must be a list.")
        if not self.question:
            raise HTTPException(status_code=404, detail="question Not Found.")
        if len(self.content) < self.top_k:
            self.top_k = len(self.content)

    class Config:
        json_schema_extra = {
            "example": {
                "question": "What's your name?",
                "content": [
                    "My name is tnt",
                    "I am tnt",
                    "Tnt is my name"
                ],
                "top_k": 5
            }
        }
