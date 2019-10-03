
class PyPackage:
    def __init__(self, name, version, location):
        self.packagename = name
        self.packageversion = version
        self.packagelocation = location

    def __eq__(self, other): 
        if not isinstance(other, PyPackage):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.packagename == other.packagename and self.packageversion == other.packageversion

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.packagename, self.packageversion))

class PyPackageReport:
    def __init__(self, timestamp, username, machinename):
        self.timestamp = timestamp
        self.username = username
        self.machinename = machinename
        self.packages = []

            