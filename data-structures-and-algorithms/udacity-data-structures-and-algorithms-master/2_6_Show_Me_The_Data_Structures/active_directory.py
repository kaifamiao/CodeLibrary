class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def _check_user(user, group, cache):
    if len(user) == 0 or group is None:
        return False
    if group.name in cache:
        return cache[group.name]

    if user in group.get_users():
        return True
    else:
        for group in group.get_groups():
            is_in_group = is_user_in_group(user, group)
            cache[group.name] = is_in_group
            if is_in_group:
                return True
    return False


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    Returns:
        bool: True if user is in the group, False otherwise
    """
    cache = dict()
    return _check_user(user, group, cache)


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)

    # Normal Cases:
    print('Normal Cases:')
    print(is_user_in_group(user='parent_user', group=parent))
    # False
    print(is_user_in_group(user='child_user', group=parent))
    # False
    print(is_user_in_group(user='sub_child_user', group=parent), '\n')
    # True
    # Edge Cases:
    print('Edge Cases:')
    print(is_user_in_group(user='', group=parent))
    # False
    print(is_user_in_group(user='', group=child))
    # False
