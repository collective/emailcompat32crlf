import email


# Patch the Compat32 class.
email.policy.Compat32.linesep = "\r\n"

# Patch the compat32 instance.
# You cannot directly set compat32.linesep.
# The email package itself prevents this, but we can do it in the same way
# that the email package does it.
object.__setattr__(email.policy.compat32, "linesep", "\r\n")
