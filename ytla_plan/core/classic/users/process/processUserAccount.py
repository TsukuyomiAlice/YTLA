# encode = utf-8
from core.classic.users.dao import daoUser
from core.classic.frame.func.loggerConfig import process_log
from core.classic.frame.instance.instanceProcessToRoutes import Response


@process_log
def create_new_user(user_data: dict):
    """
    Handle the business logic of creating a new user.

    Args:
        user_data (dict): A dictionary containing user data.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    if not daoUser.check_unique('username', user_data['username']):
        response.fail(code=400, msg='Username already exists')
        return response
    if not daoUser.check_unique('email', user_data['email']):
        response.fail(code=400, msg='Email already exists')
        return response
    if 'phone_number' in user_data and not daoUser.check_unique('phone_number', user_data['phone_number']):
        response.fail(code=400, msg='Phone number already exists')
        return response

    result = daoUser.create_user(user_data)
    if result['success']:
        response.success(data={'user_id': result['user_id']})
    else:
        response.fail(code=400, msg=result['error'])
    return response


@process_log
def verify_user_credentials(email: str, password: str):
    """
    Handle the business logic of verifying user credentials.

    Args:
        email (str): User email.
        password (str): User password.

    Returns:
        dict: A dictionary containing the verification result.
    """
    response = Response()
    result = daoUser.verify_credentials(email, password)
    if result['success']:
        response.success(data=result['user'])
    else:
        response.fail(code=400, msg=result['error'])
    return response


@process_log
def update_user_last_login(user_id: int, ip: str):
    """
    Handle the business logic of updating the user's last login information.

    Args:
        user_id (int): User ID.
        ip (str): Login IP address.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    try:
        daoUser.update_last_login(user_id, ip)
        response.success(data={})
    except Exception as e:
        response.fail(code=400, msg=str(e))
    return response


@process_log
def update_user_profile(user_id: int, user_data: dict):
    """
    Handle the business logic of updating user information.

    Args:
        user_id (int): User ID.
        user_data (dict): A dictionary containing updated user data.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    if 'username' in user_data and not daoUser.check_unique('username', user_data['username']):
        response.fail(code=400, msg='Username already exists')
        return response
    if 'email' in user_data and not daoUser.check_unique('email', user_data['email']):
        response.fail(code=400, msg='Email already exists')
        return response
    if 'phone_number' in user_data and not daoUser.check_unique('phone_number', user_data['phone_number']):
        response.fail(code=400, msg='Phone number already exists')
        return response

    result = daoUser.update_user_info(user_id, user_data)
    if result['success']:
        response.success(data={})
    else:
        response.fail(code=400, msg=result['error'])
    return response


@process_log
def soft_delete_user_account(user_id: int):
    """
    Handle the business logic of soft-deleting a user account.

    Args:
        user_id (int): User ID.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    try:
        result = daoUser.soft_delete_user(user_id)
        if result:
            response.success(data={})
        else:
            response.fail(code=400, msg='Failed to soft-delete user')
    except Exception as e:
        response.fail(code=400, msg=str(e))
    return response


@process_log
def deactivate_user_account(user_id: int):
    """
    Handle the business logic of deactivating a user account.

    Args:
        user_id (int): User ID.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    try:
        result = daoUser.deactivate_user(user_id)
        if result:
            response.success(data={})
        else:
            response.fail(code=400, msg='Failed to deactivate user')
    except Exception as e:
        response.fail(code=400, msg=str(e))
    return response


@process_log
def get_user_login_history(user_id: int, limit: int = 30):
    """
    Handle the business logic of getting the user's recent login history.

    Args:
        user_id (int): User ID.
        limit (int, optional): The maximum number of records to return, defaults to 30.

    Returns:
        dict: A dictionary containing the user's login history.
    """
    response = Response()
    try:
        history = daoUser.get_login_history(user_id, limit)
        response.success(data={"history": history})
    except Exception as e:
        response.fail(code=400, msg=str(e))
    return response
