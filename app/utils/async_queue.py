# app/utils/async_queue.py

import asyncio
from app.models.request_models import OperationRequest
from app.db.crud import insert_operation
from app.services.calculator import pow_op, fib_op, fact_op
from app.utils.logger import logger

task_queue = asyncio.Queue()

async def async_worker():
    while True:
        data = await task_queue.get()
        try:
            result = _dispatch(data)
            insert_operation(data, result)
            logger.info(f"Async task completed: {data.operation} -> {result}")

        except Exception as e:
            logger.error(f"Async task failed: {e}")
        finally:
            task_queue.task_done()

def _dispatch(data: OperationRequest):
    op = data.operation.lower()
    inputs = data.inputs

    if op == "power":
        return pow_op(inputs["base"], inputs["exponent"])
    elif op == "fibonacci":
        return fib_op(inputs["n"])
    elif op == "factorial":
        return fact_op(inputs["n"])
    else:
        raise ValueError("Unsupported operation")

async def submit_async_task(data: OperationRequest):
    await task_queue.put(data)
