from typing import List, Optional
from pydantic import BaseModel, Field


class SlideOutlineModel(BaseModel):
    title: str = Field(
        description="Title of the slide in about 3 to 5 words",
    )
    body: str = Field(
        description="Content of the slide in markdown format",
    )


class PresentationOutlineModel(BaseModel):
    title: str = Field(
        description="Title of the presentation in about 3 to 8 words",
    )
    notes: Optional[List[str]] = Field(default=None, description="Notes for the presentation")
    slides: List[SlideOutlineModel] = Field(description="List of slides")

    def to_string(self):
        message = f"# Presentation Title: {self.title} \n\n"
        for i, slide in enumerate(self.slides):
            message += f"## Slide {i+1}:\n"
            message += f"  - Title: {slide.title} \n"
            message += f"  - Body: {slide.body} \n"

        if self.notes:
            message += f"# Notes: \n"
            for note in self.notes:
                message += f"  - {note} \n"
        return message
