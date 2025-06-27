import sqlite3

DATABASE = "betting_pool.db"

# List of tuples: (FIFA code, Country Name)
countries = [
    ("AFG", "Afghanistan"), ("ALB", "Albania"), ("ALG", "Algeria"), ("AND", "Andorra"), ("ANG", "Angola"),
    ("ATG", "Antigua and Barbuda"), ("ARG", "Argentina"), ("ARM", "Armenia"), ("AUS", "Australia"), ("AUT", "Austria"),
    ("AZE", "Azerbaijan"), ("BAH", "Bahamas"), ("BHR", "Bahrain"), ("BAN", "Bangladesh"), ("BRB", "Barbados"),
    ("BLR", "Belarus"), ("BEL", "Belgium"), ("BLZ", "Belize"), ("BEN", "Benin"), ("BHU", "Bhutan"),
    ("BOL", "Bolivia"), ("BIH", "Bosnia and Herzegovina"), ("BOT", "Botswana"), ("BRA", "Brazil"), ("BRU", "Brunei"),
    ("BUL", "Bulgaria"), ("BFA", "Burkina Faso"), ("BDI", "Burundi"), ("CPV", "Cabo Verde"), ("CAM", "Cambodia"),
    ("CMR", "Cameroon"), ("CAN", "Canada"), ("CTA", "Central African Republic"), ("CHA", "Chad"), ("CHI", "Chile"),
    ("CHN", "China"), ("COL", "Colombia"), ("COM", "Comoros"), ("COD", "Congo DR"),
    ("CGO", "Congo"), ("CRC", "Costa Rica"), ("CIV", "Côte d'Ivoire"), ("CRO", "Croatia"),
    ("CUB", "Cuba"), ("CYP", "Cyprus"), ("CZE", "Czechia"), ("DEN", "Denmark"), ("DJI", "Djibouti"),
    ("DMA", "Dominica"), ("DOM", "Dominican Republic"), ("ECU", "Ecuador"), ("EGY", "Egypt"), ("SLV", "El Salvador"),
    ("EQG", "Equatorial Guinea"), ("ERI", "Eritrea"), ("EST", "Estonia"), ("SWZ", "Eswatini"), ("ETH", "Ethiopia"),
    ("FIJ", "Fiji"), ("FIN", "Finland"), ("FRA", "France"), ("GAB", "Gabon"), ("GAM", "Gambia"), ("GEO", "Georgia"),
    ("GER", "Germany"), ("GHA", "Ghana"), ("GRE", "Greece"), ("GRN", "Grenada"), ("GUA", "Guatemala"),
    ("GUI", "Guinea"), ("GBS", "Guinea-Bissau"), ("GUY", "Guyana"), ("HAI", "Haiti"), ("HON", "Honduras"),
    ("HUN", "Hungary"), ("ISL", "Iceland"), ("IND", "India"), ("IDN", "Indonesia"), ("IRN", "Iran"),
    ("IRQ", "Iraq"), ("IRL", "Ireland"), ("ISR", "Israel"), ("ITA", "Italy"), ("JAM", "Jamaica"), ("JPN", "Japan"),
    ("JOR", "Jordan"), ("KAZ", "Kazakhstan"), ("KEN", "Kenya"), ("KIR", "Kiribati"), ("PRK", "Korea DPR"),
    ("KOR", "South Korea"), ("KOS", "Kosovo"), ("KUW", "Kuwait"), ("KGZ", "Kyrgyzstan"), ("LAO", "Laos"),
    ("LVA", "Latvia"), ("LIB", "Lebanon"), ("LES", "Lesotho"), ("LBR", "Liberia"), ("LBY", "Libya"),
    ("LIE", "Liechtenstein"), ("LTU", "Lithuania"), ("LUX", "Luxembourg"), ("MAD", "Madagascar"), ("MAW", "Malawi"),
    ("MAS", "Malaysia"), ("MDV", "Maldives"), ("MLI", "Mali"), ("MLT", "Malta"), ("MHL", "Marshall Islands"),
    ("MTN", "Mauritania"), ("MRI", "Mauritius"), ("MEX", "Mexico"), ("FSM", "Micronesia"), ("MDA", "Moldova"),
    ("MON", "Monaco"), ("MNG", "Mongolia"), ("MNE", "Montenegro"), ("MAR", "Morocco"), ("MOZ", "Mozambique"),
    ("MYA", "Myanmar"), ("NAM", "Namibia"), ("NRU", "Nauru"), ("NEP", "Nepal"), ("NED", "Netherlands"),
    ("NZL", "New Zealand"), ("NCA", "Nicaragua"), ("NIG", "Niger"), ("NGA", "Nigeria"), ("MKD", "North Macedonia"),
    ("NOR", "Norway"), ("OMA", "Oman"), ("PAK", "Pakistan"), ("PLW", "Palau"), ("PLE", "Palestine"),
    ("PAN", "Panama"), ("PNG", "Papua New Guinea"), ("PAR", "Paraguay"), ("PER", "Peru"), ("PHI", "Philippines"),
    ("POL", "Poland"), ("POR", "Portugal"), ("QAT", "Qatar"), ("ROU", "Romania"), ("RUS", "Russia"),
    ("RWA", "Rwanda"), ("SKN", "Saint Kitts and Nevis"), ("LCA", "Saint Lucia"),
    ("VIN", "Saint Vincent and the Grenadines"), ("SAM", "Samoa"), ("SMR", "San Marino"),
    ("STP", "Sao Tome and Principe"), ("KSA", "Saudi Arabia"), ("SEN", "Senegal"), ("SRB", "Serbia"),
    ("SEY", "Seychelles"), ("SLE", "Sierra Leone"), ("SGP", "Singapore"), ("SVK", "Slovakia"), ("SVN", "Slovenia"),
    ("SOL", "Solomon Islands"), ("SOM", "Somalia"), ("RSA", "South Africa"), ("SSD", "South Sudan"),
    ("ESP", "Spain"), ("SRI", "Sri Lanka"), ("SDN", "Sudan"), ("SUR", "Suriname"), ("SWE", "Sweden"),
    ("SUI", "Switzerland"), ("SYR", "Syria"), ("TPE", "Chinese Taipei"), ("TJK", "Tajikistan"), ("TAN", "Tanzania"),
    ("THA", "Thailand"), ("TLS", "Timor-Leste"), ("TOG", "Togo"), ("TGA", "Tonga"),
    ("TRI", "Trinidad and Tobago"), ("TUN", "Tunisia"), ("TUR", "Turkey"), ("TKM", "Turkmenistan"),
    ("TUV", "Tuvalu"), ("UGA", "Uganda"), ("UKR", "Ukraine"), ("UAE", "United Arab Emirates"),
    ("ENG", "England"), ("USA", "United States"), ("URU", "Uruguay"), ("UZB", "Uzbekistan"),
    ("VAN", "Vanuatu"), ("VAT", "Vatican City"), ("VEN", "Venezuela"), ("VIE", "Vietnam"), ("WAL", "Wales"), ("YEM", "Yemen"),
    ("ZAM", "Zambia"), ("ZIM", "Zimbabwe")
]

def insert_countries():
    conn = sqlite3.connect(DATABASE)
    try:
        for fifa_code, name in countries:
            conn.execute(
                "INSERT OR IGNORE INTO country (code, name) VALUES (?, ?)",
                (fifa_code, name)
            )
        conn.commit()
        print("All countries inserted into the country table with FIFA codes.")
    finally:
        conn.close()

if __name__ == "__main__":
    insert_countries()