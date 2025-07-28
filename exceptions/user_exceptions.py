from fastapi import HTTPException


USER_ALREADY_EXISTS = HTTPException(
    status_code=409, detail="Пользователь с таким email уже зарегистрирован"
)

USER_NOT_FOUND = HTTPException(status_code=404, detail="Пользователь не найден")

USER_TOKEN_INVALID = HTTPException(status_code=401, detail="Неверный токен")

USER_NOT_AUTHENTICATED = HTTPException(
    status_code=401, detail="Пользователь не авторизован"
)

USER_NOT_VERIFIED = HTTPException(
    status_code=400, detail="Пользователь не прошел верификацию"
)


USER_PASSWORDS_NOT_MATCH = HTTPException(status_code=400, detail="Пароли не совпадают")
