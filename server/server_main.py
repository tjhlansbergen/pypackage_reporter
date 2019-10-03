from pypackagereport import PyPackage, PyPackageReport
import server_networking
import server_reporting
import server_mocking
import pkg_resources
import datetime
import getpass
import socket


# hoofdfunctie, entrypoint van de server applicatie
def main():
    
    # tijdelijk, creeer rapport (deze komt later via networking binnen)
    reports = server_mocking.get_mock_reports(5)

    # creeer html
    server_reporting.write_html_report(reports)

    # server_networking.accept_report()

# laat python interpreter beginnen met main() functie
if __name__ == '__main__':
    main()
