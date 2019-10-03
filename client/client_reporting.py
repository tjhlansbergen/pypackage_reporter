from pypackagereport import PyPackage, PyPackageReport
import pkg_resources
import datetime
import getpass
import socket

# functie voor het ophalen van Python package informatie
def gather_package_info() -> PyPackageReport:

    # Python packages ophalen, gesorteerd op naam
    dists = sorted(pkg_resources.working_set, key=lambda x: x.project_name)

    # rapport aanmaken met metadata
    report = PyPackageReport(datetime.datetime.now(), getpass.getuser(), socket.gethostname())

    # rapport vullen met packages
    for dist in dists:
        package = PyPackage(dist.project_name, dist.version, dist.location)
        report.packages.append(package)

    return report
