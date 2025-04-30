# PAGASA Signal Number Calculator v.1.2
A really simple python program meant as teaching material for introductory python.  
This program accepts an integer input of wind speed and outputs the corresponding information:  
- **The signal number** (1 to 5)
- **Storm type** (tropical depression to super typhoon)
- **Potential impact** (minor to extreme)
- **Warning lead time.** (36 to 12 hrs)

All information is taken from **[PAGASA](https://www.pagasa.dost.gov.ph/learning-tools/tropical-cyclone-wind-signal)** guidelines as of March 2022.

## Infographic
<img src="https://pubfiles.pagasa.dost.gov.ph/pagasaweb/images/tropical-cyclone/old%20and%20new.jpg" alt="PAGASA Infographic, if you see this text that means there is an error with the link." width="60%">

## Expected Output
**Test cases:**

    Input cyclone wind speed (km/h): 20
    Signal no. 1
    Type: Tropical Depression
    Lead Time: 36 h
    Impact: Minor

    Input cyclone wind speed (km/h): 70
    Signal no. 2
    Type: Tropical Storm
    Lead Time: 24 h
    Impact: Moderate

    Input cyclone wind speed (km/h): 100
    Signal no. 3
    Type: Severe Tropical Storm
    Lead Time: 18 h
    Impact: Significant

    Input cyclone wind speed (km/h): 150
    Signal no. 4 
    Type: Typhoon
    Lead Time: 12 h
    Impact: Severe

    Input cyclone wind speed (km/h): 300
    Signal no. 5
    Type: Super Typhoon
    Lead Time: 12 h
    Impact: Catastrophic

## Link to Slides
Public view link: **[Create Your SySTEM](https://www.canva.com/design/DAGkTOHuzw4/shJy_3ikKQJWoMt4e29bUQ/view?utm_content=DAGkTOHuzw4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hcb69a864d8)**
