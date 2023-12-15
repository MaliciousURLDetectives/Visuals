import folium
import json
import webbrowser
import folium
import pandas as pd
import requests
import os

os.chdir('C:\\Users\\georg\\OneDrive\\Desktop\\map')

states = []
df = pd.read_csv('Information.csv')
data = df['JSON Data']
for i in range(len(data)):
    states.append(json.loads(df['JSON Data'][i])['country_name'])

input_dict = {}
for i in states:
    if i in input_dict:
        input_dict[i] += 1
    else:
        input_dict[i] = 1

tot = sum(input_dict.values())

# Function to update values by dividing each value by 2
def divide_values_by_tot(input_dict):
    updated_dict = {}
    for key, value in input_dict.items():
        updated_dict[key] = 100 * value / tot
    return updated_dict

# Call the function to update values
input_dict = divide_values_by_tot(input_dict)
df = pd.DataFrame()
df['Country_Code'] = input_dict.keys()
df['Malicious'] = input_dict.values()
# Print the updated dictionary
df.to_csv('data.csv')

# Make the map from here
state_geo = requests.get("https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json").json()
state_data = pd.read_csv("data.csv")
state_data['Country_Code'][0] = 'USA'
state_data['Country_Code'][1] = 'RUS'
state_data['Country_Code'][2] = 'DEU'
state_data['Country_Code'][3] = 'AUS'
state_data['Country_Code'][4] = 'CAN'
state_data['Country_Code'][5] = 'GBR'
state_data['Country_Code'][6] = 'NLD'
state_data['Country_Code'][7] = 'FRA'
state_data['Country_Code'][8] = 'SGP'
state_data['Country_Code'][9] = 'IND'
state_data['Country_Code'][10] = 'AUT'
state_data['Country_Code'][11] = 'BRA'
state_data['Country_Code'][12] = 'DNK'
state_data['Country_Code'][13] = 'TUR'
state_data['Country_Code'][14] = 'MKD'
state_data['Country_Code'][15] = 'SGP'
state_data['Country_Code'][16] = 'NLD'
state_data['Country_Code'][17] = 'HKG'
state_data['Country_Code'][18] = 'FRA'
state_data['Country_Code'][19] = 'POL'
state_data['Country_Code'][20] = 'JPN'
state_data['Country_Code'][21] = 'MYS'
state_data['Country_Code'][22] = 'DZA'
state_data['Country_Code'][23] = 'CHN'
state_data['Country_Code'][24] = 'IDN'
state_data['Country_Code'][25] = 'ESP'
state_data['Country_Code'][26] = 'ITA'
state_data['Country_Code'][27] = 'CZE'
state_data['Country_Code'][28] = 'GBR'
state_data['Country_Code'][29] = 'VGB'
state_data['Country_Code'][30] = 'ARG'
state_data['Country_Code'][31] = 'SVK'
state_data['Country_Code'][32] = 'LVA'
state_data['Country_Code'][33] = 'SWE'
state_data['Country_Code'][34] = 'IRL'
state_data['Country_Code'][35] = 'UKR'
state_data['Country_Code'][36] = 'HUN'
state_data['Country_Code'][37] = 'FIN'
state_data['Country_Code'][38] = 'LTU'
state_data['Country_Code'][39] = 'VNM'
state_data['Country_Code'][40] = 'NZL'
state_data['Country_Code'][41] = 'GRC'
state_data['Country_Code'][42] = 'CHL'
state_data['Country_Code'][43] = 'AZE'
state_data['Country_Code'][44] = 'ROU'
state_data['Country_Code'][45] = 'COL'
state_data['Country_Code'][46] = 'BGR'
state_data['Country_Code'][47] = 'THA'
state_data['Country_Code'][48] = 'KOR'
state_data['Country_Code'][49] = 'IRN'
state_data['Country_Code'][50] = 'ZWE'
state_data['Country_Code'][51] = 'TWN'
state_data['Country_Code'][52] = 'SVN'
state_data['Country_Code'][53] = 'BEL'
state_data['Country_Code'][54] = 'PRT'
state_data['Country_Code'][55] = 'VUT'
state_data['Country_Code'][56] = 'KAZ'
state_data['Country_Code'][57] = 'GEO'
state_data['Country_Code'][58] = 'HRV'
state_data['Country_Code'][59] = 'ECU'
state_data['Country_Code'][60] = 'LUX'
state_data['Country_Code'][61] = 'PAK'
state_data['Country_Code'][62] = 'EST'
state_data['Country_Code'][63] = 'NOR'
state_data['Country_Code'][64] = 'BHS'
state_data['Country_Code'][65] = 'ARM'
state_data['Country_Code'][66] = 'BLR'
state_data['Country_Code'][67] = 'CHE'
state_data['Country_Code'][68] = 'GMB'
state_data['Country_Code'][69] = 'SRB'
state_data['Country_Code'][70] = 'TZA'
state_data['Country_Code'][71] = 'BGD'
state_data['Country_Code'][72] = 'SMR'
state_data['Country_Code'][73] = 'ISR'
state_data['Country_Code'][74] = 'VEN'
state_data['Country_Code'][75] = 'CRI'
state_data['Country_Code'][76] = '-'
state_data['Country_Code'][77] = 'MEX'
state_data['Country_Code'][78] = 'MOZ'
state_data['Country_Code'][79] = 'URY'
state_data['Country_Code'][80] = 'NPL'
state_data['Country_Code'][81] = 'UZB'
state_data['Country_Code'][82] = 'BIH'

