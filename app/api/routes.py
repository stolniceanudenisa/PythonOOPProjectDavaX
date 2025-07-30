from fastapi import APIRouter, HTTPException
from app.models.request_models import OperationRequest
from app.services.calculator import pow_op, fib_op, fact_op
from app.db.crud import insert_operation, fetch_all_operations
from app.utils.logger import logger
from app.utils.async_queue import submit_async_task


router = APIRouter()

@router.post("/compute")
def compute(data: OperationRequest):
    try:
        op = data.operation.lower()
        inputs = data.inputs

        if op == "power":
            result = pow_op(inputs["base"], inputs["exponent"])
        elif op == "fibonacci":
            result = fib_op(inputs["n"])
        elif op == "factorial":
            result = fact_op(inputs["n"])
        else:
            raise ValueError("Unsupported operation")

        insert_operation(data, result)
        return {"result": result}
    except Exception as e:
        logger.error(f"Compute error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/history")
def history():
    return fetch_all_operations()




@router.post("/compute_async")
async def compute_async(data: OperationRequest):
    try:
        await submit_async_task(data)
        return {"status": "accepted", "message": f"{data.operation} task queued"}
    except Exception as e:
        logger.error(f"Failed to queue async task: {e}")
        raise HTTPException(status_code=400, detail=str(e))
