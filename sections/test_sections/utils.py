from users.models import User, UserRoles
from sections.models import Section, Question, Content

def get_admin_user(): 
    user = User.objects.create(
        email='tester_admin@test1.com',
        role=UserRoles.ADMIN,
        is_superuser=True,
        is_staff=True,
        is_active=True,        
    )
    user.set_password('qwerty')
    user.save()
    return user

def get_member_user():
    user = User.objects.create(
        email='tester_member@test2.com',
        role=UserRoles.MEMBER,
        is_superuser=False,
        is_staff=False,
        is_active=True,        
    )
    user.set_password('qwerty')
    user.save()
    return user

def get_test_section():
    section = Section.objects.create(
        title="Test Section",
        description='Test Description',
    )
    return section

def get_test_content():
    section = get_test_section()
    content = Content.objects.create(
        section=section,
        title="Test Title Content",
        content="Test Content",
    )
    return content
