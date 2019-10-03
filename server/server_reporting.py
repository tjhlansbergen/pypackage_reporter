from collections import Counter
import server_html
import server_css
import tempfile
import os

# lokale constante voor rapport lokatie
_REPORTER_HTML_PATH = os.path.join(tempfile.gettempdir(), "pypackage_reporter.html")

def write_html_report(client_reports):
    
    # data uit losse client-reports samenvoegen
    overview = report_aggregate(client_reports)

    # maak html pagina aan vanuit template
    resulting_html = server_html.HTML % ("PyPackage Reporter", server_css.CSS, overview_section(overview), single_machines_section(client_reports),  "&#169; 2019 - Novi Hogeschool")

    # schrijf weg naar schijf
    # TODO exceptie afhandeling
    with open(_REPORTER_HTML_PATH, "w") as f:
        f.write(resulting_html)

    print("Nieuw rapport aangemaakt in %s" % _REPORTER_HTML_PATH)

    return

def overview_section(overview) -> str:
    
    overview_html = ''

    # titel
    overview_html += '\n<br />\n<h2>Overview</h2>\n'

    # kop
    overview_html += '<div class=grid-container-overview>\n\t<div class=header-overview>Package:</div><div class="header-overview right">Version:</div><div class="header-overview right">Count:</div>\n'

    # maak html voor de unieke items
    for package, count in overview:
        overview_html += '\t<div><b>%s</b></div><div class="right">%s</div><div class="right">%s</div>\n' % (package.packagename, package.packageversion, count)

    # sluiten
    overview_html += '</div>\n'

    return overview_html


def single_machines_section(reports) -> str:
    
    section_html = ''

    for report in reports:

        # titel
        section_html += '\n<br />\n<h3>%s (%s)</h3>\n' % (report.machinename, report.username)

        # kop
        section_html += '<div class=grid-container-user>\n\t<div class=header-user>Package:</div><div class="header-user right">Version:</div>\n'

        # packages
        for package in report.packages:
            section_html += '\t<div><b>%s</b> (%s)</div><div class="right">%s</div>\n' % (package.packagename, package.packagelocation, package.packageversion)

        # sluiten
        section_html += '</div>\n'
        
    return section_html

def report_aggregate(reports) -> dict:

    # maak een totaal-lijst van alle packages in de losse reports met list-comprehension
    total_list = [package for report in reports for package in report.packages]

    # tel de unieke items op en return als dictionary, gesorteerd op aantal met hoogste aantal bovenaan
    return Counter(total_list).most_common()






    