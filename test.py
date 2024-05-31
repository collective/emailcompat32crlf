# Very simple test file.  Just run `python test.py`
# No unittest/pytest/whatever, just assert statements.
#
# First import items from the email module, and then import our package,
# to show that it is fine if our patch is done later.
import email
from email.mime.text import MIMEText


# Define carriage return plus line feed.
CRLF = "\r\n"

# Do some tests to show that there really is a problem.
# If these fail, the package may not be needed anymore.
assert CRLF not in str(MIMEText("one\ntwo"))
assert CRLF not in str(email.message_from_string("one\ntwo"))
assert CRLF not in str(email.message_from_bytes(b"one\ntwo"))

# Importing the package activates the patch.
import emailcompat32crlf  # noqa

# Test that CRLF is used after our package is imported.
assert CRLF in str(MIMEText("one\ntwo"))
assert CRLF in str(email.message_from_string("one\ntwo"))
assert CRLF in str(email.message_from_bytes(b"one\ntwo"))

print("Ran tests.")
