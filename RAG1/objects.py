from pydantic import BaseModel, Field

class Answer(BaseModel):
    """
    Represents an answer object with a unique identifier and the answer text.
    """
     
    answer:str = Field(description="the answer that is needed for the user question")
    context:str = Field(description="this is the context that the agent used to reply to the user question")
    