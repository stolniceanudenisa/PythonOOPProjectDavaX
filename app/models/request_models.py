from pydantic import BaseModel, Field

class OperationRequest(BaseModel):
    operation: str = Field(..., description="The operation name (e.g., power, fibonacci, factorial)")
    inputs: dict = Field(..., description="The dictionary of inputs for the operation")
