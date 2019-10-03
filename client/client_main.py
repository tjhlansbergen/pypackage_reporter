# TODO voor alle bestanden header docstring comment toevoegen

from pypackagereport import PyPackage, PyPackageReport
import client_networking
import client_reporting
import client_constants
import client_io
import pickle

# hoofdfunctie, entrypoint van de client applicatie
def main():
    
    # controleer of er een nieuwe rapport gemaakt dient te worden
    if not client_io.new_report_needed():
        print(client_constants.MSG_REPORT_EXISTS)
        return  # direct beeindigen als recent rapport gevonden is en dus geen nieuwe rapport nodig is

    # terugkoppeling naar gebruiker
    print(client_constants.MSG_REPORT_NEEDED)

    # maak een nieuw rapport
    report = client_reporting.gather_package_info()

    # schrijf rapport lokaal weg
    client_io.store_as_json(report)
    
    # verzend rapport naar server
    pickled_report = pickle.dumps(report)
    client_networking.send_report(pickled_report)

    # terugkoppeling naar gebruiker
    print(client_constants.MSG_REPORT_CREATED)  
    
# laat python interpreter beginnen met main() functie
if __name__ == '__main__':
    main()
    