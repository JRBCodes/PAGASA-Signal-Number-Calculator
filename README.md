# PAGASA Signal Number Calculator v.1.2
A really simple python program meant as teaching material for introductory python.  
This program accepts an integer input of wind speed and outputs the corresponding information:  
- **The signal number** (1 to 5)
- **Storm type** (tropical depression to super typhoon)
- **Potential impact** (minor to extreme)
- **Warning lead time.** (36 to 12 hrs)

All information are taken from **[PAGASA]([assets/pagasa.jpg](https://www.pagasa.dost.gov.ph/learning-tools/tropical-cyclone-wind-signal))** guidelines as of March 2022.

## Infographic
<img src="assets/pagasa.jpg" alt="PAGASA Infographic, if you see this text that means there is an error with the link." width="60%">

## Continue this code
```python
wind_speed = int(input("Input cyclone wind speed (km/h): "))

if wind_speed <= 61:
    print("Signal no. 1")
    #print more info

elif 62 <= wind_speed <= 88:
    print("Signal no. 2")
    #print more info
    
elif 89 <= wind_speed <= 117:
    print("Signal no. 3")
    #print more info

# Add signal number 5
else: # Program ends too early
    print("Signal no. 4")
```
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
If you finished early: **[Bonus Project](https://www.canva.com/design/DAGkTOHuzw4/shJy_3ikKQJWoMt4e29bUQ/view?utm_content=DAGkTOHuzw4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hcb69a864d8#111)**
