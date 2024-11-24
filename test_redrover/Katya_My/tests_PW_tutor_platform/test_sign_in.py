from playwright.sync_api import Page, expect


def test_check_login_student(page, login_student):
    expect(page).to_have_url('http://195.133.27.184/list/')


def test_check_login_tutors(page, login_tutors):
    expect(page).to_have_url('http://195.133.27.184/list/')
