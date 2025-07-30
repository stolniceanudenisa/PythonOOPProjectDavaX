from .database import conn
from app.models.request_models import OperationRequest
from datetime import datetime
from app.utils.logger import logger

def insert_operation(data: OperationRequest, result: str):
    try:
        conn.execute('''
            INSERT INTO operations (operation, inputs, result, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (data.operation, str(data.inputs), str(result), datetime.utcnow().isoformat()))
        conn.commit()
        logger.info(f"Saved: {data.operation} | {data.inputs} = {result}")
    except Exception as e:
        logger.error(f"Insert failed: {e}")

def fetch_all_operations():
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT operation, inputs, result, timestamp FROM operations')
        return [dict(zip(["operation", "inputs", "result", "timestamp"], row)) for row in cursor.fetchall()]
    except Exception as e:
        logger.error(f"Fetch failed: {e}")
        return []
