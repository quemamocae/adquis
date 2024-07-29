def check_status(status):
    # Convert status to lowercase and check if 'unknown' is a substring
    if 'unknown' in status.lower():
        print("Status contains 'unknown'")
    else:
        print("Status does not contain 'unknown'")

# Testing with different cases
check_status("The status is unknown.")  # Output: Status contains 'unknown'
check_status("UNKNOWN location")        # Output: Status contains 'unknown'
check_status("Status: UnKnown")         # Output: Status contains 'unknown'
check_status("All clear")               # Output: Status does not contain 'unknown'