# Create a Folium Map centered at the USA
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4,zoom_max=8, scrollWheelZoom=False)

# Add choropleth layer
choropleth = folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["Country_Code", "Malicious"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="% of Malicious URLs per Country",
).add_to(m)

# Add a custom tooltip for the USA
tooltip_html = """
    <div style="width: 250px; text-align: center;">
        <h4>{}</h4>
        <p>mal: {}%</p>
        <p>3,000 Malicious URLs in the US from our Dataset of 7000</p>
        <p>There can be millions or even Billions of harmful sites!</P>
    </div>
"""
tooltip_html2 = """
    <div style="width: 400px; text-align: center;">
        <h4>{}</h4>
        <p>mal: {}%</p>
        <p>This Was shocking seeing as how Russia along with North Korea and China</p>
        <p>are thought of as bad actors in a global stage with North Korea's infamous!</P>
        <p>Lazarus Cyber Group and their hack on SONY and stealing of bitcoin from South Korea</p>
        <p>to help fund their Nuclear Power Program. I expect that they deleted all their links</p>
        <p>and that's why there are so many Unknowns</p>
    </div>
"""

tooltip_html3 = """
    <div style="width: 300px; text-align: center;">
        <h4>{}</h4>
        <p>mal: {}%</p>
        <p>This came as a surprise but 20 percent of the maliciious URLS</p>
        <p>That we could extract information from came from Germany!</P>
    </div>
"""


usa_info = state_data[state_data["Country_Code"] == "USA"]
folium.Marker(
    location=[38.9072, -77.0369],
    tooltip=folium.Tooltip(
        tooltip_html.format("DEU", usa_info["Malicious"].values[0]),
        sticky=False,
        direction="right",
    ),
).add_to(m)


rus_info = state_data[state_data["Country_Code"] == "RUS"]
folium.Marker(
    location=[55.7558,37.6173],
    tooltip=folium.Tooltip(
        tooltip_html2.format("RUS", usa_info["Malicious"].values[0]),
        sticky=False,
        direction="right",
    ),
).add_to(m)

deu_info = state_data[state_data["Country_Code"] == "DEU"]
folium.Marker(
    location=[52.52,13.4050],
    tooltip=folium.Tooltip(
        tooltip_html3.format("DEU", usa_info["Malicious"].values[0]),
        sticky=False,
        direction="right",
    ),
).add_to(m)

# Add LayerControl to toggle layers on/off
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save("m.html")

# Open the map in a web browser
webbrowser.open("m.html")
