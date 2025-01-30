from fastapi import APIRouter, Depends
from app.controllers.auth_controller import AuthController
from app.main.schemas import UserCreate, UserLogin, UserOut

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, controller: AuthController = Depends()):
    """
    Registers a new user.
    """
    return controller.register_user(user)

@router.post("/login")
def login(user: UserLogin, controller: AuthController = Depends()):
    """
    Logs in a user and returns a JWT access token.
    """
    return controller.login_user(user)
