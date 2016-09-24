# Positional elements (columns) with the following indices -- and only those elements, at present --
# will be gathered and counted using a dictionary
dictable_cols = [4, 5, 6, 7, 8, 9, 10]

# let the data do the heavy lifting...everything is in this dict!
refs = {
    'lib': ['The Library', ['Harrison Dekker', 'Jamie Wittenberg', 'Susan Edwards', 'Steve Mendoza', 'Steven Mendoza',
                            'Margaret Phillips', 'data-consult list (Library)', 'Brian Quigley', 'Library',
                            'Data Storage/Sharing and the Social Sciences Working Group', 'Erik Mitchell', 'Susan Powell']],
    'css': ['Campus Shared Services - IT', ['Brett Larsen', 'Daniel Bass', 'Johnathon Kogelman', 'CSS-IT']],
    'dlab': ['D-Lab', ['D-Lab Consulting List', 'D-Lab', 'Jon Stiles', 'Zawadi Rucks Ahidiana']],
    'scf': ['Statistical Computing Facility', ['Chris Paciorek', 'Ryan Lovett']],
    'brc': ['Berkeley Research Computing',
            ['Patrick Schmitz', 'Aron Roberts', 'Aaron Culich', 'Jason Christopher', 'Kelly Rowland', 'Gary Jung',
             'BRC Cloud Consulting']],
    'dh': ['Digital Humanities @ Berkeley', ['Quinn Dombrowski', 'Camille Villa', 'Digital Humanities']],
    'rdm': ['RDM Consulting', ['researchdata@berkeley.edu', 'Rick Jaffe', 'Chris Hoffman']],
    'cdl': ['California Digital Library', ['Joan Starr', 'Stephanie Simms']],
    'ist': ['Information Services & Technology - API', ['Jennifer Bellenger', 'Jon Broshious', 'Ian Crew', 'Jon Hays', 'bConnected']],
    'micronet': ['Micronet', ['micronet', 'Micronet', 'micronet list', 'Micronet list']],
    'iao': ['Industry Alliances Office', ['Nicole Hensley', 'Nicole Hensley (IAO/IPIRA)']],
    'ssw': ['School of Social Welfare', ['David Fullmer']]
}

labels = ['', 'None', 'Unknown department', 'Unknown division', 'Consultation(s) without a partner', 'Unknown', '']

headings = ['Referrals In', 'Referrals Out', 'Departments Served, number of engagements', 'Library Division, number of engagements',
            'Organizational Partners, number of shared engagements', 'Patron Status, number of patrons', 'Consultation Complexity']
