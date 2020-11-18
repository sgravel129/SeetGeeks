import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


valid_test_user_email="test_frontend@test.com"
valid_test_user_password="Test_frontend!"

# Mock a sample user
test_user = User(
    id = 1,
    email=valid_test_user_email,
    name='test_frontend',
    password=generate_password_hash(valid_test_user_password),
    balance = 5000
)

# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'date': '12/24/2020', 'quantity':'1', 'email':'test_frontend@test.com'}
]


class test_R3(BaseCase):

	@patch('qa327.backend.get_user', return_value=test_user)
	@patch('qa327.backend.get_all_tickets', return_value=test_tickets)
	def test_logged_in_redirect_to_user_profile(self, *_):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")


	def test_this_page_header(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")
		self.assert_text("Hi test_frontend", "#welcome-header")


	def test_this_page_user_balance(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test user balance
		self.assert_element("#user_balance")
		self.assert_text("Balance: {{ user.balance }}", "#user_balance")


	def test_this_page_logout_link(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test logout link // added id to logout link
		self.assert_element("#logout_link")


	def test_this_page_all_tickets(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test that all ticket information is displayed
		self.assert_element("#tickets div h4")
		self.assert_text("t1 100", "#tickets div h4")
		self.assert_text("1 11/17/2020 test_frontend@test.com", "#tickets div p")


	def test_this_page_sell_tickets(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test sell ticket form
		self.assert_element("#name")
		self.assert_element("#quantity")
		self.assert_element("#price")
		self.assert_element("#expireDate")


	def test_this_page_buy_tickets(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test sell ticket form
		self.assert_element("#buyName")
		self.assert_element("#buyQuantity")


	def test_this_page_redirect_to_sell(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test sell ticket form
		self.click('input[type="submit", id="btn-submit"]')

		# Test on sell page now
		self.assert_element("#sell_header")


	def test_this_page_redirect_to_buy(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test buy ticket form
		self.click('input[type="submit", id="btn-submit2"]')

		# Test on buy page now
		self.assert_element("#buy_header")


	def test_this_page_redirect_to_update(self):
		# Open logout page, invalid any logged-in sessions that may exist
		self.open(base_url + '/logout')

		# Open login page
		self.open(base_url + '/login')

		# Fill email and password
		self.type("#email", valid_test_user_email)
		self.type("#password", valid_test_user_password)

		# Click submit button
		self.click('input[type="submit"]')

		# Open login page again
	#	self.open(base_url + '/login')

		# Test that current page contains #welcome-header (i.e. redirected to user profile page)
	#	self.assert_element("#welcome-header")

		# Test sell ticket form
		self.click('input[type="submit", id="btn-submit3"]')

		# Test on update page now
		self.assert_element("#update_header")




