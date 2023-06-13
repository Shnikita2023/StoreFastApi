from fastapi import APIRouter, BackgroundTasks, Depends

from .tasks import send_email_report_dashboard

router_celery = APIRouter(prefix="/report", tags=["Email"])


@router_celery.get("/dashboard")
def get_dashboard_report(background_tasks: BackgroundTasks):
    # 1400 ms - Клиент ждет
    name = "Nikita"
    # send_email_report_dashboard(name)
    # 500 ms - Задача выполняется на фоне FastAPI в event loop'е или в другом треде
    background_tasks.add_task(send_email_report_dashboard, name)
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    # send_email_report_dashboard.delay(name)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }