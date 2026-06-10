<img width="1965" height="509" alt="Apparent Solar Time Calculator-2" src="https://github.com/user-attachments/assets/6ad867aa-687e-416b-8d0d-35f2caa8e2d5" />

![Python Versions](https://img.shields.io/pypi/pyversions/django) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![App](https://img.shields.io/badge/Streamlit-Live_App-brightgreen?logo=streamlit) ![Version](https://img.shields.io/badge/version-1.0.0-blue)


**Apparent Solar Time Calculator (ASTC)** corrects the local standard time (LST) from a given postcode in order to compute time, based on the observed position of the Sun. AST is calculated by adjusting LST using the eqaution of time and a longitude correction to account for Earth's orbital velocity and differences between the observors longitude and the LST meridian.

Those interested in testing the calculator can visit [ASTC](https://apparent-solar-time-calculator-kbrjjgpnz6cwahcpooonxn.streamlit.app/); and, (i) enter a UK postcode (either the first three digits or the full postcode); (ii) click the 'Calculate' button to run the function; and (iii) receive an output representing the AST. It is worth noting that while both postcode versions are supported, full postcodes generally provide more precise outputs. 

For project usage, feel free to copy the raw code into your own project and run it locally. Although the function is best-suited as a stand-alone tool, it can be integrated into existing applications for solar geometry; and while it is currently limited to UK postcodes, future versions will allow global applicabiltiy. You can find examples of how to use the calculator [here](https://github.com/billynunn/Apparent-Solar-Time-Calculator/tree/main/examples). 
