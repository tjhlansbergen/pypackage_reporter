# mocking module that creates PyPackageReport objects as mock data

from pypackagereport import PyPackage, PyPackageReport
import pypackagereport
import pkg_resources
import datetime
import getpass
import socket
import random
import string
import copy

def get_mock_reports(n = 1) -> PyPackageReport:

    # lijst met reports
    reports = []

    # het eerste report is altijd een 'echte' uitdraai van de lokaal op de server geinstalleerd Python packages
    original_report = gather_package_info()
    reports.append(original_report)

    # als er maar één rapport gevraagd wordt return deze gelijk om onderstaande code over te slaan
    if n < 2:
        return reports

    for _ in range(n-1):
        # neem origineel rapport en verander
        new_report = randomly_alter_report(original_report)

        # en voeg toe
        reports.append(new_report)

    return reports


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

def randomly_alter_report(report) -> PyPackageReport:
    
    # maak kopie van object (zodat er een nieuw object bijkomt en het bestaande object ongewijzigd blijft)
    new_report = copy.deepcopy(report)

    # verander machinenaam
    new_report.machinename = "HOST-TEST%s" % random.randint(10, 99)

    # verwijder usernaam (niet relevant voor een testobect)
    new_report.username = "N/a"

    # verwijder willekeruig gekozen packages
    new_report.packages = random.sample(new_report.packages, random.randint(1, len(new_report.packages)))

    # introduceer nieuwe willekeurig gegenereerde 'packages'
    for _ in range(random.randint(0,5)):
        pkg = PyPackage(''.join(random.choices(string.ascii_lowercase, k=random.randint(4,10))), random.randint(10,199) / 10, "N/a")
        new_report.packages.append(pkg)

    return new_report
