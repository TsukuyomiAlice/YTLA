# encode = utf-8
from core.users.dao import daoUser
from core.frame.func.loggerConfig import process_log
from core.frame.instance.instanceProcessToRoutes import Response


@process_log
def assign_user_role(user_id: int, role_name: str):
    """
    Handle the business logic of assigning a role to a user.

    Args:
        user_id (int): User ID.
        role_name (str): The name of the role to be assigned.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    result = daoUser.assign_role(user_id, role_name)
    if result['success']:
        response.success(data={})
    else:
        response.fail(code=400, msg=result['error'])
    return response


@process_log
def get_user_permission_list(user_id: int):
    """
    Handle the business logic of getting the user's permission list.

    Args:
        user_id (int): User ID.

    Returns:
        dict: A dictionary containing the user's permission list.
    """
    response = Response()
    try:
        permissions = daoUser.get_user_permissions(user_id)
        response.success(data={"permissions": permissions})
    except Exception as e:
        response.fail(code=400, msg=str(e))
    return response


@process_log
def check_user_permission(user_id: int, role_id: int):
    """
    Handle the business logic of checking if a user has a specific permission.

    Args:
        user_id (int): User ID.
        role_id (int): The role ID to be checked.

    Returns:
        dict: A dictionary containing the check result.
    """
    response = Response()
    result = daoUser.check_permission(user_id, role_id)
    if result['success']:
        response.success(data={})
    else:
        response.fail(code=400, msg=result['error'])
    return response


@process_log
def update_user_role(user_id: int, role_id: int):
    """
    Handle the business logic of updating user role information.

    Args:
        user_id (int): User ID.
        role_id (int): New role ID.

    Returns:
        dict: A dictionary containing the operation result.
    """
    response = Response()
    result = daoUser.update_role_info(user_id, role_id)
    if result['success']:
        response.success(data={})
    else:
        response.fail(code=400, msg=result['error'])
    return response
