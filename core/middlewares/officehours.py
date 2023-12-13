from datetime import datetime
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message


def office_hours() -> bool:
    return datetime.now().weekday() in range(5) and datetime.now().hour in (
        i for i in range(8, 19)
    )


class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if office_hours():
            return await handler(event, data)

        await event.answer(
            "Время работы бота:\nПн-Пт с 8 до 18.\nПриходите в рабочие часы."
        )
